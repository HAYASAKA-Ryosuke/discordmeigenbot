import json
import discord


TOKEN = '<TOKEN>'
CHANNELID = 0000000

client = discord.Client()

def fetch_fortune():
    url = "https://meigen.doodlenote.net/api/json.php"
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    if content and len(content) == 1:
       return f"{content[0].get('meigen')} by {content[0].get('auther')}"


@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    if not message.author.bot:
        return
    if not message.content.startswith('$meigen'):
        return

    channel = client.get_channel(CHANNELID)
    response_message = fetch_fortune()
    await channel.send(response_message)
    print(response_message)


client.run(TOKEN)
