from fund.src.Info import Info


def get_table_info_test(info, boxes):
    info.get_table_info(boxes)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    source_file = open("../results/test3.html", "r", encoding="utf-8")
    soup = info.get_soup(source_file)
    boxes = info.get_box(soup)
    get_table_info_test(info, boxes)
