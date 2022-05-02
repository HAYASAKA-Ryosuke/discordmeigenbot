import os
import discord
from fortune import fetch_fortune
from weather import fetch_weather
from money_convert import calc_exchange


DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
CHANNELID = int(os.environ['CHANNELID'])

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    print(message)
    if message.author.bot:
        return

    channel = client.get_channel(CHANNELID)

    if message.content.startswith('!meigen'):
        response_message = fetch_fortune()
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

    if message.content.startswith('!EURO'):
        price = int(message.content.split()[1])
        response_message = calc_exchange(price, "EURO", "JPY")
        await channel.send(response_message)
        print(response_message)


client.run(DISCORD_TOKEN)
