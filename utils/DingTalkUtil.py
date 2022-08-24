"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
from dingtalkchatbot.chatbot import DingtalkChatbot

def sendtext(msg):
    """
    @function:钉钉推送
    @parameter:msg=str
    @attention:
    """
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f0259ce18fe6a1ee1acdf581474d438410aeb71eefdd757e858ff52bfcc4174b'
    secret = 'SEC19b04da6063c98cc51f849816a389237423ecd8908545a666ea1cb63957a1c2b'
    xiaoding = DingtalkChatbot(webhook, secret=secret)
    xiaoding.send_text(str(msg), is_at_all=False)