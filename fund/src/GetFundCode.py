from FundCode import FundCode

if __name__ == "__main__":
    url_mix = r"http://fund.eastmoney.com/data/fundrating.html#fthh"
    url_stock = r"http://fund.eastmoney.com/data/fundrating.html#ftgp"
    url_etf = r"http://fund.eastmoney.com/data/fundrating.html#ftzs"

    fc_mix = FundCode(url_mix, "mix_url")
    fc_mix.get_target_url()

    fc_stock = FundCode(url_stock, "stock_url")
    fc_stock.get_target_url()

    fc_etf = FundCode(url_etf, "etf_url")
    fc_etf.get_target_url()