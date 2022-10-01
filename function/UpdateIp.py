"""
@function:
@parameter:
@attention:
"""
from utils import MysqlUtil


def upIpPool(params):
    sql = "insert into day_data.IP_POOL (id,ip) values(%s,%s)"
    MysqlUtil.Pymysql().insertSql(sql, params)
    return
