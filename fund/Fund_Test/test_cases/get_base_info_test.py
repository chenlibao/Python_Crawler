from fund.src.Info import Info


def get_base_test(info, soup):
    name = info.get_base_info(soup)
    print(name)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    source_file = open("../results/test3.html", "r", encoding="utf-8")
    soup = info.get_soup(source_file)
    get_base_test(info, soup)