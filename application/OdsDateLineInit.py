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


class OdsDateLineInit:
    def get_Dateline(self, ts_code, start_date, end_date):
        return utils.TuShareApi.tushare_api.daily(ts_code=ts_code, start_date=start_date,
                                                  end_date=end_date)

    def get_MoneyFlow(self, ts_code, start_date, end_date):
        return utils.TuShareApi.tushare_api.moneyflow(ts_code=ts_code, start_date=start_date, end_date=end_date)

    def get_LimitPrice(self, ts_code, start_date, end_date):
        return utils.TuShareApi.tushare_api.stk_limit(ts_code=ts_code, start_date=start_date, end_date=end_date)

    def get_DailyBasic(self, ts_code, start_date, end_date):
        return utils.TuShareApi.tushare_api.daily_basic(ts_code=ts_code, start_date=start_date, end_date=end_date,
                                                        fields=[
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
                                                        ])

    def get_AdjFactor(self, ts_code):
        return utils.TuShareApi.tushare_api.adj_factor(ts_code=ts_code, trade_date='')

    def merge_all(self, ts_code, start_date, end_date):
        daily = self.get_Dateline(ts_code, start_date, end_date)
        limit_price = self.get_LimitPrice(ts_code, start_date, end_date)
        adjfactor = self.get_AdjFactor(ts_code)
        moneyflow = self.get_MoneyFlow(ts_code, start_date, end_date)
        daily_basic = self.get_DailyBasic(ts_code, start_date, end_date)
        list_all = pd.merge(left=daily, right=limit_price, how='left', on='trade_date', suffixes=('', '_DROP'))
        list_all = pd.merge(left=list_all, right=adjfactor, how='left', on='trade_date', suffixes=('', '_DROP'))
        list_all = pd.merge(left=list_all, right=moneyflow, how='left', on='trade_date', suffixes=('', '_DROP'))
        list_all = pd.merge(left=list_all, right=daily_basic, how='left', on='trade_date',
                            suffixes=('', '_DROP')).filter(
            regex='^(?!.*_DROP)')
        return list_all

    def read_list(self):
        ENGINE = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                             AC.TENCENT_DB)
        sql = 'select ts_code,list_date from ods_code_list;'
        df = pd.read_sql(sql, ENGINE).set_index('ts_code')
        ENGINE.dispose()
        return df



if __name__ == "__main__":
    codelist = OdsDateLineInit().read_list()
    end_date = datetime.now().strftime('%Y%m%d')
    ListName = "ods_date_line"
    If_Exists = "append"
    Engine = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                         AC.TENCENT_DB)
    for ts_code in codelist.index:
        start_date = codelist.loc[ts_code]['list_date']
        df = OdsDateLineInit().merge_all(ts_code, start_date, end_date)
        try:
            df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
        except:
            Engine = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                                 AC.TENCENT_DB)
            df = OdsDateLineInit().merge_all(ts_code, start_date, end_date)
    Engine.dispose()
    sql='update update_record set date = '+end_date+' where table_name = \'ods_date_line\' ;'
    utils.MysqlUtil.MySqLUtil().update(sql)
