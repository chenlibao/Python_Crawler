from fund.src.Info import Info


def get_url_test(file):
    info = Info(file)
    url_list = info.get_url()
    print(url_list)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    get_url_test(file)