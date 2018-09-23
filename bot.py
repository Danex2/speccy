from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import discord
import asyncio
from datetime import date
import json


client = discord.Client()


@client.event
async def on_ready():
    print('Started ' + client.user.name + ' on ' + str
          (date.today()))


@client.event
async def on_message(message):
    if message.content.startswith('!build'):
        user_url = message.content[7:]
        req = Request(user_url,
                      headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        content = url.read()
        embed = discord.Embed(title="", color=0xcc1df1)
        soup = BeautifulSoup(content, "html.parser")
        i = soup.findAll("td", {'class': ["component-type", "component-name"]})
        output = []
        for x in i:
            output.append(x.get_text().strip("\n"))
        embed.add_field(name="Dane's build", value='\n'.join(output))
        await client.send_message(message.channel, embed=embed)

with open('token.json', 'r') as t:
    data = json.load(t)

client.run(data["token"])
