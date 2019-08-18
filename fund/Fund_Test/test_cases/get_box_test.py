from fund.src.Info import Info


def get_box_test(info, soup):
    boxes = info.get_box(soup)
    print(boxes)
    print(len(boxes))


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    source_file = open("../results/test3.html", "r", encoding="utf-8")
    soup = info.get_soup(source_file)
    get_box_test(info, soup)