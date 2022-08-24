"""
@function:
@parameter:
@attention:
"""
from datetime import datetime

import akshare as ak
import pandas as pd
import utils.MysqlUtil
import function.write_into_mongo

if __name__ == "__main__":
    Q1 = '0331'
    Q2 = '0630'
    Q3 = '0930'
    Q4 = '0101'
    month_day = datetime.now().strftime('%m%d')
    year = datetime.now().strftime('%Y')
    if month_day < Q1:
        date = year + Q4
    elif month_day < Q2:
        date = year + Q1
    elif month_day < Q3:
        date = year + Q2
    else:
        date = year + Q3
    print(date)
    stock_gdfx_free_holding_detail_em_df = ak.stock_gdfx_free_holding_detail_em(date=date)
    stock_gdfx_free_holding_detail_em_df['报告期'] = pd.to_datetime(stock_gdfx_free_holding_detail_em_df['报告期']).dt.strftime('%Y%m%d')
    stock_gdfx_free_holding_detail_em_df['公告日'] = pd.to_datetime(stock_gdfx_free_holding_detail_em_df['公告日']).dt.strftime('%Y%m%d')
    List_Name = 'ods_free_hold_detail'
    function.write_into_mongo.WirteIntoMongo().WriteIntoMongoWithDeleteAll(stock_gdfx_free_holding_detail_em_df, List_Name)
    sql = 'update update_record set date = %s where table_name = %s;'
    utils.MysqlUtil.MySqLUtil().update(sql, (date, List_Name))
