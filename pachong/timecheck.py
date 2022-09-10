import time
from tenacity import retry
from datetime import datetime
import getdfcf


# 1.检查是否是交易日,是运行，否sleep 2hour
# 2.检查时间，是否在开盘时间
# 3.检查ip是否有效
# 4.发送信息
@retry()
def geti(topic):
    proxies = getdfcf.getip()
    while (1 == 1):
        do(topic,proxies)


def do(topic,proxies):
    try:
        strftime = datetime.now().strftime('%Y%m%d')
        i = int(time.time())
        localtime = time.localtime(i)
        if (localtime.tm_hour == 9):
            if (localtime.tm_min >= 25):
                getdfcf.getseconddata(topic,proxies)
            else:
                time.sleep(1)
        elif (localtime.tm_hour == 10):
            getdfcf.getseconddata(topic,proxies)
        elif (localtime.tm_hour == 11):
            if (localtime.tm_min < 30):
                getdfcf.getseconddata(topic,proxies)
            else:
                time.sleep(1)
        elif (localtime.tm_hour in (13, 14)):
            getdfcf.getseconddata(topic,proxies)
        else:
            time.sleep(1)
    except:
        raise Exception("错误")
    return




if __name__=="__main__":
    topic = "second_line_test"
    geti(topic)
