import requests
import re
import time
import os
from bs4 import BeautifulSoup
from sty import fg, bg, ef, rs

URL = "https://pid.cz/zastavkova-tabla/?stop=Hlavn%C3%AD&stanoviste=A"

def get_data():
    r = requests.get(URL)
    if r != None:
        soup = BeautifulSoup(r.content, 'html5lib')
    else:
        pass

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    data = []

    for row in rows:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        data.append(cols)
    del data[:2]

    x = 1
    list1 = []
    for s in range(30):
        list1.append(x)
        x = x + 3
    for i in reversed(list1):
        del data[i]

    y = 1
    list2 = []
    for q in range(30):
        list2.append(y)
        y = y + 2

    times = []
    for i in list2:
        l = [int(s) for s in re.findall(r'\b\d+\b', str(data[i]))]
        times.append(l[0])

    clear = lambda: os.system('clear')
    clear()
    
    print("{:<40}{:>40} min".format(fg.red + str(data[0][0]) + fg.rs + ' ' + data[0][1], fg.green + str(times[0]) + fg.rs))
    print("{:<40}{:>40} min".format(fg.red + str(data[2][0]) + fg.rs + ' ' + data[2][1], fg.green + str(times[1]) + fg.rs))
    print("{:<40}{:>40} min".format(fg.red + str(data[4][0]) + fg.rs + ' ' + data[4][1], fg.green + str(times[2]) + fg.rs))
    print("{:<40}{:>40} min".format(fg.red + str(data[6][0]) + fg.rs + ' ' + data[6][1], fg.green + str(times[3]) + fg.rs))
    print("{:<40}{:>40} min".format(fg.red + str(data[8][0]) + fg.rs + ' ' + data[8][1], fg.green + str(times[4]) + fg.rs))
    print("{:<40}{:>40} min".format(fg.red + str(data[10][0]) + fg.rs + ' ' + data[10][1], fg.green + str(times[5]) + fg.rs))
    print("================================================================")

while True:
    get_data()
    time.sleep(15)
