"""
@function:
@parameter:
@attention:
"""
from utils import MysqlUtil

def getIp():
    sql = "select id,ip from day_data.IP_POOL"
    read_sql = MysqlUtil.Pymysql().readSql(sql)
    print(read_sql)


getIp()
getIp()