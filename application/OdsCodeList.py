"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
import utils.TuShareApi as TuShare
import utils.MysqlUtil as Mysql
import common.AshareConfig as AC


class OdsCodeList:
    def get_code_list(self):
        return TuShare.tushare_api.stock_basic(exchange='', list_status='L',
                                               fields='ts_code,symbol,name,area,industry,market,list_date,is_hs')


if __name__ == "__main__":
    ListName = 'ods_code_list'
    If_Exists = 'replace'
    df = OdsCodeList().get_code_list()
    df = df.drop(df[df['market'] == '北交所'].index).reset_index(drop=True)
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST,AC.TENCENT_USER,AC.TENCENT_PSAAWD,AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()

