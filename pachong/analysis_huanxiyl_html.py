from bs4 import BeautifulSoup
import pymysql

# 连接数据库
my_db = pymysql.connect(host='192.168.2.54', port=3306, user='fatwrite', passwd='fatwrite',
                        db='DEV_GOMANAGER_VEDENG_COM', charset='utf8')
cursor = my_db.cursor()
# 获取要更新字段的数据
query_update_goods_sql = "select GOOD_HTML, GOOD_URL from T_SEO_KEYWORDS_HUANXIYL_GOODS where GOOD_HTML is not null and GOOD_URL NOT LIKE '%/.html%' "

cursor.execute(query_update_goods_sql)
good_list = cursor.fetchall()
html_list = []
for good in good_list:
    good_info = {
        "url": good[1],
        "html": good[0]
    }
    html_list.append(good_info)
# 关闭连接
my_db.close()

# 遍历html
for html_info in html_list:
    # 创建一个BeautifulSoup 对象解析 html
    soup = BeautifulSoup(html_info["html"], "html.parser")

    # 存放解析出来的结果
    good_res = {'url': html_info['url']}

    # 获取第一个 h1 tag 就是 产品名称
    title_list = soup.find_all('h1', limit=1)
    if len(title_list) == 0:
        # 打印没有商品名称的 URL
        print(html_info["url"])
    else:
        good_res['good_name'] = title_list[0].get_text()

    # 获取内容字段
    nei_rong_list = soup.select('.neirong > .fl,.red')
    for nei_rong in nei_rong_list:
        nei_rong_text = str(nei_rong.get_text())
        if "批准文号" in nei_rong_text:
            good_res['good_register_number'] = nei_rong_text
        elif "订货号" in nei_rong_text:
            good_res['sku_no'] = nei_rong_text
        elif "分类编号" in nei_rong_text:
            good_res['category_no'] = nei_rong_text
        elif "型号" in nei_rong_text:
            good_res['good_model'] = nei_rong_text
        elif "科室" in nei_rong_text:
            good_res['department'] = nei_rong_text
        elif "品牌" in nei_rong_text:
            good_res['good_brand'] = nei_rong_text

    #  获取产品描述
    good_desc_tag_list = soup.select('.miaoshu.remen', limit=1)
    for good_desc_tag in good_desc_tag_list:
        good_desc_str = str(good_desc_tag.get_text())
        good_res['good_desc'] = good_desc_str

    # 获取产品分类
    category_tag_list = soup.select('.mianbaoxie .fl a')
    category_count = len(category_tag_list)
    # 因为有三级分类的产品面包屑里数量为 5,所以特殊处理
    # 如有其他情况, 另行处理
    if category_count == 5:
        good_res['first_category_url'] = "https://www.huanxiyl.com" + str(category_tag_list[2]['href'])
        good_res['first_category_name'] = str(category_tag_list[2].get_text())

        good_res['second_category_url'] = "https://www.huanxiyl.com" + str(category_tag_list[3]['href'])
        good_res['second_category_name'] = str(category_tag_list[3].get_text())

        good_res['third_category_url'] = "https://www.huanxiyl.com" + str(category_tag_list[4]['href'])
        good_res['third_category_name'] = str(category_tag_list[4].get_text())

    # 查看最后打印的结果
    print(good_res)

