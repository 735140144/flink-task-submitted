"""
@function:
@parameter:
@attention:
"""
import utils.MysqlUtil as Mysql
import common.AshareConfig as AC
import pandas as pd
import sys

def get_date():
    sql = 'select dfs from update_record where table_name = \''+sys.argv[1]+'\';'
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    date = pd.read_sql(sql,Engine)
    return date.iat[0,0]

if __name__ == "__main__":
    print(get_date())