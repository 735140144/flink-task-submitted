import time
from tenacity import retry

@retry()
def geti(n=0):
    n=n+1
    print(n)
    do()


def do():
    i = int(time.time())
    localtime = time.localtime(i)
    if(localtime.tm_hour==9):
        if(localtime.tm_min>=25):
            print(i)
        else:
            print(1)
            time.sleep(1)
    elif(localtime.tm_hour==10):
        print(i)
    elif(localtime.tm_hour==11):
        if(localtime.tm_min<30):
            print(i)
        else:
            print(2)
            time.sleep(1)
    elif(localtime.tm_hour in (13,14)):
        print(i)
    else:
        print(3)
        time.sleep(1)
        raise Exception("cuowu")
    return

while(1==1):
    geti()