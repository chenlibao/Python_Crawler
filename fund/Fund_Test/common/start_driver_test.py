from fund.src.Info import Info


# 测试start_driver,成功启动driver,则打印成功启动
def start_driver_test(info):
    driver = info.start_driver()
    print("Start driver successfully")
    return driver


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    start_driver_test(info)