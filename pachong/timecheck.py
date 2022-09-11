import time
from datetime import datetime

from retry import retry

import getdfcf


# 1.检查是否是交易日,是运行，否sleep 2hour
# 2.检查时间，是否在开盘时间
# 3.检查ip是否有效
# 4.发送信息
@retry()
def geti(topic):
    proxies = getdfcf.getip()
    getdfcf.getTradeDate(time.localtime(time.time()).tm_year)
    df = getdfcf.checkDate()
    while 1 == 1:
        strftime = datetime.now().strftime('%Y%m%d')
        is_open = getdfcf.check(df, strftime)
        if is_open == 1:
            do(topic, proxies)
        else:
            print(1)
            time.sleep(3600)


def do(topic, proxies):
    while 1 == 1:
        try:
            i = int(time.time())
            localtime = time.localtime(i)
            if localtime.tm_hour == 9:
                if localtime.tm_min >= 25:
                    getdfcf.getseconddata(topic, proxies)
                else:
                    time.sleep(1)
            elif localtime.tm_hour == 10:
                getdfcf.getseconddata(topic, proxies)
            elif localtime.tm_hour == 11:
                if localtime.tm_min < 30:
                    getdfcf.getseconddata(topic, proxies)
                else:
                    time.sleep(1)
            elif localtime.tm_hour in (13, 14):
                getdfcf.getseconddata(topic, proxies)
            elif localtime.tm_hour == 15 and localtime.tm_min == 0 and localtime.tm_sec == 0:
                getdfcf.getseconddata(topic, proxies)
            else:
                break
        except:
            raise Exception("错误")
    return


if __name__ == "__main__":
    topic = "second_line"
    geti(topic)
