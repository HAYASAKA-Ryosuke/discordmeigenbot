from urllib.parse import urlparse
import discord 

def erase_query_parameter(url: str):
    embed = discord.Embed()
    parsing_url = urlparse(url)
    erased_query_param_url = f'{parsing_url.scheme}://{parsing_url.hostname}{parsing_url.path}'
    embed.add_field(name=erased_query_param_url, url=erased_query_param_url)
    return embed