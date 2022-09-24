"""
@function:
@parameter:
@attention:
"""
import json
import random
import re
import time

import pandas as pd
import requests
from kafka import KafkaProducer
from retry import retry

import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
import utils.TuShareApi as TuShare


def kafkaConf():
    bootstrap_servers = ['172.16.0.101:9092', '172.16.0.102:9092', '172.16.0.103:9092']
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda m: json.dumps(m).encode("utf-8"))
    return producer


def sendKafka(topic, value):
    kafkaConf().send(topic, value)
    return


@retry(tries=3)
def getseconddata(topic, proxies):
    first = random.randint(1, 100)
    second = random.randrange(10240652803365012748, 12240652803365012748)
    time_time = int(time.time() * 1000)
    for n in range(1, 4):
        page_url = "http://" + str(first) + ".push2.eastmoney.com/api/qt/clist/get?cb=jQuery" + str(second) + "_" + str(
            time_time) + "&pn=" + str(
            n) + "&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=" + str(
            time_time)
        query = "Query" + str(second) + "_" + str(time_time)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        res = requests.get(page_url, headers=header, proxies=proxies, timeout=10)
        if res.status_code == 200:
            page_content = res.text
            split_ = page_content.split(query)[1].split("(")[1].split(");")[0]
            loads = json.loads(split_)
            loads["time"] = time_time
            print(loads)
            sendKafka(topic, loads)
        else:
            raise Exception("错误")


@retry(tries=3)
def getsecondetf(topic, proxies):
    first = random.randint(1, 100)
    second = random.randrange(10240652803365012748, 12240652803365012748)
    time_time = int(time.time() * 1000)
    page_url = "http://" + str(first) + ".push2.eastmoney.com/api/qt/clist/get?cb=jQuery" + str(second) + "_" + str(
        time_time) + "&pn=1&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=b:MK0021,b:MK0022,b:MK0023,b:MK0024&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=" + str(
        time_time)
    query = "Query" + str(second) + "_" + str(time_time)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    res = requests.get(page_url, headers=header, proxies=proxies, timeout=10)
    if res.status_code == 200:
        page_content = res.text
        split_ = page_content.split(query)[1].split("(")[1].split(");")[0]
        loads = json.loads(split_)
        loads["time"] = time_time
        print(loads)
        sendKafka(topic, loads)
    else:
        raise Exception("错误")

def getbalance():
    page_e = "https://wapi.http.linkudp.com/index/index/get_my_balance?neek=2173527&appkey=5eb7b69a345bd648968f17698b1be2fd"
    get = requests.get(page_e)
    text = get.json()
    return text['data']['balance']


def getip():
    print("获取代理ip")
    page_ip = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    ipurl = requests.get(page_ip)
    json = ipurl.json()
    if json['code'] == 0:
        ip = json['data'][0]['ip'] + ":" + str(json['data'][0]['port'])
        proxies = {
            "http": ip,
            "https": ip
        }
        print("获得ip" + str(proxies))
        return proxies
    elif json['code'] == 113:
        message_ = json['msg']
        print(message_)
        reg = r"([\d]+.[\d]+.[\d]+.[\d]+)"
        search = re.search(reg, message_).group(1)
        writeurl = 'https://wapi.http.linkudp.com/index/index/save_white?neek=2173527&appkey=5eb7b69a345bd648968f17698b1be2fd&white=' + search
        requests.get(writeurl)
        raise Exception("添加白名单")


def getTradeDate(year):
    df = TuShare.tushare_api.trade_cal(xchange='', start_date=str(year) + '0101', end_date=str(year) + '1231')
    ListName = 'open_trade_date'
    If_Exists = 'replace'
    Engine = Mysql.PandasMysql().engine_create(AC.HADOOP102_HOST, AC.HADOOP102_MYSQL_USER,
                                               AC.HADOOP102_MYSQL_PASSWD,
                                               AC.HADOOP102_PORT, AC.HADOOP102_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
    return


def checkDate():
    sql = "select cal_date,is_open from open_trade_date"
    Engine = Mysql.PandasMysql().engine_create(AC.HADOOP102_HOST, AC.HADOOP102_MYSQL_USER,
                                               AC.HADOOP102_MYSQL_PASSWD,
                                               AC.HADOOP102_PORT, AC.HADOOP102_DB)
    df = pd.read_sql(sql, Engine)
    Engine.dispose()
    return df


def check(df, date):
    return df.loc[df['cal_date'] == date].iat[0, 1]
