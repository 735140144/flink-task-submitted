import requests
import pymysql
import time
import datetime
import re
from bs4 import BeautifulSoup

proxies = {
    'https': '113.133.18.22:4253'
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

time_out_cnt = 0


def good_list_3618_spider():
    # 连接数据库
    my_db = pymysql.connect(host='192.168.2.54', port=3306, user='fatwrite', passwd='fatwrite',
                            db='DEV_GOMANAGER_VEDENG_COM', charset='utf8')
    cursor = my_db.cursor()
    query_update_goods_sql = "SELECT GOOD_URL FROM T_PRODUCTS_3618"
    cursor.execute(query_update_goods_sql)
    good_list = cursor.fetchall()
    goods_set = set()
    for good in good_list:
        goods_set.add(good[0])
    # my_db.close()

    total_page = 4048
    start_page = int(get_page_num()) + 1
    pre = 'https://www.3618med.com'
    # for i in range(start_page, total_page + 1):
    spider_page_list = get_no_spider_page()
    for i in spider_page_list:
        time.sleep(1)
        print("开始爬取第 " + str(i) + " 页")
        page_url = "https://www.3618med.com/product/p" + str(i) + ".html"
        try:
            res = requests.get(page_url, headers=header, proxies=proxies, timeout=10)
            good_list = []
            if res.status_code == 200:
                page_content = res.text
                page_soup = BeautifulSoup(page_content, "html.parser")
                product_page_list = page_soup.select('.tia_l_list > li')
                for product in product_page_list:
                    good_info = {}
                    good_title_tag = product.contents[1]
                    good_info['good_url'] = pre + good_title_tag.contents[0]['href']
                    good_info['good_simple_html'] = str(product)
                    good_list.append(good_info)
                print("本页共有 " + str(len(product_page_list)) + " 条数据")
                for g in good_list:
                    if g['good_url'] not in goods_set:
                        sql = "INSERT INTO T_PRODUCTS_3618(GOOD_URL, GOOD_SIMPLE_HTML) " \
                              "VALUES (%s, %s)"
                        try:
                            par = (g['good_url'], g['good_simple_html'])
                            cursor.execute(sql, par)
                            my_db.commit()
                            goods_set.add(g['good_url'])
                        except Exception as e:
                            my_db.rollback()
                            print("保存失败")
                            print(e)

                wf = open(r'D:/py-project/py-spider/3618med/processing.csv', 'a+', encoding="utf-8")
                wf.write('%s\n' % str(i))
                wf.close()
            else:
                print("请求失败 状态码为:" + str(res.status_code))
        except Exception as pe:
            global time_out_cnt
            if "由于目标计算机积极拒绝" in str(pe) or "Authorized failed" in str(pe):
                print("代理失效")
                print(pe)
                update_proxy()
                time_out_cnt = 0
                continue
            else:
                print(pe)
                if time_out_cnt >= 4:
                    print("一直超时 更新IP")
                    update_proxy()
                    time_out_cnt = 0
                else:
                    print("访问频繁, sleep 控制一下")
                    time.sleep(3)
                    time_out_cnt = time_out_cnt + 1
                continue
    my_db.close()


def get_page_num():
    with open(r'D:/py-project/py-spider/3618med/processing.csv', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines[-1]


proxy_time = datetime.datetime.now()

ip_error_count = 0


def update_proxy():
    global ip_error_count
    try:
        resp = requests.get(
            "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=0&sb=0&pb=4&mr=1&regions=")
        ip = resp.text
        global proxy_time
        old_proxy_time = proxy_time
        update_proxy_time = datetime.datetime.now()
        print("更新代理, 新ip为:" + str(ip) + "更新时间为:" + str(update_proxy_time))
        print("原ip:" + proxies['https'] + " 存活时间为: " + str((update_proxy_time - old_proxy_time).seconds) + "秒")
        proxy_time = update_proxy_time
        if re.match(r'(?:(?:25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', ip) is None:
            exit("IP 不正确")
        # proxies['http'] = ip
        proxies['https'] = ip
    except Exception as e:
        print(e)
        print("ip 获取失败")
        ip_error_count = ip_error_count + 1
        if ip_error_count <= 5:
            time.sleep(10)
            update_proxy()


def get_no_spider_page():
    res = []

    already_set = set()
    with open(r'D:/py-project/py-spider/3618med/processing.csv', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines()]
        for li in lines:
            already_set.add(li)
    for i in range(1, 4049):
        if str(i) not in already_set:
            res.append(str(i))
    return res


if __name__ == '__main__':
    # update_proxy()
    good_list_3618_spider()
    # get_page_num()
    # print(get_no_spider_page())
    # print(len(get_no_spider_page()))
