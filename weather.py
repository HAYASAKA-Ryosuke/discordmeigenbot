from urllib import request
import json

def fetch_weather():
    path_code = "130000" # tokyo
    area_detail_code = "130010" # tokyo
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{path_code}.json"
    response = request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    if content and len(content) >= 1:
       result = ''
       for area in content[0].get('timeSeries')[0].get('areas'):
           if area.get('area').get('code') == area_detail_code:
               for time_define, weather in zip(content[0].get('timeSeries')[0].get('timeDefines'), area.get('weathers')):
                   result +=f"{time_define}: {weather}\n"
       return f"東京の天気\n{result}"
    return ''