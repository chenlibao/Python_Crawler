from fund.src.Info import Info


def save_page_source_test(info, page_source):
    info.save_page_source(page_source)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    with open("../data/new_mix_url.txt", "r") as f:
        url = f.readline()
        driver = info.start_driver()
        page_source = info.get_page_source(url, driver)
        save_page_source_test(info, page_source)