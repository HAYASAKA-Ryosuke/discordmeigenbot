import urllib

def erase_query_parameter(url: str):
    parsing_url = urllib.parse.urlparse(url)
    return f'[here]({parsing_url.scheme}//{parsing_url.hostname}{parsing_url.path})'