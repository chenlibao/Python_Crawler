import requests
import json
from pymongo import MongoClient
import pandas as pd
import time

client = MongoClient()
chigu_Zhongjin = client.stock_chigu_db.chigu_Zhongjin
chigu_Shebao104 = client.stock_chigu_db.chigu_Shebao104
chigu_Shebao403 = client.stock_chigu_db.chigu_Shebao403
chigu_Shebao103 = client.stock_chigu_db.chigu_Shebao103
chigu_Huijin = client.stock_chigu_db.chigu_Huijin
chigu_Shebao101 = client.stock_chigu_db.chigu_Shebao101
chigu_Shebao110 = client.stock_chigu_db.chigu_Shebao110


def get_stock_list(url):
    cookie = [
        'searchGuide=sg; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1503478626; __utma=156575163.1936459573.1503289139.1518485846.1518510403.54; __utmz=156575163.1518510403.54.54.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; spversion=20130314; usersurvey=1; _sm_au_c=iVV6pjvpDFZ30npN0e; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1524205112,1524554540,1524712710,1524897558; reviewJump=nojump; historystock=000069%7C*%7C002672%7C*%7C601566%7C*%7C000995; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1524908610; v=Av-SgIzkmdJgmp3Ow6WtYWU4jtiM5FImbTtXcZHMm2Tx1RUMmbTj1n0I58mi',
        'searchGuide=sg; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1503478626; __utma=156575163.1936459573.1503289139.1518485846.1518510403.54; __utmz=156575163.1518510403.54.54.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; spversion=20130314; usersurvey=1; _sm_au_c=iVV6pjvpDFZ30npN0e; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1524205112,1524554540,1524712710,1524897558; reviewJump=nojump; historystock=000069%7C*%7C002672%7C*%7C601566%7C*%7C000995; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1524908610; v=As-iEDzUySKQis1ek2190bUIXmjc9CFKvU4nBuHcaKZBIuWc6cSzZs0Yt17y',
        'searchGuide=sg; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1503478626; __utma=156575163.1936459573.1503289139.1518485846.1518510403.54; __utmz=156575163.1518510403.54.54.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; spversion=20130314; usersurvey=1; _sm_au_c=iVV6pjvpDFZ30npN0e; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1524205112,1524554540,1524712710,1524897558; reviewJump=nojump; historystock=000069%7C*%7C002672%7C*%7C601566%7C*%7C000995; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1524908610; v=AkcqqPSM0TpYolW2SwN1OW1Q1vAUTBgWdSmfrhk0YPb5BW1kIRyrfoXwL_cq',
        'searchGuide=sg; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1503478626; __utma=156575163.1936459573.1503289139.1518485846.1518510403.54; __utmz=156575163.1518510403.54.54.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; spversion=20130314; usersurvey=1; _sm_au_c=iVV6pjvpDFZ30npN0e; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1524205112,1524554540,1524712710,1524897558; reviewJump=nojump; historystock=000069%7C*%7C002672%7C*%7C601566%7C*%7C000995; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1524908610; v=AoLve-EzbLlVNXBlvmb42lBn04PhU4W3OFt6nMybrWGkjii3tOPWfQjnyqef',
        'searchGuide=sg; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1503478626; __utma=156575163.1936459573.1503289139.1518485846.1518510403.54; __utmz=156575163.1518510403.54.54.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; spversion=20130314; usersurvey=1; _sm_au_c=iVV6pjvpDFZ30npN0e; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1524205112,1524554540,1524712710,1524897558; reviewJump=nojump; historystock=000069%7C*%7C002672%7C*%7C601566%7C*%7C000995; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1524908610; v=AkcqqPSM0TpYolW2Sxd1OW1Q1vAUTB-ndS-frxk0YMf5H21kIRyrfoXwL_Uq',
        'searchGuide=sg; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1503478626; __utma=156575163.1936459573.1503289139.1518485846.1518510403.54; __utmz=156575163.1518510403.54.54.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; spversion=20130314; usersurvey=1; _sm_au_c=iVV6pjvpDFZ30npN0e; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1524205112,1524554540,1524712710,1524897558; reviewJump=nojump; historystock=000069%7C*%7C002672%7C*%7C601566%7C*%7C000995; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1524908610; v=AgNudGhYXY78zhF6Z2lpLUnMksyoeJKb0R7b4zXgXPXdYCk4vUgnCuHcazZG'
    ]
    hexin = [
        'Av-SgIzkmdJgmp3Ow6WtYWU4jtiM5FImbTtXcZHMm2Tx1RUMmbTj1n0I58mi',
        'As-iEDzUySKQis1ek2190bUIXmjc9CFKvU4nBuHcaKZBIuWc6cSzZs0Yt17y',
        'AkcqqPSM0TpYolW2SwN1OW1Q1vAUTBgWdSmfrhk0YPb5BW1kIRyrfoXwL_cq',
        'AoLve-EzbLlVNXBlvmb42lBn04PhU4W3OFt6nMybrWGkjii3tOPWfQjnyqef',
        'AkcqqPSM0TpYolW2Sxd1OW1Q1vAUTB-ndS-frxk0YMf5H21kIRyrfoXwL_Uq',
        'AgNudGhYXY78zhF6Z2lpLUnMksyoeJKb0R7b4zXgXPXdYCk4vUgnCuHcazZG'
    ]
    holdid = [
        'T000073058',
        'T000025533',
        '03149165',
        'T000280241',
        'T000025532',
        '00079956'
    ]
    name = [
        '中国证券金融股份有限公司',
        '全国社保基金一零四组合',
        '全国社保基金四零三组合',
        '中央汇金资产管理有限责任公司',
        '全国社保基金一零三组合',
        '全国社保基金一零一组合'
    ]
    collection = [
        chigu_Zhongjin,
        chigu_Shebao104,
        chigu_Shebao403,
        chigu_Huijin,
        chigu_Shebao101,
        chigu_Shebao110
    ]
    s = 0
    for i,j,m,n,c in zip(cookie,hexin,holdid,name,collection):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': i,
            'hexin-v': j,
            'Host': 'basic.10jqka.com.cn',
            'Referer': 'http://basic.10jqka.com.cn/000069/holder.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        params = {
            'holdid': m,
            'code': '000069',
            'type': '0',
            'curcode': '000069',
            'name': n
        }
        html = requests.get(url, params=params, headers=headers)
        json_data = json.loads(html.text)
        stock_list = json_data['stockflash']
        name = ['stock','num']
        test = pd.DataFrame(columns=name,data=stock_list)
        test.to_csv('D:/mongodb/Libao/chigu/update1/%s.csv' % n)
        time.sleep(10)


if __name__ == "__main__":
    url = 'http://basic.10jqka.com.cn/ajax/agencyHoldInfo.php?'
    get_stock_list(url)