"""
@function:
@parameter:
@attention:
"""
import utils.MysqlUtil as Mysql
import sys

if __name__ =="__main__":
    sql = 'update update_record set dfs = %s where table_name = %s;'
    Mysql.MySqLUtil().update(sql, (sys.argv[1], sys.argv[2]))
