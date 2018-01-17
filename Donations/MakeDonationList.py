import io
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
def get_Members_list_from_donation(file='Rival Regions.html'):
    with io.open(file,mode='r', encoding='utf-8') as f:
        html=f.read()
        soup = BeautifulSoup(html, 'html.parser')
        tds=soup.findAll('td',{"class": "list_avatar pointer imp"},recursive=True)
        members=[]
        name_donation=[]
        tmp=0
        name_to_donations=dict()
        for nr,td in enumerate(tds):
            if nr%2==0:
                tmp=td
            else:
                name_donation.append([tmp,td])
        for name_td,donation_td in name_donation:
            name='error'
            donation='error'
            if 'slide/profile/' in str(name_td.get('action')):
                name=str(name_td.contents[0]).strip()
            donation=str(donation_td.find('span').contents[0]).strip().replace('.','')
            if name in name_to_donations:
                addStringToUser(donation,name_to_donations[name])
            else:
                name_to_donations[name]=dict()
                addStringToUser(donation,name_to_donations[name])


        return name_to_donations

def addStringToUser(donation, user_dict):
    number_unit=donation.split(' ')
    if number_unit[1] in user_dict:
        user_dict[number_unit[1]]+=int(number_unit[0])
    else:
        user_dict[number_unit[1]]=int(number_unit[0])

def dict_to_text(donations, amount_of_ppl=20):
    to_sort=[]
    name_to_value_donation=dict()
    for name in donations:
        for donation in donations[name]:
            if '$' in donation:
                if name in name_to_value_donation:
                    name_to_value_donation[name] += int(donations[name][donation])
                else:
                    name_to_value_donation[name] = int(donations[name][donation])
            elif 'bbl' in donation or 'kg' in donation:
                if name in name_to_value_donation:
                    name_to_value_donation[name] += int(donations[name][donation])*300
                else:
                    name_to_value_donation[name] = int(donations[name][donation])*300
            elif 'pcs' in donation:
                if name in name_to_value_donation:
                    name_to_value_donation[name] += int(donations[name][donation]) * 1500000
                else:
                    name_to_value_donation[name] = int(donations[name][donation]) * 1500000
            elif 'g' in donation:
                if name in name_to_value_donation:
                    name_to_value_donation[name] += int(donations[name][donation]) * 2500
                else:
                    name_to_value_donation[name] = int(donations[name][donation]) * 2500

    for k in name_to_value_donation:
        to_sort.append([k,name_to_value_donation[k]])
    to_sort.sort(key=itemgetter(1), reverse=True)
    objects = []
    performance = []

    for v in to_sort[:25]:
        name=v[0]
        sum=v[1]/ float(1000000)
        for donation in donations[name]:
            print(name, donation, donations[name][donation] / float(1000000), "in kk")
        objects.append(name)
        performance.append(sum)
    #Make bar chart
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects, rotation='vertical')
    plt.ylabel('Usage')
    plt.title('Donations')
    plt.ylabel('donations sum in kk, oil=ore=300$, diamonds=1.5kk$, uran=2500$')
    plt.tight_layout()
    plt.show()





dict_to_text(get_Members_list_from_donation())
#read_war()