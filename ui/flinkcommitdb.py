"""
@function:
@parameter:
@attention:
"""
import pymysql
import flinkcommitconf as conf

class FLINKCOMMITDB:
    def __init__(self):
        self.db = pymysql.connect(host=conf.ALI_HOST,
                                  user=conf.ALI_USER,
                                  port=conf.ALI_PORT,
                                  password=conf.ALI_PASSWD,
                                  db=conf.Ali_DB,
                                  charset='utf8')

    def readSql(self, sql, params=None):
        connect = self.db
        cur = connect.cursor()
        cur.execute(sql, params)
        fetchall = cur.fetchall()
        cur.close()
        connect.close()
        return fetchall

    def insertSql(self, sql, params=None):
        connect = self.db
        cur = connect.cursor()
        cur.execute(sql, params)
        cur.close()
        connect.close()
        return

    def getjars(self):
        sql = "select distinct(jar) from flink_job"
        return self.readSql(sql)

    def getClass(self,jar):
        sql = "select class from flink_job where jar='" + jar + "'"
        return self.readSql(sql)

    def getAllName(self,jar, classentry):
        sql = "select appname,ckname from flink_job where jar='" + jar + "' and class='" + classentry + "'"
        return self.readSql(sql)