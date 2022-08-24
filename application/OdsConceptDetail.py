"""
@function:
@parameter:
@attention:
"""
import pandas as pd

import common.AshareConfig as AC
import utils.MysqlUtil as Mysql
import utils.MysqlUtil
import utils.TuShareApi
from tqdm import tqdm
from tenacity import retry, wait_fixed

class OdsConceptDetail:
    @retry(wait=wait_fixed(60))
    def single_concet(self, ts_code):
        df = utils.TuShareApi.tushare_api.concept_detail(ts_code=ts_code)
        df.drop(['concept_name', 'name'], axis=1, inplace=True)
        return df

    def read_list(self):
        ENGINE = utils.MysqlUtil.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD,
                                                             AC.TENCENT_DB)
        sql = 'select ts_code,list_date from ods_code_list;'
        df = pd.read_sql(sql, ENGINE).set_index('ts_code')
        ENGINE.dispose()
        return df



if __name__ == "__main__":
    code_list = OdsConceptDetail().read_list()
    df = pd.DataFrame()
    for ts_code in tqdm(code_list.index):
        df = df.append(OdsConceptDetail().single_concet(ts_code))
    ListName = 'ods_concept_detail'
    If_Exists = 'replace'
    Engine = Mysql.PandasMysql().engine_create(AC.TENCENT_HOST, AC.TENCENT_USER, AC.TENCENT_PSAAWD, AC.TENCENT_DB)
    df.to_sql(name=ListName, con=Engine, if_exists=If_Exists, index=False)
    Engine.dispose()
