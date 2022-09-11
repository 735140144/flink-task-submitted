"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
import utils.TuShareApi as TuShare
import utils.MysqlUtil as Mysql
import common.AshareConfig as AC
from datetime import datetime


class OdsTradeDate:
    def getTradeDate(self,year):
        TuShare.tushare_api.trade_cal(xchange='', start_date=str(year) + '0101', end_date=str(year) + '1231', is_open='1')
        ListName = 'open_trade_date'
        If_Exists = 'append'
        Engine = Mysql.PandasMysql().engine_create(AC.HADOOP102_HOST, AC.HADOOP102_MYSQL_USER,
                                                   AC.HADOOP102_MYSQL_PASSWD,
                                                   AC.HADOOP102_POST, AC.HADOOP102_DB)
        # for year in range(2000,2030):
        year = '2023'
        df = OdsTradeDate().getTradeDate(year)
        df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
        Engine.dispose()


if __name__ == "__main__":
    ListName = 'open_trade_date'
    If_Exists = 'append'
    Engine = Mysql.PandasMysql().engine_create(AC.HADOOP102_HOST, AC.HADOOP102_MYSQL_USER, AC.HADOOP102_MYSQL_PASSWD,
                                               AC.HADOOP102_POST, AC.HADOOP102_DB)
    # for year in range(2000,2030):
    year = '2023'
    df = OdsTradeDate().getTradeDate(year)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
    date = datetime.now().strftime('%Y%m%d')
