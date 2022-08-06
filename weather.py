from urllib import request
from datetime import datetime
import json

def get_weather_message(code):
    weatherCodes = {
        100: "☀ 晴",
        101: "☀☁ 晴時々曇",
        102: "☀☂ 晴一時雨",
        103: "☀☂ 晴時々雨",
        104: "☀☃ 晴一時雪",
        105: "☀☃ 晴時々雪",
        106: "☀☂|☃ 晴一時雨か雪",
        107: "☀☂|☃ 晴時々雨か雪",
        108: "☀☂|⛈ 晴一時雨か雷雨",
        110: "☀➡☁ 晴後時々曇",
        111: "☀➡☁ 晴後曇",
        112: "☀➡☂ 晴後一時雨",
        113: "☀➡☂ 晴後時々雨",
        114: "☀➡☂ 晴後雨",
        115: "☀➡☂ 晴後一時雪",
        116: "☀➡☃ 晴後時々雪",
        117: "☀➡☃ 晴後雪",
        118: "☀➡☂|☃ 晴後雨か雪",
        119: "☀➡☂|⛈ 晴後雨か雷雨",
        120: "☀➡☂ 晴朝夕一時雨",
        121: "☀➡☂ 晴朝の内一時雨",
        122: "☀➡☂ 晴夕方一時雨",
        123: "☀➡⛈ 晴山沿い雷雨",
        124: "☀➡☃ 晴山沿い雪",
        125: "☀➡⛈ 晴午後は雷雨",
        126: "☀➡☂ 晴昼頃から雨",
        127: "☀➡☂ 晴夕方から雨",
        128: "☀➡☂ 晴夜は雨",
        130: "🌫➡☀ 朝の内霧後晴",
        131: "☀➡🌫 晴明け方霧",
        132: "☀➡🌫 朝夕曇",
        140: "☀⛈ 晴時々雨で雷を伴う",
        160: "☀☃|☂ 晴一時雪か雨",
        170: "☀☃|☂ 晴時々雪か雨",
        181: "☀➡☃|☂ 晴後雪か雨",
        200: "☁ 曇",
        201: "☁☀ 曇時々晴",
        202: "☁☀ 曇一時雨",
        203: "☁☂ 曇時々雨",
        204: "☁☃ 曇一時雪",
        205: "☁☃ 曇時々雪",
        206: "☁☂|☃ 曇一時雨か雪",
        207: "☁☂|☃ 曇時々雨か雪",
        208: "☁☂|⛈ 曇一時雨か雷雨",
        209: "🌫 霧",
        210: "☁➡☀ 曇後時々晴",
        211: "☁➡☀ 曇後晴",
        212: "☁➡☂ 曇後一時雨",
        213: "☁➡☂ 曇後時々雨",
        214: "☁➡☂ 曇後雨",
        215: "☁➡☃ 曇後一時雪",
        216: "☁➡☃ 曇後時々雪",
        217: "☁➡☃ 曇後雪",
        218: "☁➡☂|☃ 曇後雨か雪",
        219: "☁➡☂|⛈ 曇後雨か雷雨",
        220: "☁☂ 曇朝夕一時雨",
        221: "☁☂ 曇朝の内一時雨",
        222: "☁➡☂ 曇夕方一時雨",
        223: "☁☀ 曇日中時々晴",
        224: "☁➡☂ 曇昼頃から雨",
        225: "☁➡☂ 曇夕方から雨",
        226: "☁➡☂ 曇夜は雨",
        228: "☁➡☃ 曇昼頃から雪",
        229: "☁➡☃ 曇夕方から雪",
        230: "☁➡☃ 曇夜は雪",
        231: "☁🌫|☂ 曇海上海岸は霧か霧雨",
        240: "☁⛈ 曇時々雨で雷を伴う",
        250: "☁☃⛈曇時々雪で雷を伴う",
        260: "☁☃|☂ 曇一時雪か雨",
        270: "☁☃|☂ 曇時々雪か雨",
        281: "☁➡☃|☂ 曇後雪か雨",
        300: "☂ 雨",
        301: "☂☀ 雨時々晴",
        302: "☂☀ 雨時々止む",
        303: "☂☃ 雨時々雪",
        304: "☂|☃雨か雪",
        306: "☂ 大雨",
        308: "☂🌀 雨で暴風を伴う",
        309: "☂☃ 雨一時雪",
        311: "☂☀ 雨後晴",
        313: "☂☁ 雨後曇",
        314: "☂➡☃ 雨後時々雪",
        315: "☂➡☃ 雨後雪",
        316: "☂|☃➡☀ 雨か雪後晴",
        317: "☂|☃➡☁ 雨か雪後曇",
        320: "☂➡☀ 朝の内雨後晴",
        321: "☂➡☁ 朝の内雨後曇",
        322: "☂➡☃ 雨朝晩一時雪",
        323: "☂➡☀ 雨昼頃から晴",
        324: "☂➡☀ 雨夕方から晴",
        325: "☂➡☀ 雨夜は晴",
        326: "☂➡☃ 雨夕方から雪",
        327: "☂➡☃ 雨夜は雪",
        328: "☂ 雨一時強く降る",
        329: "☂☃ 雨一時みぞれ",
        340: "☃|☂ 雪か雨",
        350: "⛈ 雨で雷を伴う",
        361: "☃|☂➡☀ 雪か雨後晴",
        371: "☃|☂➡☁ 雪か雨後曇",
        400: "☃ 雪",
        401: "☃➡☀ 雪時々晴",
        402: "☃☀ 雪時々止む",
        403: "☃☂ 雪時々雨",
        405: "☃ 大雪",
        406: "☃☂ 風雪強い",
        407: "☃🌀 風雪",
        409: "☃☂ 雪一時雨",
        411: "☃➡☀ 雪後晴",
        413: "☃➡☁ 雪後曇",
        414: "☃➡☂ 雪後雨",
        420: "☃➡☀ 朝の内雪後晴",
        421: "☃➡☁ 朝の内雪後曇",
        422: "☃➡☂ 雪昼頃から雨",
        423: "☃➡☂ 雪夕方から雨",
        425: "☃ 雪一時強く降る",
        426: "☃➡☃☂ 雪後みぞれ",
        427: "☃☃☂ 雪一時みぞれ",
        450: "☃⛈ 雪で雷を伴う"}
    return weatherCodes.get(int(code))

