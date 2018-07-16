import time
import re
# from multiprocessing import Pool
import requests
from  pymongo import MongoClient

client = MongoClient()
qiushibaike = client.qiushi_db.qiushibaike
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_info(url):
    html = requests.get(url,headers=headers)
    users = re.findall('<h2>(.*?)</h2>',html.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', html.text, re.S)
    laughs = re.findall('<span class="stats-vote">.*?<i class="number">(\d+)</i>(.*?)</span>', html.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', html.text, re.S)
    info = []
    for user,content,laugh,comment in zip(users,contents,laughs,comments):
        data = {
            '用户':user.strip(),
            '内容':content.strip(),
            '笑脸数量':laugh[0].strip()+laugh[1].strip(),
            '评论数':comment
        }
        info.append(data)
    print(info)

if __name__ == "__main__":
    urls = ['https://www.qiushibaike.com/8hr/page/{}/'.format(str(i)) for i in range(3,5)]
    start_time1 = time.time()
    for url in urls:
        get_info(url)
    end_time1 = time.time()
    print("time1:",end_time1-start_time1)
    #
    # start_time2 = time.time()
    # pool = Pool(processes=2)
    # pool.map(get_info,urls)
    # end_time2 = time.time()
    # print('time2:',end_time2-start_time2)
    #
    # start_time3 = time.time()
    # pool = Pool(processes=4)
    # pool.map(get_info,urls)
    # end_time3 = time.time()
    # print('time3:',end_time3-start_time3)

    # pool = Pool(processes=4)
    # pool.map(get_info,urls)