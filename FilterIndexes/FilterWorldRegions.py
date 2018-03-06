from bs4 import BeautifulSoup
import io
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


def read_world_regions(file='Rival Regions.html'):
    with io.open(file, mode='r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        tds = soup.findAll('tr', {"class": "list_link header_buttons_hover"}, recursive=True)
        lis_region_data=[]
        region=dict()
        for t in tds:
            name=t.findAll('td', {"class": "list_name pointer small"}, recursive=True)[0].contents[0]
            citizens=t.findAll('td', {"class": "list_level yellow"}, recursive=True)[0].contents[0]
            indexes=t.findAll('td',recursive=True)
            health=indexes[3].get('rat').split('.')
            military=indexes[4].get('rat').split('.')
            school=indexes[5].get('rat').split('.')
            house=indexes[6].get('rat').split('.')
            tmp=dict()
            tmp['Health index']=int(health[0])
            tmp['Health']=int(health[1])

            tmp['Military index']=int(military[0])
            tmp['Military']=int(military[1])

            tmp['School index']=int(school[0])
            tmp['School']=int(school[1])

            tmp['House index']=int(house[0])
            tmp['House']=int(house[1])
            tmp['Citizens']=int(citizens)
            region[name]=tmp
    return region

def box_plot_index(dict,key_ind, key, index, plot):
    data=[]
    for reg_name in dict:
        region=dict[reg_name]
        if region[key_ind]==index:
            data.append(region[key])
    average=np.mean(data)
    min=np.min(data)
    max=np.max(data)
    if not max==min:
        plot.text(0.55,(max+average)/2.0,key_ind+":"+str(index),fontsize=12)
        plot.text(1.1,min,'Minimum level:'+str(min),fontsize=12)
        plot.text(1.1,(max+average)/2.0,'Maximum level:'+str(max),fontsize=12)
        plot.text(0.55,min,'Average level:'+str(int(average)),fontsize=12)
    else:
        plot.text(0.55,max+20,key_ind+":"+str(index),fontsize=12)
        plot.text(0.55,min,'Average=Min=Max:'+str(int(average)),fontsize=12)

    plot.boxplot(data)

def plot_for_an_indexe(index, name, regions,til_limit=11):
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[1] = 30
    fig_size[0] = 6

    f, axarr = plt.subplots(til_limit, sharex=True)
    for i in range(1,til_limit+1):
        box_plot_index(regions, index, name, i, axarr[i-1])
    plt.tight_layout()
    plt.savefig(name+'.png',dpi=200, bbox_inches='tight')
    plt.clf()

def plot_for_all_indexes():
    regions=read_world_regions()
    plot_for_an_indexe('Health index','Health',regions)
    plot_for_an_indexe('School index','School',regions)
    plot_for_an_indexe('Military index','Military',regions)
    plot_for_an_indexe('House index','House',regions,til_limit=10)

def plot_distribution_of_citizens(file='country.html'):
    regions=read_world_regions()
    with io.open(file, mode='r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        tds = soup.findAll('a', {"class": "dot hov2"}, recursive=True)
        name_country=tds[0].contents[0]
        lis_region_data=[]
        lable_regs=[]
        size_regs=[]
        to_sort=[]
        country_regs=soup.findAll('div', {"class": "short_details tc tip header_buttons_hover float_left"}, recursive=True)
        for i in country_regs:
            to_sort.append([i.contents[0].strip()+" citizens:"+str(regions[i.contents[0].strip()]['Citizens']),regions[i.contents[0].strip()]['Citizens']])
        to_sort.sort(key=itemgetter(1), reverse=True)
        for i in to_sort:
            lable_regs.append(i[0])
            size_regs.append(i[1])

        plt.clf()
        patches, texts = plt.pie(size_regs, labels=lable_regs, startangle=90, radius=1.0, rotatelabels=True)
        plt.legend(patches, lable_regs, loc='center left', bbox_to_anchor=(1.0, 0.5),
                   fontsize=8)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.text(0, 0, name_country+" Citizen Distribution", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
        plt.savefig(name_country + '.png', dpi=300, bbox_inches='tight')

def plot_distribution_of_citizens_world():
    regions=read_world_regions()
    lable_regs=[]
    size_regs=[]
    to_sort=[]
    for i in regions:
        to_sort.append([i, regions[i]['Citizens']])
    to_sort.sort(key=itemgetter(1), reverse=True)
    for i in to_sort[:50]:
        lable_regs.append(i[0]+' citizens:'+str(i[1]))
        size_regs.append(i[1])

    plt.clf()
    patches, texts = plt.pie(size_regs, labels=lable_regs, startangle=90, radius=1.0, rotatelabels=True)
    plt.legend(patches, lable_regs, loc='center left', bbox_to_anchor=(1.0, 0.5),
                  fontsize=8)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.text(0, 0, "Wolrd"+" Citizen Distribution", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
    plt.savefig("World Citizens"+ '.png', dpi=300, bbox_inches='tight')

#plot_distribution_of_citizens_world()
#plot_distribution_of_citizens()
plot_for_all_indexes()