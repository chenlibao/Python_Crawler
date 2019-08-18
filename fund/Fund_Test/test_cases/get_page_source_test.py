from fund.src.Info import Info


# 测试get_page_source,启动driver,获取源码,打印源码
def get_page_source_test(info, url, driver):
    page_source = info.get_page_source(url, driver)
    print(page_source)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    with open("../data/new_mix_url.txt", "r") as f:
        url = f.readline()
        driver = info.start_driver()
        get_page_source_test(info, url, driver)