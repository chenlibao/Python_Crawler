import re


class CreateUrl:
    def __init__(self, file, destFile):
        self.file = file
        self.destFile = destFile

    #从txt文件中获取基金代码code
    def get_code(self):
        with open(self.file, "r") as f:
            for line in f.readlines():
                l = re.match(r"http://fund.eastmoney.com/(\d+).html\s", line)
                url_code = l.group(1)
                print(url_code)
                self.get_new_url(url_code)

    #根据code构造新的url存入到新的txt文件中, a+表示可追加可写,文件不存在则创建
    def get_new_url(self, url_code):
        new_url = "http://fundf10.eastmoney.com/ccmx_" + url_code + ".html" + "\n"
        with open(self.destFile, "a+") as fl:
            fl.write(new_url)


if __name__ == "__main__":
    files = ["../data/etf_url.txt","../data/mix_url.txt","../data/stock_url.txt"]
    destFile = ["../data/new_etf_url.txt","../data/new_mix_url.txt","../data/new_stock_url.txt"]
    for i in range(3):
        cu = CreateUrl(files[i], destFile[i])
        cu.get_code()