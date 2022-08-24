"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
import tushare as ts
import common.AshareConfig

tushare_api = ts.pro_api(common.AshareConfig.API.TUSHARE_TOKEN)
tushare_set = ts.set_token(common.AshareConfig.API.TUSHARE_TOKEN)
