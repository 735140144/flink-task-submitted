"""
@function:
@parameter:
@attention:
"""
import requests


def main(token, num):
    for i in range(1, num + 1):
        headers = {
            "t": token,
            # 小朱token
            # "t": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQyNjA2MjIsIm5iZiI6MTY2MzE1ODQyMiwiaWF0IjoxNjYzMTU2NjIyLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjozNjkyNDczOSwiZGVidWciOiIiLCJsYW5nIjoiIn0.6zNE0DdLo1nd3No-5-pUlXd8G2Z69ewyeoHRAiUFkAg",
            "content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c29) NetType/WIFI Language/zh_CN",
            "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/20/page-frame.html",
            "Host": "cat-match.easygame2021.com",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip,compress,br,deflate-alive"
        }

        url = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=14&rank_role=1&skin=1"
        response = requests.get(url, headers)
        print(response.status_code)
        print("已过关" + str(i) + "次")
    return str(num) + "次已完成"
