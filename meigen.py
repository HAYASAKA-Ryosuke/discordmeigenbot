from urllib.request import urlopen
import json


def download_meigen() -> list[dict]:
    url = "https://meigen.doodlenote.net/api/json.php"
    response = urlopen(url)
    return json.loads(response.read().decode('utf8'))


def fetch_meigen():
    meigen = download_meigen()
    if meigen and len(meigen) == 1:
       return f"{meigen[0].get('meigen')} by {meigen[0].get('auther')}"
