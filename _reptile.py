from urllib import request
from bs4 import BeautifulSoup
def _reptile(url):
    resp = request.urlopen(url)
    html_data = resp.read().decode('utf-8')
    return html_data

def _Analysis(html):
    soup = BeautifulSoup(html,'html.parser')
    listUL = soup.find_all('ul',class_='listUl')
    list_house_list = listUL[0].find_all('li')
    _house_list_information = []
    for item in list_house_list:
        _house_information = {}
        if(item.find_all('p',class_='room') is not None):
            _house_information['_room_area'] = item.find_all('p',class_='room')[0].string
        #if(item.find_all('div',class_='money') is not None):
            # _house_information['_money'] = item.find_all('div',class_='money')[0].find_all('b')[0].string
        #_location = item.find_all('p',class_='add')[0]
        _house_list_information.append(_house_information)
    print(_house_list_information)
html = _reptile('http://sz.58.com/chuzu/pn1/')
_Analysis(html)