import os
import sys
from tkinter import *
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
stop_day=1
stop_month= 'january'
stop_year=2019

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

def int_to_month(i):
    if i==1:
        return 'january'
    if i==2:
        return 'february'
    if i==3:
        return 'march'
    if i==4:
        return 'april'
    if i==5:
        return 'may'
    if i==6:
        return 'june'
    if i==7:
        return 'july'
    if i==8:
        return 'august'
    if i==9:
        return 'september'
    if i==10:
        return 'october'
    if i==11:
        return 'november'
    if i==12:
        return 'december'
    print("THIS IS NOT GOOD:",i)
    return -1000

def get_soup_to_link(header, link):
    http = urllib3.PoolManager()

    r = http.request('GET', link, headers=header)
    soup = bs(r.data)
    with open('log.html', 'w+') as f:
        f.write(str(soup.encode("utf-8")))
    return soup

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
        if stop_year <= int(year) and month_to_int(stop_month) > month_to_int(month):
            print(date, "stop")
            return False
        if stop_year <= int(year) and month_to_int(stop_month) == month_to_int(month) and int(day) < stop_day:
            print(date, "stop")
            return False
    return True

def make_donation_analysis(myheader,id,path):
    url = "http://rivalregions.com/map/state_details/"+str(id)
    soup = get_soup_to_link(myheader, url)
    print(soup)
    state_region_ids=[]
    players_to_dict=dict()
    regions = soup.findAll('div', {"class": "short_details tc tip header_buttons_hover float_left"}, recursive=True)
    print("\n\nLength:",len(regions))
    for region in regions:
        region_id=region.get('action').split("/")[2]
        state_region_ids.append(int(region_id))
        players_to_dict=read_donationats_for_region(myheader,region_id,players_to_dict)
    #players_to_dict=read_donationats_for_region(myheader,state_region_ids[0],players_to_dict)
    make_stat(players_to_dict,path)
def make_stat(player_dict,path):
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
    plt.text(0, 0, "Donations in kkk", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
    plt.savefig(path, dpi=200, bbox_inches='tight')



myheader = \
        {
            "Host": "rivalregions.com",
            "Connection": "keep-alive",
            'Upgrade-Insecure-Requests': '1',
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": " XMLHttpRequest",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            "DNT": "1",
            "Referer": "http//rivalregions.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
            "Cookie": '__cfduid=dfed188bff52c1448ff18cfcb3e73ea151526622148; _ym_uid=1526622145533126521; _iub_cs-76236742=%7B%22consent%22%3Atrue%2C%22timestamp%22%3A%222018-05-18T05%3A42%3A34.985Z%22%2C%22version%22%3A%221.2.2%22%2C%22id%22%3A76236742%7D; PHPSESSID=q6q6igdtvclgda6elvkoud0ae0; __atuvc=1%7C3; __atuvs=5c3fad4d717eedd7000; _ym_d=1547677006; _ym_isad=1; _ym_visorc_20472997=w; rr=f49e0325f85aae2455c9ab47d745c85f; rr_id=2000248613; rr_add=151117b3509ac7758c52a27dd00ca409'
        }


def format_cookie(str):
    split=str.split('\n')
    header_dict=dict()
    for line in split:
        if 'HTTP' in line and 'GET' in line:
            continue
        key_val=line.split(':')
        key = key_val[0].strip()
        val = key_val[1].strip()
        header_dict[key]=val
    print(header_dict)
    return header_dict

class InputGuiSimple:
    def __init__(self, master):
        self.master = master
        master.title("Meschs RR Donator")
        self.title = Label(master, text="RR Donation Calculator!", width=50)
        self.cookie_label = Label(master, text="Request Header:", width=50)
        self.state_id_label = Label(master, text="State id:", width=50)
        self.end_date_label = Label(master, text="End Date(YYYY.MM.DD):", width=50)
        self.path_label = Label(master, text="Output Path(C:\\pathToPlace\\nameOfFile.png):", width=50)
        self.error_text=StringVar()
        self.error_hint = Label(master,textvariable=self.error_text, width=50,font=("Arial", 20),fg="red")


        self.cookie_input = Entry(master, width=50)
        self.state_id_input = Entry(master, width=50)
        self.end_date_input = Entry(master, width=50)
        self.path_entry = Entry(master, width=50)


        self.make_donations_button = Button(master, text="Make Donations", command=self.makeDonations, width=50)

        self.close_button = Button(master, text="Close", command=master.quit, width=50)


        self.title.grid(row=0, column=0, columnspan=100)
        self.error_hint.grid(row=1, column=0, columnspan=100)
        self.cookie_label.grid(row=2, column=0, columnspan=100)
        self.cookie_input.grid(row=3, column=0, columnspan=100)

        self.state_id_label.grid(row=5, column=0, columnspan=100)

        self.state_id_input.grid(row=8, column=0, columnspan=100)
        self.end_date_label.grid(row=9, column=0, columnspan=100)
        self.end_date_input.grid(row=10, column=0, columnspan=100)
        self.path_label.grid(row=11, column=0, columnspan=100)
        self.path_entry.grid(row=12, column=0, columnspan=100)
        self.make_donations_button.grid(row=14, column=0, columnspan=100)
        self.close_button.grid(row=15, column=0, columnspan=100)

    def makeDonations(self):
        #set date
        try:
            date_str=self.end_date_input.get().split('.')
            stop_year=int(date_str[0])
            stop_month=int_to_month(int(date_str[1].replace('0','')))
            stop_day=int_to_month(int(date_str[2].replace('0','')))
        except:
            self.error_text.set('Issue with date')
            return
        path=self.path_entry.get().replace('\\','/')
        print('path in is:',path)
        folder='/'.join(path.split('/')[:-1])
        print('folder is;',folder)
        if not os.path.isdir(folder):
            self.error_text.set('Issue with path')
            return
        header=format_cookie(self.cookie_input.get())
        make_donation_analysis(header, int(self.state_id_input.get()),path)

root = Tk()
frame=Frame(root,
            border=1,
            relief=GROOVE,
            background="white",
            )
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=30, column=100, sticky=N+S+E+W)



my_gui = InputGuiSimple(root)

root.mainloop()