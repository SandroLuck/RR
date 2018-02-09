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

def dict_to_text(donations, amount_of_ppl=20,filter=''):
    to_sort=[]
    name_to_value_donation=dict()
    print(donations)
    for name in donations:
        if "SIP" in name:
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
    don_list=''
    not_list=['Mesch','White','Frisch','Alan','Helljumper','Mac']
    not_list=['sostupidtowriteblalalal']
    for v in to_sort[:25]:
        name=v[0]
        if(not_in_list(name,not_list)):
            sum=v[1]/ float(1000000000)
            for donation in donations[name]:
                don_list+=str(name+" "+str(donation)+" "+ str(donations[name][donation] / float(1000000))+" "+"in kkk\n")
            objects.append(name)
            performance.append(sum)
    #Make bar chart
    y_pos = np.arange(len(objects))
    print(don_list)
    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects, rotation='vertical')
    plt.ylabel('Usage')
    plt.autoscale(enable=True, axis='y')
    plt.title('Donations')
    plt.ylabel('Donations in kkk')
    plt.text(5,max([i for i in performance])*0.9,"oil=ore=300$, diamonds=1.5kk$, uran=2500$")
    plt.text(5,max([i for i in performance])*0.9,"oil=ore=300$, diamonds=1.5kk$, uran=2500$")
    plt.tight_layout()
    plt.show()
def not_in_list(text,not_list):
    for i in not_list:
        if i in text:
            return False
    return True
def get_Lottery_Tickets(donations):
    to_del=[]
    print(donations)
    for k in donations:
        if '[SIP]' in k:
            to_del.append(k)
    for k in to_del:
        donations.pop(k,None)
    name_to_tickets=dict()
    for k in donations:
        sum=0

        for don in donations[k]:
            if 'bbl' in don or 'kg' in don:
                sum+=donations[k][don]
        name_to_tickets[k]=int(sum/float(10000000))+int(0.1*sum/float(10000000))
    return name_to_tickets

def get_numbers_for_each_user(name_tickets):
    sum=np.sum([int(name_tickets[k]) for k in name_tickets])
    print('Total tickets:',sum)
    counter=1
    for name in name_tickets:
        print('Name: ',name,' Numbers: from and with,',counter,' to and with:',counter+name_tickets[name]-1,"\nAmount of tickets:",name_tickets[name], "Chance to win in a draw: ",100.0*(name_tickets[name]/float(sum)),' %',' Donations in kk: ',name_tickets[name]-int(name_tickets[name]*0.1))
        counter+=name_tickets[name]

    objects = []
    performance = []
    for v in name_tickets:
        name=v
        tickets=int(name_tickets[v])
        objects.append(name)
        performance.append(tickets)
    #Make bar chart
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects, rotation='vertical')
    plt.ylabel('Usage')
    plt.title('Tickets')
    plt.ylabel('Tickets')
    plt.text(5,max([i for i in performance])*0.9,"Tickets total: {}".format(sum))
    plt.tight_layout()
    plt.show()





#get_numbers_for_each_user(get_Lottery_Tickets(get_Members_list_from_donation()))
dict_to_text(get_Members_list_from_donation())
#read_war()