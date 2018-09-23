from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import discord
import asyncio
from datetime import date
import json
<<<<<<< HEAD
import sqlite3
=======
>>>>>>> d4a26fcb5c962c7ef9c93caccdef4b74d90c5966

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS builds (name integer, buildLink text)''')
client = discord.Client()


@client.event
async def on_ready():
<<<<<<< HEAD
    await client.change_presence(game=discord.Game(name='Beep boop!'))
    print('Started ' + client.user.name + ' on ' + str
          (date.today()))
=======
    print('Started ' + client.user.name + ' on ' + str
          (date.today()))

>>>>>>> d4a26fcb5c962c7ef9c93caccdef4b74d90c5966

'''check if user is in db
    if user exists let them know
    if not add build to db'''
@client.event
async def on_message(message):
    if message.content.startswith('!build'):
        user_url = message.content[7:]
<<<<<<< HEAD
        '''req = Request(user_url,
=======
        req = Request(user_url,
>>>>>>> d4a26fcb5c962c7ef9c93caccdef4b74d90c5966
                      headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        content = url.read()
        embed = discord.Embed(title="", color=0xcc1df1)
        soup = BeautifulSoup(content, "html.parser")
        i = soup.findAll("td", {'class': ["component-type", "component-name"]})
        output = []
        for x in i:
            output.append(x.get_text().strip("\n"))
        embed.add_field(name=message.author, value='\n'.join(output))
        await client.send_message(message.channel, embed=embed)'''
        c.execute("INSERT INTO builds (name,buildLink) VALUES (?,?)", (message.author.id, user_url))
        conn.commit()
        conn.close()

with open('token.json', 'r') as t:
    data = json.load(t)

<<<<<<< HEAD
=======
with open('token.json', 'r') as t:
    data = json.load(t)

>>>>>>> d4a26fcb5c962c7ef9c93caccdef4b74d90c5966
client.run(data["token"])
