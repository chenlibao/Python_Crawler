from selenium import webdriver
from bs4 import BeautifulSoup


class FundCode:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    # webdriver模拟浏览器，用BeautifulSoup解析html，获取soup
    def get_soup(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        return soup

    # 定位，找到所有的tr标签
    def get_trs(self):
        soup = self.get_soup()
        tbody = soup.select("#lbtable > tbody")
        trs = tbody[0].select("tr")
        return trs

    # 找到每个tr标签下a标签href属性值，并写入到txt文件中
    def get_target_url(self):
        trs = self.get_trs()
        file = "../data/%s.txt" % self.filename
        with open(file, 'w+') as f:
            for tr in trs:
                # 使用get(key)方法就可以获得a标签中key的属性值
                target_url = tr.select("td.dm > a")[0].get('href') + "\n"
                f.write(target_url)