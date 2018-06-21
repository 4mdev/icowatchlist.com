# 4mDev
# icowatchlist.com API
# https://api.icowatchlist.com/public/v1/

import json
import requests as r

def get_IWL_data(url):
    try:
        events = r.post(url)
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result

def get_IWL_live_ico():
    return get_IWL_data("https://api.icowatchlist.com/public/v1/live")['ico']['live']

def get_IWL_upcoming_ico():
    return get_IWL_data("https://api.icowatchlist.com/public/v1/upcoming")['ico']['upcoming']

def get_IWL_finished_ico():
    return get_IWL_data("https://api.icowatchlist.com/public/v1/finished")['ico']['finished']

