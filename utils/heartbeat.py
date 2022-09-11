"""
@function:
@parameter:
@attention:
"""
from datetime import datetime
import utils.MysqlUtil as Mysql

def heartbeat(jobname):
    strftime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "insert into day_data.JOB_HEART values(%s,%s)"
    Mysql.MySqLUtil().selectone(sql,(jobname,strftime))