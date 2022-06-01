from urllib.parse import urlparse
import discord 

def erase_query_parameter(url: str):
    embed = discord.Embed()
    parsing_url = urlparse(url)
    erased_query_param_url = f'[here erase query param URL]({parsing_url.scheme}://{parsing_url.hostname}{parsing_url.path})'
    # embed.add_field(name='here erase query param URL', value=erased_query_param_url)
    embed.url = erased_query_param_url
    return embed