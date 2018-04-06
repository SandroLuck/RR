import urllib3
import time

from collections import OrderedDict
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from operator import itemgetter
from collections import OrderedDict
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from operator import itemgetter
stop_day=4
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
    with open('log.html', 'w+') as f:
        f.write(str(soup.encode("utf-8")))
    return soup

myheader = \
        {
            "Host": " rivalregions.com",
            "Connection": " keep-alive",
            "Accept": " text/html, */*; q=0.01",
            "X-Requested-With": " XMLHttpRequest",
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "DNT": " 1",
            "Referer": " http//rivalregions.com/",
            "Accept-Encoding": " gzip, deflate",
            "Accept-Language": " en-US,en;q=0.9,de;q=0.8",
"Cookie": "_ym_uid=1511307282951464034; fbm_1457231197822920=base_domain=.rivalregions.com; __cfduid=dedafd79af26a6580a9e0713059811ff81520122926; _ym_isad=2; PHPSESSID=dq3b0av4ieevspa5kt0mus0p67; __atuvc=5%7C13%2C2%7C14; __atuvs=5ac32c881d9b0a5b000; _ym_visorc_20472997=w; rr=cd7f7f17d9ce17752ebe9d85876d4282; rr_id=2000248613; rr_add=fe22fac69be3cb99a0300ce36fc74540"
        }
def read_donationats_for_region(myheader,id,don_dict):
    url="http://rivalregions.com/listed/donated_regions/"+str(id)
    cont=True
    adder=0
    while(cont):
        if adder>0:
            cont,don_dict=read_donation_page(myheader, url, adder, don_dict,only_text=True)
        else:
            cont,don_dict=read_donation_page(myheader, url, adder, don_dict)

        if not cont:
            return don_dict
        adder+=25

def get_value_for_don(don):
    val=int(str(don).strip().split(" ")[0].replace(".",""))

    typ=str(don).strip().split(" ")[1]
    print(val,typ)

    if typ=='kg' or typ=='bbl':
        return val*190
    elif typ=="g":
        return val*1700
    elif typ=="$":
        return val
    elif typ=="pcs.":
        return val*1050000
    elif typ=="G":
        return val
    else:
        print(val,typ," ****** errror")


def read_donation_page(myheader,url,adder,don_dict,only_text=False):
    url=url+"/"+str(adder)
    soup=get_soup_to_link(myheader, url)
    if only_text:
        donations = soup.findAll('tr', {"class": "list_link header_buttons_hover turn_0 list_only"}, recursive=True)
        for don in donations:
            try:
                name = don.findAll('td', {"class": "list_avatar pointer imp"}, recursive=True)[0].contents[0].replace("\r","").replace("\n","").replace("\t","")
                date = don.findAll('td', {"class": "list_avatar pointer small"}, recursive=True)[0].contents[0]
                donation = don.findAll('span', recursive=True)[0].contents[0]
                print(name,date,donation)
                if date_in_range(date):
                    if name in don_dict:
                        don_dict[name]=don_dict[name]+get_value_for_don(donation)
                    else:
                        don_dict[name]=get_value_for_don(donation)
                else:
                    print("STOPPER")
                    return False,don_dict
            except Exception as e:
                print(e)
    else:
        donations = soup.findAll('tr', {"class": "list_link header_buttons_hover"}, recursive=True)
        for don in donations:
            name = don.findAll('td', {"class": "list_avatar pointer imp"}, recursive=True)[0].contents[0].replace("\r","").replace("\n","").replace("\t","")
            date = don.findAll('td', {"class": "list_avatar pointer small"}, recursive=True)[0].contents[0]
            donation = don.findAll('span', recursive=True)[0].contents[0]
            print(name,date,donation)
            if date_in_range(date):
                if name in don_dict:
                    don_dict[name]=don_dict[name]+get_value_for_don(donation)
                else:
                    don_dict[name]=get_value_for_don(donation)
            else:
                print("STOPPER")
                return False,don_dict
            print(don_dict)
    return True,don_dict
def date_in_range(date):
    print(date)
    if len(date.split(' ')) > 2:
        day, month, year, time = date.split(' ')
        if stop_year > int(year):
            print(date, "stop")
            return False
        if stop_year <= int(year) and month_to_int(stop_moth) > month_to_int(month):
            print(date, "stop")
            return False
        if stop_year <= int(year) and month_to_int(stop_moth) == month_to_int(month) and int(day) < stop_day:
            print(date, "stop")
            return False
    return True

def make_donation_analysis(myheader,url="http://rivalregions.com/map/state_details/2433"):
    soup = get_soup_to_link(myheader, url)
    state_region_ids=[]
    players_to_dict=dict()
    regions = soup.findAll('div', {"class": "short_details tc tip header_buttons_hover float_left"}, recursive=True)
    for region in regions:
        region_id=region.get('action').split("/")[2]
        state_region_ids.append(int(region_id))
        players_to_dict=read_donationats_for_region(myheader,region_id,players_to_dict)
    #players_to_dict=read_donationats_for_region(myheader,state_region_ids[0],players_to_dict)
    make_stat(players_to_dict)
def make_stat(player_dict):
    players=[]
    for play in player_dict:
        players.append([play,player_dict[play]])
    players.sort(key=itemgetter(1), reverse=True)
    print(players)
    don_size=[]
    don_name=[]
    leg=[]
    for i,j in players:
        ds=int(j/1000000000)
        dn=i
        leg.append(dn + " " + str(ds) + " kkk")
        if ds>300:
            don_name.append(dn)
        else:
            don_name.append(" ")
        don_size.append(ds)

    plt.clf()
    patches, texts = plt.pie(don_size, labels=don_name, startangle=90, radius=1.0, rotatelabels=True)
    plt.legend(patches, leg, loc='center left', bbox_to_anchor=(1.0, 0.5),
                  fontsize=8)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.text(0, 0, "Donations to Switzerland in kkk", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
    plt.savefig("SwissDonations"+ '.png', dpi=200, bbox_inches='tight')

make_donation_analysis(myheader)