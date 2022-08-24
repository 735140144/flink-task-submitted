"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from tqdm import tqdm
import pandas as pd
def MultiThreading(function, table):
    """
    @function:多线程计算
    @parameter:function=方法 table=表名.列名
    @attention:table.index or table.columns
    """
    executor = ThreadPoolExecutor()
    all_task = [executor.submit(function, i) for i in table]
    for future in tqdm(as_completed(all_task), total=len(table), desc='当前进度'):
        future.result()


def MultipleProcesses(function, table):
    """
    @function:多进程计算
    @parameter:function=方法 table=表名.列名
    @attention:table.index or table.columns
    """
    df = pd.DataFrame()
    executor = ProcessPoolExecutor()
    all_task = [executor.submit(function, i) for i in table]

    for future in tqdm(as_completed(all_task), total=len(table), desc='当前进度'):
        df = df.append(future.result()).reset_index(drop=True)
    return df