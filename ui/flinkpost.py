"""
@function:
@parameter:
@attention:
"""

import json
import flinkcommitconf
import requests
def flinkpost(params):
    url = flinkcommitconf.POST_URL
    load = params
    req = requests.post(url, json.dumps(load))
    return req.text
