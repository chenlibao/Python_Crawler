import time
# from multiprocessing import Pool
import requests
import re
from pymongo import MongoClient


client = MongoClient()
qiushi = client.qiushibaike_db.qiushi
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_info(url):
    html = requests.get(url,headers=headers)
    authors = re.findall('<h2>(.*?)</h2>',html.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',html.text,re.S)
    votes = re.findall('<span class="stats-vote">.?<i class="number">(\d+)</i>(.*?)</span>',html.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',html.text,re.S)
    for author,content,vote,comment in zip(authors,contents,votes,comments):
        data = {
            'author':author.strip(),
            'content':content.strip(),
            'votes':vote[0]+vote[1].strip(),
            'comment':comment
        }
        qiushi_id = qiushi.insert(data)

if __name__ == "__main__":
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,11)]
    for url in urls:
        get_info(url)
    time.sleep(1)