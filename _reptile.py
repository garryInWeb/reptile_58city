from urllib import request
from bs4 import BeautifulSoup
def _reptile(url):
    resp = request.urlopen(url)
    html_data = resp.read().decode('utf-8')
    return html_data

def _Analysis(html):
    soup = BeautifulSoup(html,'html.parser')
    _li_list = soup.find_all('li')
    _house_list_information = []
    for item in _li_list[1:]:
        _house_information = {}
        if (item.find('p', class_='room') is not None):
            _room_area = item.find('p', class_='room')
        if (_room_area is not None):
            _house_information['_room_area'] = _clean_string(_room_area.string)
        if(item.find('div',class_='money') is not None):
            _money = item.find('div',class_='money').find('b')
            if (_money is not None):
                _house_information['_money'] = _money.string
        _house_list_information.append(_house_information)
    print(_house_list_information)
def _clean_string(string):
    result = string.replace(' ','')
    result = result.replace('\xa0','')
    return result
html = _reptile('http://sz.58.com/chuzu/pn1/')
_Analysis(html)