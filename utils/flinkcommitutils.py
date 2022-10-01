"""
@function:
@parameter:
@attention:
"""
from utils.MysqlUtil import LuckyConfDB as db


def getjars():
    sql = "select distinct(jar) from flink_job"
    return db().readSql(sql)

def getClass(jar):
    sql = "select class from flink_job where jar='"+jar+"'"
    return db().readSql(sql)
