"""
@function:
@parameter:
@attention:
"""
import utils.tusharepost as tsapi

params={
        "api_name":'daily',
        "ts_code": '000002.SZ',
        "start_date":'20220101',
        "end_date":'20220911'
    }

def getDateLineInit(params):
    #dataline
    print(tsapi.tusharepost(params))
    #moneyflow

    #daulybasic

    #adjFactor

getDateLineInit(params)