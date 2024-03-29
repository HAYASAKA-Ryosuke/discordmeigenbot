import os
import discord
from meigen import fetch_meigen
from weather import fetch_weather
from money_convert import calc_exchange
from erase_query_parameter import erase_query_parameter
from help import get_help_message


DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    print(message)
    if message.author.bot:
        return
 
    channel = client.get_channel(message.channel.id)

    if message.content.startswith('!help'):
        response_message = get_help_message()
        await channel.send(response_message)
        print(response_message)

    if message.content.startswith('!meigen'):
        response_message = fetch_meigen()
        await channel.send(response_message)
        print(response_message)
    
    if message.content.startswith('!weather'):
        response_message = fetch_weather()
        await channel.send(response_message)
        print(response_message)

    if message.content.startswith('!USD'):
        price = int(message.content.split()[1])
        response_message = calc_exchange(price, "USD", "JPY")
        await channel.send(response_message)
        print(response_message)

    if message.content.startswith('!EUR'):
        price = int(message.content.split()[1])
        response_message = calc_exchange(price, "EUR", "JPY")
        await channel.send(response_message)
        print(response_message)

    if message.content.startswith('!URL'):
        url = message.content.split()[1]
        embed = erase_query_parameter(url)
        await channel.send(embed=embed)
        print(response_message)

    if message.content.startswith('!calc'):
        content = message.content.lstrip('!calc ')
        response_message = eval(content)
        await channel.send(response_message)
        print(response_message)


client.run(DISCORD_TOKEN)
