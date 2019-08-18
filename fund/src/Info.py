import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import datetime


class Info:

    def __init__(self, file):
        self.file = file

    def get_url(self):
        url_list = []
        with open(self.file, "r") as f:
            for line in f.readlines():
                url = line.split("\n")[0]
                url_list.append(url)
        return url_list

    def start_driver(self):
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        return driver

    def get_page_source(self, url, driver):
        driver.get(url)
        driver.implicitly_wait(5)
        page_source = driver.page_source
        return page_source

    def save_page_source(self, page_source):
        with open("../results/test3.html", "w", encoding="utf-8") as f:
            f.write(page_source)
        time.sleep(1)
        return

    def open_local_html(self):
        source_file = open("../results/test3.html", "r", encoding="utf-8")
        return source_file

    def get_soup(self, source_file):
        soup = BeautifulSoup(source_file, "lxml")
        return soup

    def get_base_info(self, soup):
        fund_name = soup.select(".col-left > h4 > a")[0].get_text()
        date_establishment = soup.select(".bs_gl > p > label > span")[0].get_text()
        fund_manager = soup.select(".bs_gl > p > label > a")[0].get_text()
        fund_type = soup.select(".bs_gl > p > label > span")[1].get_text()
        fund_company = soup.select(".bs_gl > p > label > a")[1].get_text()
        fund_scale = soup.select(".bs_gl > p > label > span")[2].get_text().strip().split("\n")[0]
        cut_off_date = soup.select(".bs_gl > p > label > span")[2].get_text().strip().split("\n")[1].strip()

        base_info = {
            "基金": fund_name,
            "成立日期": date_establishment,
            "基金经理": fund_manager,
            "类型": fund_type,
            "管理人": fund_company,
            "资产规模": fund_scale,
            "记录时间": cut_off_date
        }
        return base_info

    def get_box(self, soup):
        boxes = soup.select("#cctable > div > div")
        return boxes

    def get_table_info(self, boxes):
        today = '%s' % datetime.date.today()
        box = []
        for box in boxes:

            # ==========date_quarter===========
            quarter = box.select("h4 > label.left")[0]
            # 因为date_quarter中包含了双引号，直接传入match无法识别，格式化外层用单引号就可以解决问题
            date_q = '%s' % quarter
            dq = re.match(r"<label class=\"left\"><a href=\"http://fund\.eastmoney\.com/\d+\.html\">(.*)</a>(.*)</label>", date_q)
            date_quarter = dq.group(2).strip()
            # ============table=================
            tables = box.select("table")
            # ==========table_content===========
            for table in tables:
                trs = table.select("tbody > tr")
                for tr in trs:
                    stock_codes = tr.select("td > a")[0].get_text()
                    stock_name = tr.select("td > a")[1].get_text()
                    if len(tr.select("td.tor")) == 5:
                        price = tr.select("td.tor")[0].get_text()
                        try:
                            price = round(float(price), 2)
                        except ValueError:
                            price = 0
                        holding = tr.select("td.tor")[-3].get_text()
                        stock_num = tr.select("td.tor")[-2].get_text() + "万股"

                        num_qua = float(tr.select("td.tor")[-1].get_text().replace(',', ''))
                        num_cur = float(tr.select("td.tor")[-2].get_text().replace(',', ''))
                        quarter_market_value = round(num_qua * 0.0001, 4)
                        current_market_value = round(float(price * num_cur * 0.0001), 4)

                        box_new = {
                            "股票代码": stock_codes,
                            "股票名称": stock_name,
                            "当前价格": price,
                            "占净值比例": holding,
                            "持股数": stock_num,
                            "持仓市值（亿元）": quarter_market_value,
                            "当前市值（亿元）": current_market_value,
                            "季度": date_quarter,
                            "日期": today
                        }
                        print(box_new)
                        # self.save_to_MongoDB(box_new)
                    else:
                        holding = tr.select("td.tor")[-3].get_text()
                        stock_num = tr.select("td.tor")[-2].get_text() + "万股"
                        quarter_market_value = tr.select("td.tor")[-1].get_text() + "万元"

                        box_old = {
                            "股票代码": stock_codes,
                            "股票名称": stock_name,
                            "当前价格": "null",
                            "占净值比例": holding,
                            "持股数": stock_num,
                            "持仓市值": quarter_market_value,
                            "当前市值": "null",
                            "季度": date_quarter,
                            "日期": today
                        }
                        # self.save_to_MongoDB(box_old)
                        print(box_old)

    def save_to_MongoDB(self, box):
        pass

    def excute(self):
        url_list = self.get_url()
        driver = self.start_driver()
        for url in url_list:
            page_source = self.get_page_source(url, driver)
            self.save_page_source(page_source)
            source_file = self.open_local_html()
            soup = self.get_soup(source_file)
            base_info = self.get_base_info(soup)
            boxes = self.get_box(soup)
            table_info = self.get_table_info(boxes)
