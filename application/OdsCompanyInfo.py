"""
@function:
@parameter:
@attention:
"""

import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
import utils.TuShareApi


class OdsCompanyInfo:
    def get_Company_Info(self, exchange):
        return utils.TuShareApi.tushare_api.stock_company(exchange=exchange,
                                                          fields='ts_code,chairman,manager,secretary,'
                                                                 'reg_capital,setup_date,'
                                                                 'province,city,introduction,website,email,'
                                                                 'office,employees,main_business')


if __name__ == "__main__":
    ListName = 'ods_company_info'
    SSE = 'SSE'
    SZSE = 'SZSE'
    df_SZ = OdsCompanyInfo().get_Company_Info(SZSE)
    df_SE = OdsCompanyInfo().get_Company_Info(SSE)
    df = df_SZ.append(df_SE)
    If_Exists = 'replace'
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
