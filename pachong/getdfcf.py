"""
@function:
@parameter:
@attention:
"""
import json
import random
import time
import requests
from kafka import KafkaProducer

bootstrap_servers = ['172.16.0.101:9092', '172.16.0.102:9092', '172.16.0.103:9092']
topic = 'daily_test'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,value_serializer=lambda m: json.dumps(m).encode("utf-8"))
first = random.randint(1, 100)
second = random.randrange(10240652803365012748, 12240652803365012748)
time_time = int(time.time() * 1000)
page_url = "http://" + str(first) + ".push2.eastmoney.com/api/qt/clist/get?cb=jQuery" + str(second) + "_" + str(
    time_time) + "&pn=1&pz=6000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=" + str(
    time_time)
query = "Query" + str(second) + "_" + str(time_time)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#
res = requests.get(page_url, headers=header, timeout=10)
if res.status_code == 200:
    page_content = res.text
    split_ = page_content.split(query)[1].split("(")[1].split(");")[0]
    diff_ = json.loads(split_)['data']['diff']
    for n in range(0, len(diff_)):
        print(diff_[n])
        producer.send(topic,diff_[0])

    producer.close()

        # df.insert(diff_[n])
    # print(df)
