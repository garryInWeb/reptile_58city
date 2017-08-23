from urllib import request
from bs4 import BeautifulSoup
import csv
def _reptile(url):
    resp = request.urlopen(url)
    html_data = resp.read().decode('utf-8')
    return html_data

def _Analysis(html):
    soup = BeautifulSoup(html,'html.parser')
    _room_area_list = soup.find_all('p',class_='room')
    _money_list = soup.find_all('div',class_='money')
    _link_list_div = soup.find_all('div',class_='des')
    _room_location = soup.find_all('p',class_='add')
    _house_information_list = []
    for item in range(_room_area_list.__len__()):
        _house_information = {}
        _room_area = _clean_string(_room_area_list[item].string)
        _money = _money_list[item].find('b').string
        _link = _link_list_div[item].find('h2').find('a').attrs['href']
        _room_location_district = _room_location[item].find_all('a')[0].string
        if _room_location[item].find_all('a').__len__() >= 2:
            _room_location_place = _room_location[item].find_all('a')[1].string
        else:
            _room_location_place = None
        if _room_location[item].contents.__len__() > 6:
            _room_location_street = _room_location[item].contents[6]
        else:
            _room_location_street = None

        _house_information['_room_area'] = _room_area
        _house_information['_money'] = _money
        _house_information['_link'] = _link
        _house_information['_room_location_district'] = _room_location_district
        _house_information['_room_location_place'] = _room_location_place
        _house_information['_room_location_street'] = _room_location_street

        _house_information_list.append(_house_information)
    return _house_information_list
def _clean_string(string):
    result = string.replace(' ','')
    return result
def csv_write(str):
    with open('58_house_informaiton_dg.csv', 'w', newline='') as csvfile:
        fieldname = ['room_area', 'money','link','room_location_district','room_location_place','room_location_street']
        writer = csv.DictWriter(csvfile, fieldnames=fieldname)
        writer.writeheader()
        for item in str:
            writer.writerow({'room_area': item['_room_area'], 'money': item['_money'],'link':item['_link'],'room_location_district':item['_room_location_district'],
                             'room_location_place':item['_room_location_place'],'room_location_street':item['_room_location_street']})
list = []
for i in range(60):
    html = _reptile('http://dg.58.com/chuzu/pn' + str(i) + '/')
    list += _Analysis(html)
csv_write(list)