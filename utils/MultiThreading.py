"""
@function:
@parameter:
@attention:
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from tqdm import tqdm

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
