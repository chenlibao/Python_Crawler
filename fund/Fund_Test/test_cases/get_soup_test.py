from fund.src.Info import Info


def get_soup_test(info, source_file):
    soup = info.get_soup(source_file)
    print(soup)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    source_file = open("../results/test3.html", "r", encoding="utf-8")
    get_soup_test(info, source_file)