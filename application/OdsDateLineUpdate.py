"""
@function:
@parameter:
@attention:
"""

from datetime import datetime

import pandas as pd

import utils.KafkaUtil as kf
from utils import heartbeat
import utils.MongoUtil
import utils.MysqlUtil
import utils.TuShareApi
import utils.MysqlUtil as mysql
from pachong import getdfcf


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



date = getdfcf.checkDate()
sql = "select max(trade_date) from day_data.DAY_DATA_LINE"
selectone = int(mysql.MySqLUtil().selectone(sql)[0])
end_date = datetime.now().strftime('%Y%m%d')
undefday = date[(date['cal_date'] > str(selectone)) & (date['cal_date'] <= end_date)]
for i in undefday['cal_date']:
    is_open = getdfcf.check(date, i)
    if is_open == 1 :
        df = OdsDateLineUpdate().merge_all(i)
        topic = "ods_date_line"
        json = df.to_json(orient='records')
        kf.sendKafka(topic, json)
        heartbeat.heartbeat("OdsDateLineInit")

