from bs4 import BeautifulSoup
import io
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec


def get_damage_side_party(file='Rival Regions.html',til_plot=50):
    with io.open(file, mode='r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        tds = soup.findAll('tr', {"class": "list_link header_buttons_hover turn_0 list_only"}, recursive=True)
        members = []
        lis_party_data=[]
        for t in tds:
            name_and_side=t.findAll('td', {"class": "list_name pointer"}, recursive=True)[0].contents
            name=name_and_side[0]
            side=name_and_side[2].contents[0]
            damage=int(t.findAll('td', {"class": "list_level"}, recursive=True)[0].contents[0].contents[0].replace('.',''))
            lis_party_data.append([name,side,damage])
        lis_party_data.sort(key=itemgetter(2), reverse=True)

        make_plot_from_list(lis_party_data[:til_plot])

        print_percentage_of_side(lis_party_data[:til_plot])
        print_percentage_of_side(lis_party_data[:til_plot],side='Defending side')

def make_plot_from_list(lis):
    objects = []
    performance = []
    colors=[]
    don_list = ''
    not_list = ['Mesch', 'White', 'Frisch', 'Alan', 'Helljumper', 'Mac']
    not_list = ['sostupidtowriteblalalal']
    for v in lis[:25]:
        objects.append(v[0])
        performance.append(v[2])
        if(v[1]=='Attacking side'):
            colors.append('red')
        else:
            colors.append('blue')
    # Make bar chart
    plt.clf()
    ax = plt.gca()
    ax.axes.get_yaxis().get_major_formatter().set_scientific(False)
    y_pos = np.arange(len(objects))
    print(don_list)
    plt.bar(y_pos, performance,color=colors, align='center')
    plt.xticks(y_pos, objects, rotation='vertical')
    plt.ylabel('Usage')
    plt.title('Damage in War')
    plt.ylabel('Total Damage of party')
    plt.text(5, max([i for i in performance]) * 0.9, "Blue=Defending side, Red=Attacking Side")
    plt.tight_layout()
    plt.savefig('Total Damage comparison'+'.png',dpi=300, bbox_inches='tight')

def print_percentage_of_side(lis, rounding=3,side='Attacking side'):
    plt.clf()
    sum_att=0
    lab_att=[]
    size_att=[]
    for i in lis:
        if i[1]==side:
            sum_att+=i[2]
    print(10*'*',side,10*'*')
    for i in lis:
        if i[1]==side:
            print(i[0],i[2],' Percentage of'+side+':'+str(100.0*round((i[2]/float(sum_att)),rounding)))
            lab_att.append(i[0]+" "+str(round(100.0*round((i[2]/float(sum_att)),rounding),rounding))+' %')
            size_att.append(100.0*round((i[2]/float(sum_att)),rounding))
    patches, texts = plt.pie(size_att, labels=lab_att, startangle=90, radius=1.0, rotatelabels=True)
    plt.legend(patches, lab_att, loc='center left', bbox_to_anchor=(1.0, 0.5),
               fontsize=8)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.text(0,0,'Party Damage '+side, horizontalalignment='center',verticalalignment='center',fontweight='bold')
    plt.savefig(side+'.png',dpi=300, bbox_inches='tight')


get_damage_side_party()