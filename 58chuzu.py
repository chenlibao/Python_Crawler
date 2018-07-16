# import time
# # import requests
# # from bs4 import BeautifulSoup
# # from pymongo import MongoClient
# #
# # client = MongoClient()
# # zufang = client.chuzu58_db.zufang
# # headers = {
# #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# # }
# #
# # def get_info(url):
# #     html = requests.get(url,headers=headers)
# #     soup = BeautifulSoup(html.text,'lxml')
# #     titles = soup.select('.des > h2 > a')
# #     money = soup.select('.money')
# #     rooms = soup.select('.room')
# #     address = soup.select('.add')
# #     for title, money, room, address in zip(titles,money,rooms,address):
# #         data = {
# #             '租房描述':title.get_text().strip(),
# #             '租金':money.get_text().split('"')[0].strip(),
# #             '厅室':room.get_text().split()[0],
# #             '大小':room.get_text().split()[1],
# #             '地址':address.get_text().split()[0],
# #             '小区': address.get_text().split()[1]
# #         }
# #         print(data)
# #         # zufang_id = zufang.insert(data)
# #         print('-----------')
# #
# # if __name__ == "__main__":
# #     urls = {
# #         'http://sh.58.com/chuzu/?PGTID=0d100000-0000-2052-875c-3f128dcd30f8&ClickID={}'.format(str(i)) for i in range(1,2)
# #     }
# #     for url in urls:
# #         get_info(url)
# #         time.sleep(1)

import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
zufang = client.chuzu58_db.zufang
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_info(url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    titles = soup.select('.des > h2 > a')
    money = soup.select('.money')
    rooms = soup.select('.room')
    address = soup.select('.add')
    for title, money, room, address in zip(titles,money,rooms,address):
        data = {
            '租房信息':title.get_text().strip(),
            '价格':money.get_text().split('"')[0].strip(),
            '厅室':room.get_text().split()[0].strip(),
            '面积':room.get_text().split()[1].strip(),
            '地址':address.get_text().split()[0].strip()
        }
        zufang_id = zufang.insert(data)

if __name__ == "__main__":
    urls = {'http://sh.58.com/chuzu/?PGTID=0d100000-0000-2052-875c-3f128dcd30f8&ClickID={}'.format(str(i)) for i in range(1,5)}
    for url in urls:
        get_info(url)
        time.sleep(1)