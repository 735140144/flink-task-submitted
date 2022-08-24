"""
@function:
@parameter:
@attention:
"""

from datetime import datetime

import pandas as pd

import common.AshareConfig as AC
import function.write_into_mongo
import utils.MongoUtil
import utils.MysqlUtil
import utils.TuShareApi


class OdsDateLineUpdate:
    def get_Dateline(self, date):
        return utils.TuShareApi.tushare_api.daily(trade_date=date)

    def get_MoneyFlow(self, date):
        return utils.TuShareApi.tushare_api.moneyflow(trade_date=date)

    def get_LimitPrice(self, date):
        return utils.TuShareApi.tushare_api.stk_limit(trade_date=date)

    def get_DailyBasic(self, date):
        return utils.TuShareApi.tushare_api.daily_basic(trade_date=date, fields=[
            "ts_code",
            "trade_date",
            "close",
            "turnover_rate",
            "turnover_rate_f",
            "volume_ratio",
            "pe",
            "pe_ttm",
            "pb",
            "ps",
            "ps_ttm",
            "dv_ratio",
            "dv_ttm",
            "total_share",
            "float_share",
            "free_share",
            "total_mv",
            "circ_mv",
            "limit_status"
        ]).set_index('ts_code', drop=True)

    def get_AdjFactor(self, date):
        return utils.TuShareApi.tushare_api.adj_factor(ts_code='', trade_date=date)

    def merge_all(self, date):
        daily = self.get_Dateline(date)
        limit_price = self.get_LimitPrice(date)
        adjfactor = self.get_AdjFactor(date)
        moneyflow = self.get_MoneyFlow(date)
        daily_basic = self.get_DailyBasic(date)
        list_all = pd.merge(left=daily, right=limit_price, how='left', on='ts_code', suffixes=('', '_DROP'))
        list_all = pd.merge(left=list_all, right=adjfactor, how='left', on='ts_code', suffixes=('', '_DROP'))
        list_all = pd.merge(left=list_all, right=moneyflow, how='left', on='ts_code', suffixes=('', '_DROP'))
        list_all = pd.merge(left=list_all, right=daily_basic, how='left', on='ts_code',
                            suffixes=('', '_DROP')).filter(
            regex='^(?!.*_DROP)')
        return list_all

    def read_list(self):
        ENGINE = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                             AC.TENCENT_DB)
        sql = 'select cal_date from ods_trade_date;'
        df = pd.read_sql(sql, ENGINE)
        sql2 = 'select date from update_record where table_name = \'ods_date_line\';'
        DBDate = pd.read_sql(sql2, ENGINE).iat[0, 0]
        ENGINE.dispose()
        df.drop(df[df['cal_date'] < DBDate].index, inplace=True)
        df.drop(df[df['cal_date'] > today].index, inplace=True)
        return df


today = datetime.now().strftime('%Y%m%d')
if __name__ == "__main__":
    read_list = OdsDateLineUpdate().read_list()
    ListName = "ods_date_line"
    If_Exists = "append"
    Engine = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                         AC.TENCENT_DB)
    for date in read_list.cal_date:
        df = OdsDateLineUpdate().merge_all(date)
        df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
    sql = 'update update_record set date = ' + today + ' where table_name = \'ods_date_line\' ;'
    utils.MysqlUtil.MySqLUtil().update(sql)
