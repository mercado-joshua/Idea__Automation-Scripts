import urllib
import json
from selenium import webdriver
import time

"""
can be used in stock.. e.g raised by 10%
"""

def look_for_new_video():
    api_key = 'whatever your api key is get it here: https://console.developers.google.com'
    channel_id = 'get the channel id for whatever channel you want to track'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = f'{base_search_url}key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1'
    inp = urllib.urloppen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            driver = webdriver.Firefox()
            driver.get(f'{base_video_url}{vidID}')
            video_exists = True

    if video_exists:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId':vidID}
            json.dump(data, json_file)

try:
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stopping...')