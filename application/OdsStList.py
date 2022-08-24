"""
@function:
@parameter:
@attention:
"""
import akshare as ak
import utils.MysqlUtil
from datetime import datetime
import common.AshareConfig as AC
if __name__ == "__main__":
    stock_zh_a_st_em_df = ak.stock_zh_a_st_em()
    ListName = 'ods_st_list'
    date = datetime.now().strftime('%Y%m%d')
    Engine = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    stock_zh_a_st_em_df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    sql = 'update update_record set date = %s where table_name = %s;'
    utils.MysqlUtil.MySqLUtil().update(sql,(date,ListName))