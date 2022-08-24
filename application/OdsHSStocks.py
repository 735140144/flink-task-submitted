"""
@function:
@parameter:
@attention:
"""
import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
import utils.TuShareApi


class OdsHSStocks:
    def get_SH_Stocks(self):
        return utils.TuShareApi.tushare_api.hs_const(hs_type='SH')

    def get_SZ_Stocks(self):
        return utils.TuShareApi.tushare_api.hs_const(hs_type='SZ')


if __name__ == "__main__":
    ListName_SH = 'ods_hssh_stocks'
    If_Exists_SH = 'replace'
    ListName_SZ = 'ods_hssz_stocks'
    If_Exists_SZ = 'replace'
    df_SH = OdsHSStocks().get_SH_Stocks()
    df_SZ = OdsHSStocks().get_SZ_Stocks()
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df_SH.to_sql(name=ListName_SH, con=Engine, if_exists=If_Exists_SH, index=False)
    df_SZ.to_sql(name=ListName_SZ, con=Engine, if_exists=If_Exists_SZ, index=False)
    Engine.dispose()
