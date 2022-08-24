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
    def getTradeDate(self):
        year = datetime.now().strftime('%Y')
        return TuShare.tushare_api.trade_cal(xchange='', start_date=year + '0101', end_date=year + '1231', is_open='1')


if __name__ == "__main__":
    ListName = 'ods_trade_date'
    If_Exists = 'append'
    df = OdsTradeDate().getTradeDate()
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
    date = datetime.now().strftime('%Y%m%d')
    sql = 'update update_record set date = %s where table_name = %s;'
    Mysql.MySqLUtil().update(sql, (date, ListName))
