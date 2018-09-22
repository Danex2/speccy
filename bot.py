from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import discord
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print('Running ' + client.user.name + ' ' + client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('!build'):
        req = Request('https://pcpartpicker.com/list/BgK49J',
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

client.run('NDkyODAxMTI3Mzk4NjM3NTY4.DobsfQ.yEeJaWUk75mcLhLnUnI6LAsfIGg')
