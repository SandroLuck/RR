
import urllib3
import time

from collections import OrderedDict
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from operator import itemgetter

stop_day=9
stop_moth='march'
stop_year=2018
oberst = []
divisionar = []
leutnant = []
fourirer = []
korporal = []

def month_to_int(s):
    if s=='january':
        return 1
    if s=='february':
        return 2
    if s=='march':
        return 3
    if s=='april':
        return 4
    if s=='may':
        return 5
    if s=='june':
        return 6
    if s=='july':
        return 7
    if s=='august':
        return 8
    if s=='september':
        return 9
    if s=='october':
        return 10
    if s=='november':
        return 11
    if s=='december':
        return 12
    print("THIS IS NOT GOOD:",s)
    return -1000

def get_soup_to_link(header, link):
    http = urllib3.PoolManager()

    r = http.request('GET', link, headers=header)
    soup = bs(r.data)
    #print(soup)
    with open('log.html', 'w+') as f:
        f.write(str(soup.encode("utf-8")))
    return soup

def read_war_details(soup, war_dict,only_text=False):
    try:
        if not only_text:
            table = soup.findAll('table', recursive=True)[0]
            tbody = table.findAll('tbody', recursive=True)[0]
            wars = tbody.findAll('tr', {"class": "list_link header_buttons_hover"}, recursive=True)
        else:
            wars = soup.findAll('tr', {"class": "list_link header_buttons_hover turn_0 list_only"}, recursive=True)
        if len(wars)==0:
            return True

        for war in wars:
            fighting_for = war.findAll('td', {"class": "list_avatar pointer green"}, recursive=True)[0]
            side = fighting_for.contents[0]
            damage = war.findAll('td', {"class": "list_avatar yellow pointer small"}, recursive=True)[0].contents[0]
            damage = int(damage.split(' ')[0].replace('.', ''))
            date = war.findAll('td', {"class": "list_avatar pointer small"}, recursive=True)[0].contents[0]
            if len(date.split(' '))>2:
                day,month,year,time=date.split(' ')
                if stop_year>int(year):
                    print(date,"stop")
                    return True
                if stop_year<=int(year) and month_to_int(stop_moth)>month_to_int(month):
                    print(date,"stop")
                    return True
                if stop_year <= int(year) and month_to_int(stop_moth) == month_to_int(month) and int(day)<stop_day:
                    print(date,"stop")
                    return True
            if side in war_dict:
                war_dict[side] += damage
            else:
                war_dict[side] = damage
        return False
    except Exception as e:
        print(e)
        return True

def read_member_list(soup, member_list,only_text=False):
    try:
        if not only_text:
            members = soup.findAll('td', {"class": "list_name pointer"}, recursive=True)
        else:
            members = soup.findAll('td', {"class": "list_name pointer"}, recursive=True)
        if len(members)==0:
            return True

        for member in members:
            member_id=member['action']
            member_list.append(member_id.split('/')[-1])
        return False
    except Exception as e:
        print(e)
        return True


def make_war_profil_for(header,id_player='2000248613'):
    url='http://rivalregions.com/#slide/profile/'+str(id_player)
    user_id=url.split('/')[-1]
    stop=False
    end_slash=0
    name=' Error Name'
    war_dict=dict()
    try:
        while not stop:
            time.sleep(0.01)
            if end_slash>0:
                war_link = 'http://rivalregions.com/war/inall/' + user_id + "/" + str(end_slash)
                soup = get_soup_to_link(myheader, war_link)
                stop = read_war_details(soup,war_dict,only_text=True)
            else:

                war_link = 'http://rivalregions.com/war/inall/' + user_id
                soup = get_soup_to_link(myheader, war_link)
                name = soup.findAll('h1', {"class": "white slide_title"}, recursive=True)[0].contents[1].contents[0]
                stop = read_war_details(soup,war_dict)

            end_slash+=12
    except:
        pass
    return name,war_dict
def get_party_member_ids(myheader, url):
    party_id=url.split('/')[-1]
    stop=False
    end_slash=0
    name=' Error Name'
    member_list=[]
    while not stop:
        time.sleep(0.01)
        print('html starting')
        if end_slash>0:
            party_link = 'http://rivalregions.com/listed/party/' + party_id + "/" + str(end_slash)
            soup = get_soup_to_link(myheader, party_link)
            stop = read_member_list(soup,member_list,only_text=True)
        else:
            party_link = 'http://rivalregions.com/listed/party/' + party_id + "/" + str(end_slash)
            soup = get_soup_to_link(myheader, party_link)
            stop = read_member_list(soup,member_list)
            name = soup.findAll('span', {'class': 'dot results_date hov2 pointer'})[0].contents[0]

        end_slash+=25
    return name,member_list
