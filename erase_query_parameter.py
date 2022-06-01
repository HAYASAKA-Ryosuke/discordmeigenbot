from urllib.parse import urlparse

def erase_query_parameter(url: str):
    parsing_url = urlparse(url)
    return f'[here]({parsing_url.scheme}://{parsing_url.hostname}{parsing_url.path})'