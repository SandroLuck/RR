from tkinter import *

import urllib3
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from operator import itemgetter
import os

stop_day=1
stop_month= 'january'
stop_year=2019
prices=dict()

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
    ##print("THIS IS NOT GOOD:",s)
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
    ##print("THIS IS NOT GOOD:",i)
    return -1000

def get_soup_to_link(header, link):
    http = urllib3.PoolManager()

    r = http.request('GET', link, headers=header)
    soup = bs(r.data)
    with open('log.html', 'w+') as f:
        f.write(str(soup.encode("utf-8")))
    return soup

def read_donationats_for_region(myheader,id,don_dict,updateString):
    url="http://rivalregions.com/listed/donated_regions/"+str(id)
    cont=True
    adder=0
    while(cont):
        if adder>0:
            cont,don_dict=read_donation_page(myheader, url, adder, don_dict,updateString,only_text=True)
        else:
            cont,don_dict=read_donation_page(myheader, url, adder, don_dict,updateString)

        if not cont:
            return don_dict
        adder+=25

def get_value_for_don(don):
    val=int(str(don).strip().split(" ")[0].replace(".",""))

    typ=str(don).strip().split(" ")[1]
    ##print(val,typ)

    if typ=='kg' or typ=='bbl':
        return val*prices['oil/ore']
    elif typ=="g":
        return val*prices['uran']
    elif typ=="$":
        return val*1
    elif typ=="pcs.":
        return val*prices['diamond']
    elif typ=="G":
        return val
    else:
        print(val,typ," ****** errror")


def read_donation_page(myheader,url,adder,don_dict,updateString,only_text=False):
    url=url+"/"+str(adder)
    soup=get_soup_to_link(myheader, url)
    #print(soup)
    if only_text:
        donations = soup.findAll('tr', {"class": "list_link header_buttons_hover turn_0 list_only"}, recursive=True)
        for don in donations:
            try:
                name = don.findAll('td', {"class": "list_avatar pointer imp"}, recursive=True)[0].contents[0].replace("\r","").replace("\n","").replace("\t","")
                date = don.findAll('td', {"class": "list_avatar pointer small"}, recursive=True)[0].contents[0]
                donation = don.findAll('span', recursive=True)[0].contents[0]
                #print(name,date,donation)
                if date_in_range(date):
                    if name in don_dict:
                        don_dict[name]=don_dict[name]+get_value_for_don(donation)
                    else:
                        don_dict[name]=get_value_for_don(donation)
                else:
                    print("STOPPER")
                    updateString.set(updateString.get()+'.')
                    return False,don_dict
            except Exception as e:
                print(e)
    else:
        donations = soup.findAll('tr', {"class": "list_link header_buttons_hover"}, recursive=True)
        for don in donations:
            name = don.findAll('td', {"class": "list_avatar pointer imp"}, recursive=True)[0].contents[0].replace("\r","").replace("\n","").replace("\t","")
            date = don.findAll('td', {"class": "list_avatar pointer small"}, recursive=True)[0].contents[0]
            donation = don.findAll('span', recursive=True)[0].contents[0]
            #print(name,date,donation)
            if date_in_range(date):
                if name in don_dict:
                    don_dict[name]=don_dict[name]+get_value_for_don(donation)
                else:
                    don_dict[name]=get_value_for_don(donation)
            else:
                #print("STOPPER")
                return False,don_dict
            #print(don_dict)
    return True,don_dict
def date_in_range(date):
    #print(date)
    if len(date.split(' ')) > 2:
        day, month, year, time = date.split(' ')
        if stop_year > int(year):
            #print(date, "stop")
            return False
        if stop_year <= int(year) and month_to_int(stop_month) > month_to_int(month):
            #print(date, "stop")
            return False
        if stop_year <= int(year) and month_to_int(stop_month) == month_to_int(month) and int(day) < stop_day:
            #print(date, "stop")
            return False
    return True

def make_donation_analysis(myheader,idStr,path,updateString,root):
    url = "http://rivalregions.com/map/state_details/"+str(idStr)
    print(url)
    updateString.set('Starting.')
    soup = get_soup_to_link(myheader, url)
    #print(soup)
    #print('SOUP>',soup)
    state_region_ids=[]
    players_to_dict=dict()
    regions = soup.findAll('div', {"class": "short_details tc tip header_buttons_hover float_left"}, recursive=True)
    #print("\n\nLength:",len(regions))
    updateString.set('Calculating {r} regions'.format(r=len(regions)))
    try:
        for region in regions:
            root.update()
            region_id=region.get('action').split("/")[2]
            state_region_ids.append(int(region_id))
            players_to_dict=read_donationats_for_region(myheader,region_id,players_to_dict,updateString)
            updateString.set('region',str(region))
    except Exception as e:
        updateString.set(str(e))

    #players_to_dict=read_donationats_for_region(myheader,state_region_ids[0],players_to_dict)
    make_stat(players_to_dict,path)
    updateString.set('Done')