def make_pie_chart_for_player(name,war_dict,plot):
    damage_wars=[]
    label_wars=[]
    legend=[]
    sum=0

    war_dict=OrderedDict(sorted(war_dict.items(), key=itemgetter(1),reverse=True))
    for war in war_dict:
        sum+=war_dict[war]/1000000
    if sum>300:
        if sum>5000:
            oberst.append((name,sum))
        elif sum>3000:
            divisionar.append((name,sum))
        elif sum>1000:
            leutnant.append((name,sum))
        elif sum>500:
            fourirer.append((name,sum))
        elif sum>300:
            korporal.append((name,sum))

    if True:
        for war in war_dict:

            damage_wars.append(war_dict[war]/1000000)
            if (war_dict[war]/1000000)/sum>0.05:
                label_wars.append(war)
            else:
                label_wars.append("")
            legend.append(str(war)+" "+str(war_dict[war]/1000000))
        patches, texts = plot.pie(damage_wars, labels=label_wars, startangle=90, radius=1.0)
        plot.legend(patches,legend, loc='center left', bbox_to_anchor=(1.0, 0.5),
                   fontsize=8)
        plot.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plot.text(0, 0, name + " War Distribution", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
        plot.text(0, -0.2, "Total Damage in kk: "+str(int(sum)), horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
def make_pie_chart_for_party(name,war_dict,plot):
    damage_wars=[]
    label_wars=[]
    legend=[]
    sum=0
    war_dict=OrderedDict(sorted(war_dict.items(), key=itemgetter(1),reverse=True))
    for war in war_dict:
        sum+=war_dict[war]/1000000
    if True:
        for war in war_dict:

            damage_wars.append(war_dict[war]/1000000)
            if (war_dict[war]/1000000)/sum>0.05:
                label_wars.append(war)
            else:
                label_wars.append("")
            legend.append(str(war)+" "+str(war_dict[war]/1000000))
        patches, texts = plot.pie(damage_wars, labels=label_wars, startangle=90, radius=1.0)
        plot.legend(patches,legend[:15], loc='center left', bbox_to_anchor=(1.0, 0.5),
                   fontsize=8)
        plot.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plot.text(0, 0, name + " War Distribution", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
        plot.text(0, -0.2, "Total Damage in kk: "+str(sum), horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')



def make_war_analysis_for_party(myheader,url='http://rivalregions.com/listed/party/87981'):
    party_name,member_id_list=get_party_member_ids(myheader, url=url)
    member_war_dict=dict()
    total_war_dict=dict()
    member_to_total=OrderedDict()

    for member in member_id_list:
        name,war_dict=make_war_profil_for(myheader, id_player=member)
        if len(war_dict)>0:
            member_war_dict[name]=war_dict
    for member in member_war_dict:
        for country in member_war_dict[member]:
            if country in total_war_dict:
                total_war_dict[country]+=member_war_dict[member][country]
            else:
                total_war_dict[country]=member_war_dict[member][country]
    for member in member_war_dict:
        member_total=0
        for country in member_war_dict[member]:
            member_total += member_war_dict[member][country]
        member_to_total[member]=member_total
    member_to_total=OrderedDict(sorted(member_to_total.items(), key=itemgetter(1),reverse=True))


    fig_size = plt.rcParams["figure.figsize"]
    fig_size[1] = (len(member_war_dict)+1)*3.5
    fig_size[0] = 6
    f, axarr = plt.subplots(len(member_war_dict)+1, sharex=True)

    for nr,member in enumerate(member_war_dict):
            make_pie_chart_for_player(member,member_war_dict[member],axarr[list(member_to_total.keys()).index(member)+1])
    make_pie_chart_for_party("Total of "+party_name,total_war_dict,axarr[0])
    plt.tight_layout()
    plt.savefig(party_name + '.png', dpi=200, bbox_inches='tight')


myheader = \
        {
            "Host": "rivalregions.com",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "DNT": "1",
            "Referer": "http://rivalregions.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
            "Cookie": "_ym_uid=1511307282951464034; fbm_1457231197822920=base_domain=.rivalregions.com; __cfduid=dedafd79af26a6580a9e0713059811ff81520122926; __atuvc=11%7C17; _ym_isad=2; rr=242ddb3ff07c8929a1df170193feaa2a; rr_id=2000248613; rr_add=fe22fac69be3cb99a0300ce36fc74540; PHPSESSID=sr0ng4usfisprc72n5bdpovlf1; _ym_visorc_20472997=w"
        }




make_war_analysis_for_party(myheader,url='http://rivalregions.com/#listed/party/87981')
#get_party_member_ids(myheader,url='http://rivalregions.com/listed/party/87981')
#make_war_profil_for(myheader,url='http://rivalregions.com/#slide/profile/1520824088829956')
print("Obersts:", oberst)
print("Divisionar:", divisionar)
print("leutnant:", leutnant)
print("fourier:", fourirer)
print("korporal:", korporal)