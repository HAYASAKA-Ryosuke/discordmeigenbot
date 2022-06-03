from urllib import request
import json


def _fetch_exchange(base="USD", to="JPY") -> float:
    post_request = request.Request('https://api.bitfinex.com/v2/calc/fx', json.dumps(dict(ccy1=base, ccy2=to)).encode(), {'Content-Type': 'application/json'})
    response = request.urlopen(post_request)
    content = json.loads(response.read().decode('utf8'))
    return content[0]


def calc_exchange(price: int, base: str, to: str) -> str:
    exchange_value = _fetch_exchange(base, to)

    if exchange_value == -1: return "fetch error"

    return f"{base}: {price:,} → {to}: {round(price * exchange_value):,}"
