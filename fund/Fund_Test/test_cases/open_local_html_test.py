from fund.src.Info import Info


def open_local_html_test(info):
    source_file = info.open_local_html()
    print(source_file)


if __name__ == "__main__":
    file = r"C:\Libao\Test\fund\data\new_mix_url.txt"
    info = Info(file)
    open_local_html_test(info)