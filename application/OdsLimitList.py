"""
@function:
@parameter:
@attention:
"""

from datetime import datetime

import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
import utils.TuShareApi


class OdsLimitList:
    def get_limitlist(self, date):
        return utils.TuShareApi.tushare_api.limit_list(trade_date=date)


if __name__ == "__main__":
    date = datetime.now().strftime("%Y%m%d")
    df = OdsLimitList().get_limitlist(date)
    ListName = 'ods_limit_list'
    If_Exists = 'append'
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()

    sql = 'update update_record set date = %s where table_name = %s;'
    utils.MysqlUtil.MySqLUtil().update(sql, (date, ListName))
