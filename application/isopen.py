"""
@function:
@parameter:
@attention:
"""
import sys

import pandas as pd

import common.AshareConfig as AC
import utils.MysqlUtil
def is_open():
    sql = "select is_open from ods_trade_date where cal_date ='" + sys.argv[1] + "';"
    Engine = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                         AC.TENCENT_DB)
    is_open = pd.read_sql(sql, Engine)
    if len(is_open) == 0:
        is_open = 0
    else:
        is_open = 1
    return is_open


if __name__ == "__main__":
    print(is_open())
