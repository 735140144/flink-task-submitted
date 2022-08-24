"""
@function:
@parameter:
@attention:
"""
import utils.TuShareApi
import utils.MysqlUtil
import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
from datetime import datetime

if __name__ =="__main__":
    df = utils.TuShareApi.tushare_api.concept(src='ts')
    ListName = 'ods_concept_info'
    date = datetime.now().strftime('%Y%m%d')
    If_Exists = 'replace'
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
    sql = 'update update_record set date = %s where table_name = %s;'
    utils.MysqlUtil.MySqLUtil().update(sql,(date,ListName))
