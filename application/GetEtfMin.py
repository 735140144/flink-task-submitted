"""
@function:
@parameter:
@attention:
"""

import time
from datetime import datetime
from retry import retry
from pachong import getdfcf


# 1.检查是否是交易日,是运行，否sleep 2hour
# 2.检查时间，是否在开盘时间
# 3.检查ip是否有效
# 4.发送信息
@retry()
def getetfmin(topic):
    proxies = getdfcf.getip()
    print(datetime.now().strftime('%Y%m%d'))
    getdfcf.getTradeDate(time.localtime(time.time()).tm_year)
    df = getdfcf.checkDate()
    while True:
        strftime = datetime.now().strftime('%Y%m%d')
        is_open = getdfcf.check(df, strftime)
        if is_open == 1:
            do(topic, proxies)
        else:
            print("非交易时间")
            time.sleep(3600)


def do(topic, proxies):
    while True:
        try:
            i = int(time.time())
            localtime = time.localtime(i)
            if localtime.tm_hour == 9:
                if localtime.tm_min >= 25:
                    getdfcf.getsecondetf(topic, proxies)
                    time.sleep(60)
                else:
                    time.sleep(1)
            elif localtime.tm_hour == 10:
                getdfcf.getsecondetf(topic, proxies)
                time.sleep(60)
            elif localtime.tm_hour == 11:
                if localtime.tm_min < 30:
                    getdfcf.getsecondetf(topic, proxies)
                    time.sleep(60)
                else:
                    time.sleep(1)
            elif localtime.tm_hour in (13, 14):
                getdfcf.getsecondetf(topic, proxies)
                time.sleep(60)
            elif localtime.tm_hour == 15 and localtime.tm_min == 0 and localtime.tm_sec == 0:
                getdfcf.getsecondetf(topic, proxies)
                time.sleep(60)
            else:
                time.sleep(60)
                break
        except:
            raise Exception("错误")
    return


if __name__ == "__main__":
    topic = "etf_min_line"
    getetfmin(topic)
