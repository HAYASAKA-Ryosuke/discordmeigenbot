import urllib
import json


def fetch_fortune():
    url = "https://meigen.doodlenote.net/api/json.php"
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    if content and len(content) == 1:
       return f"{content[0].get('meigen')} by {content[0].get('auther')}"