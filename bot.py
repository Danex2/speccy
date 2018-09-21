from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import discord
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print('Running ' + client.user.name)


@client.event
async def on_message(message):
    if message.content.startswith('~build'):
        req = Request('https://pcpartpicker.com/list/BgK49J',
                      headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        content = url.read()
        soup = BeautifulSoup(content, "html.parser")
        i = soup.findAll("td", {'class': ["component-type", "component-name"]})
        output = []
        for c in i:
            output.append(c.get_text().strip('\n'))
        print(", ".join(output))
client.run('NDkyODAxMTI3Mzk4NjM3NTY4.DobsfQ.yEeJaWUk75mcLhLnUnI6LAsfIGg')
