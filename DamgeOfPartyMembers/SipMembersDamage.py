from bs4 import BeautifulSoup
import io
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def get_damage_of_sip_members(file='Rival Regions.html'):
    with io.open(file, mode='r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        tds = soup.findAll('tr', {"class": "list_link header_buttons_hover turn_0 list_only"}, recursive=True)
        lis_party_data=[]
        for t in tds:
            name_and_side=t.findAll('td', {"class": "list_name pointer"}, recursive=True)[0].contents
            name=name_and_side[0]
            lv=int(t.findAll('td', {"class": "list_level"}, recursive=True)[0].contents[0].contents[0].replace('.',''))
            damage=int(t.findAll('td', {"class": "list_level"}, recursive=True)[1].contents[0].contents[0].replace('.',''))
            lis_party_data.append([name,lv,damage])
        #Do it now also for other class since RR admins are crazy wierd programms
        tds = soup.findAll('tr', {"class": "list_link header_buttons_hover"}, recursive=True)
        for t in tds:
            name_and_side=t.findAll('td', {"class": "list_name pointer"}, recursive=True)[0].contents
            name=name_and_side[0]
            lv=int(t.findAll('td', {"class": "list_level"}, recursive=True)[0].contents[0].contents[0].replace('.',''))
            damage=int(t.findAll('td', {"class": "list_level"}, recursive=True)[1].contents[0].contents[0].replace('.',''))
            lis_party_data.append([name,lv,damage])

        lis_party_data.sort(key=itemgetter(2), reverse=True)
        for i in lis_party_data:
            print(i)
        plot_party_damage_pie(lis_party_data)

def plot_party_damage_pie(lis,tag='[SIP]',rounding=4):
    plt.clf()
    sum_att=0
    lab_att=[]
    size_att=[]
    for i in lis:
        if tag in i[0]:
            sum_att+=i[2]
            print(i[0])
    for i in lis:
        if tag in i[0]:
            print(i[0],i[2],' Percentage of party damage:'+str(100.0*round((i[2]/float(sum_att)),rounding)))
            lab_att.append(i[0]+" "+str(round(100.0*round((i[2]/float(sum_att)),rounding),rounding))+' %')
            size_att.append(100.0*round((i[2]/float(sum_att)),rounding))
    patches, texts = plt.pie(size_att, labels=lab_att, startangle=90, radius=1.0, rotatelabels=True)
    plt.legend(patches, lab_att, loc='center left', bbox_to_anchor=(1.0, 0.5),
               fontsize=8)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.text(0,0,tag+' Party Damage', horizontalalignment='center',verticalalignment='center',fontweight='bold')
    plt.savefig(tag+'.png',dpi=300, bbox_inches='tight')




get_damage_of_sip_members()