def get_temps(content, temp_average_code: str, days: int):
    result = {}

    for area in content[0].get('timeSeries')[2].get('areas'):
        if area.get('area').get('code') == temp_average_code:
            for i, time_define in enumerate(content[0].get('timeSeries')[2].get('timeDefines')):
                if (i % 2 != 0):
                    continue
                time_define = datetime.fromisoformat(time_define).strftime('%m-%d')
                result[time_define] = dict(max=area.get('temps')[i + 1], min=area.get('temps')[i])

    for area in content[1].get('timeSeries')[1].get('areas'):
        if area.get('area').get('code') == temp_average_code:
            for i, time_define in enumerate(content[1].get('timeSeries')[1].get('timeDefines')):
                time_define = datetime.fromisoformat(time_define).strftime('%m-%d')
                if area.get('tempsMax')[i] == '':
                    pass
                else:
                    result[time_define] = dict(max=area.get('tempsMax')[i], min=area.get('tempsMin')[i])
    today = datetime.now().strftime("%m-%d")
    if today not in result.keys():
        for area in content[1].get('tempAverage').get('areas'):
            if (area.get('area').get('code') == temp_average_code):
                result[today] = dict(max=area.get('max'), min=area.get('min'))
    return result


def download_weather_info(path_code):
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{path_code}.json"
    response = request.urlopen(url)
    return json.loads(response.read().decode())


def formatting_weather_info(content, detail_code, name, temp_average_code):
    if content and len(content) >= 1:
        result = ''
        for area in content[0].get('timeSeries')[0].get('areas'):
            if area.get('area').get('code') == detail_code:
                temps = get_temps(content, temp_average_code, len(content[0].get('timeSeries')[0].get('timeDefines')))
                for time_define, weather_code in zip(content[0].get('timeSeries')[0].get('timeDefines'), area.get('weatherCodes')):
                    time_define = datetime.fromisoformat(time_define).strftime('%m-%d')
                    max_temp = temps.get(time_define, dict(max='-', min='-')).get('max')
                    min_temp = temps.get(time_define, dict(max='-', min='-')).get('min')
                    result +=f"{time_define}: {get_weather_message(weather_code)} {min_temp}-{max_temp}℃\n"
        return f"{name}\n{result}"
    return ''


def fetch_weather():
    areas = [
        dict(code="130000", detail_code = "130010", temp_average_code="44132", name="東京"),  # tokyo
        dict(code="016000", detail_code = "016010", temp_average_code="14163", name="札幌(石狩地方)"),  # sapporo
    ]
    result = ''
    for area in areas:
        raw_weather_info = download_weather_info(area['code'])
        result += f"{formatting_weather_info(raw_weather_info, area['detail_code'], area['name'], area['temp_average_code'])}\n"
    return result
