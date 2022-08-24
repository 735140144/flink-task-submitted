"""
@function:
@parameter:
@attention:
"""
from datetime import datetime

import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
import utils.TuShareApi


class OdsSuspendInfo:
    def get_Suspend(self, date):
        return utils.TuShareApi.tushare_api.suspend_d(suspend_type='S', trade_date=date)


if __name__ == "__main__":
    date = datetime.now().strftime('%Y%m%d')
    df = OdsSuspendInfo().get_Suspend(date)
    ListName = 'ods_suspend_info'
    If_Exists = 'replace'
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
    sql = 'update update_record set date = %s where table_name = %s;'
    utils.MysqlUtil.MySqLUtil().update(sql,(date,ListName))
