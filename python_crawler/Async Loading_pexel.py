# -*- coding= utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

headers = {
		'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
	}

# urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(1,2)]
urls = ['https://www.pexels.com/?page=1']
photos = []
for url in urls:
	html = requests.get(url,headers=headers)
	soup = BeautifulSoup(html.text,'lxml')
	imgs = soup.select('a.js-photo-link > img')
	for img in imgs:
		photo = img.get('src')
		photos.append(photo)
path = "E://python/work/test/"
for photo_url in photos:
	photo_html = requests.get(photo_url,headers=headers)
	photo_names = re.findall('\d+\/(.*?)\?auto',photo_url)
	fp = open(path+photo_names[0],'wb')
	fp.write(photo_html.content)
	fp.close()