def make_stat(player_dict,path):
    players=[]
    for play in player_dict:
        players.append([play,player_dict[play]])
    players.sort(key=itemgetter(1), reverse=True)
    #print(players)
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
    patches, texts = plt.pie(don_size, labels=don_name, startangle=90, radius=1.0, rotatelabels=True, shadow=True,)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')

    plt.legend(patches, leg, loc='center left', bbox_to_anchor=(1.0, 0.5),
                  fontsize=8)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.text(0, 0, "Donations in kkk", horizontalalignment='center', verticalalignment='center',
                 fontweight='bold')
    plt.savefig(path, dpi=200, bbox_inches='tight')


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
    #print(header_dict)
    return header_dict

class InputGuiSimple:
    def __init__(self, master):
        self.master = master
        self.path_entry_var=StringVar()
        init=str(os.path.dirname(os.path.abspath(__file__)))+"\RRDonations.png"
        self.path_entry_var.set(init)
        self.end_date_var=StringVar()
        self.end_date_var.set('2019.01.01')

        self.oil_var=StringVar()
        self.uranim_var=StringVar()
        self.diamond_var=StringVar()
        self.oil_var.set('160')
        self.uranim_var.set('1245')
        self.diamond_var.set('900000')

        master.title("Meschs RR Donator")
        self.title = Label(master, text="RR Donation Calculator!", width=25)
        self.cookie_label = Label(master, text="Request Header:", width=25)
        self.state_id_label = Label(master, text="State id:", width=25)
        self.end_date_label = Label(master, text="End Date(YYYY.MM.DD):", width=25)
        self.path_label = Label(master, text="Output Path(C:\\RRPDonations.png):", width=30)
        self.error_text=StringVar()
        self.error_hint = Label(master,textvariable=self.error_text, width=25,font=("Arial", 20),fg="red")




        self.oil_label = Label(master, text='Oil/Ore $:', width=25)
        self.uranium_label = Label(master, text="Uranium $:", width=30)
        self.diamond_label = Label(master, text="Diamonds $:", width=25)
        self.oil_entry = Entry(master, width=25,textvariable=self.oil_var)
        self.uranium_entry = Entry(master, width=25,textvariable=self.uranim_var)
        self.diamonds_entry = Entry(master, width=25,textvariable=self.diamond_var)

        self.cookie_input = Entry(master, width=25)
        self.state_id_input = Entry(master, width=25,text='')
        self.end_date_input = Entry(master, width=25,text='2019.01.01',textvariable=self.end_date_var)
        self.path_entry = Entry(master, width=25,text='C:\\RRDonations.png',textvariable=self.path_entry_var)


        self.make_donations_button = Button(master, text="Make Donations", command=self.makeDonations, width=25)

        self.close_button = Button(master, text="Close", command=master.quit, width=25)


        self.title.grid(row=0, column=0, rowspan=1)
        self.error_hint.grid(row=100, column=0, rowspan=2)
        self.cookie_label.grid(row=200, column=0)
        self.cookie_input.grid(row=300, column=0, rowspan=100)

        self.state_id_label.grid(row=500, column=0)

        self.state_id_input.grid(row=800, column=0)
        self.end_date_label.grid(row=900, column=0)
        self.end_date_input.grid(row=1000, column=0)
        self.path_label.grid(row=1100, column=0)
        self.path_entry.grid(row=1200, column=0)
        self.oil_label.grid(row=801, column=0)
        self.oil_entry.grid(row=802, column=0)
        self.uranium_label.grid(row=803, column=0)
        self.uranium_entry.grid(row=804, column=0)
        self.diamond_label.grid(row=805, column=0)
        self.diamonds_entry.grid(row=806, column=0)

        self.make_donations_button.grid(row=1400, column=0)
        self.close_button.grid(row=1500, column=0)
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
        #print('path in is:',path)
        folder='/'.join(path.split('/')[:-1])
        #print('folder is;',folder)
        if not os.path.isdir(folder):
            self.error_text.set('Issue with path')
            return
        try:
            prices['oil/ore']=int(self.oil_entry.get())
            prices['uran']=int(self.uranium_entry.get())
            prices['diamond']=int(self.diamonds_entry.get())


            header=format_cookie(self.cookie_input.get())
            make_donation_analysis(header, self.state_id_input.get(), path, self.error_text,root)
            #print('Input','\n'.join(header), int(self.state_id_input.get()),path)
            #print('Input','\n'.join(header), int(self.state_id_input.get()),path)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    #make_donation_analysis()
    root = Tk()
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    my_gui = InputGuiSimple(root)

    root.mainloop()