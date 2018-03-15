
import urllib3
import time


from bs4 import BeautifulSoup as bs

stop_day=9
stop_moth='march'
stop_year=2018
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
            print(date.split(' '))
            if len(date.split(' '))>2:
                day,month,year,time=date.split(' ')
                print(side, damage, day, month, year, time)
                if not stop_year>int(year) and not month_to_int(stop_moth)<month_to_int(month) and not int(stop_day)<int(day):
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


def make_war_profil_for(header,url='http://rivalregions.com/#slide/profile/2000248613'):
    user_id=url.split('/')[-1]
    stop=False
    end_slash=0
    name=' Error Name'
    war_dict=dict()
    while not stop:
        time.sleep(1)
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
        print(war_link)
    print(war_dict)



myheader = \
        {
            "Host": "rivalregions.com",
            "Connection": "keep-alive",
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "DNT": "1",
            "Referer": "http://rivalregions.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
            "Cookie": "_ym_uid=1511307282951464034; fbm_1457231197822920=base_domain=.rivalregions.com; __cfduid=dedafd79af26a6580a9e0713059811ff81520122926; _ym_isad=2; _ym_visorc_20472997=w; PHPSESSID=baaunne8jmqh02rb30puns1v82; __atuvc=4%7C11; rr=ca2083b311e6a006c80486d39eef9a3d; rr_id=2000248613; rr_add=41245e12e10c55b3d0e8b0204c7d20f1"
        }
make_war_profil_for(myheader,url='http://rivalregions.com/#slide/profile/2000250635')
