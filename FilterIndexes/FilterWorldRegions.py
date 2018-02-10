from bs4 import BeautifulSoup
import io
import matplotlib.pyplot as plt
import numpy as np

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

plot_for_all_indexes()