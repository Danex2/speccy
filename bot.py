from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import discord
import asyncio
from datetime import date
import json
import sqlite3
from PCPartPicker_API import pcpartpicker
import time
import urllib.error




conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS builds (name integer, buildLink text)''')
client = discord.Client()

parts = {'cpu': 'cpu','cooler': 'cpu-cooler', 'mb': 'motherboard', 'ram': 'memory', 
'hdd': 'internal-hard-drive', 'gpu': 'video-card', 'psu': 'power-supply', 'case': 'case', 
'monitor': 'monitor', 'keyboard': 'keyboard', 'mouse': 'mouse'}


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Beep boop!'))
    print('Started ' + client.user.name + ' on ' + str
          (date.today()))


@client.event
async def on_message(message):
    user_url = message.content[7:]
    if message.content.startswith('!build'):
        #check if user is in db first
        c.execute("SELECT * FROM builds WHERE name=?", (message.author.id, ))
        user_build = c.fetchall()
        if user_build:
           'await client.send_message(message.channel, "You already have a build added.")'
           c.execute("SELECT * FROM builds WHERE name=?", (message.author.id, ))
           r = c.fetchone()
           req = Request(r[1], headers={'User-Agent': 'Mozilla/5.0'})
           url = urlopen(req)
           content = url.read()
           embed = discord.Embed(title="", color=0xcc1df1)
           soup = BeautifulSoup(content, "html.parser")
           i = soup.findAll("td", {'class': ["component-type", "component-name"]})
           output = []
           for x in i:
                output.append(x.get_text().strip("\n"))
           embed.add_field(name='Your pc build', value='\n'.join(output))
           await client.send_message(message.channel, embed=embed)
        elif not user_build and not user_url:
            await client.send_message(message.channel, "No build found for user. ```Usage: !build [pcpartpicker link]```")
        elif not user_build and user_url:
            c.execute("INSERT INTO builds (name, buildLink) VALUES (?,?)", (message.author.id, user_url))
            await client.send_message(message.channel, "Build saved.")
            conn.commit()
    elif message.content.startswith('!remove'):
       #remove their link
        c.execute("SELECT * FROM builds WHERE name=?", (message.author.id, ))
        user_build = c.fetchall()
        if not user_build:
            await client.send_message(message.channel, "No build to remove, please add one first.")
        else:
            c.execute('DELETE FROM builds WHERE name =?', (message.author.id, ))
            conn.commit()
            await client.send_message(message.channel, "Build removed.")
    elif message.content.startswith('!price'):
        embed = discord.Embed(title="", color=0xcc1df1)
        args = message.content.split(" ")
        if len(args) < 3:
            await client.send_message(message.channel, "```Usage: !price [region] [component] [search term]```")
        else:
            try:
                region = args[1]
                item = args[3:]
                part = args[2]
                pcpartpicker.set_region(region)
                component = pcpartpicker.lists.get_list(parts.get(part))
                part_dict = {}
                for pc_item in component:
                    """fix the searching thing"""
                    if "".join(item).lower() in pc_item['name'].lower() and pc_item["price"] != "":
                        part_dict[pc_item['name']] = pc_item["price"]
                embed.add_field(name='Part List', value=str(part_dict).strip('{}').replace(",","\n").replace("'", ""))
                await client.send_message(message.channel, embed=embed)
            except urllib.error.HTTPError as e:
                if e.code == 400:
                    await client.send_message(message.channel, "Returned too many results, try typing the exact part name or more parts of it.")

           


with open('token.json', 'r') as t:
    data = json.load(t)

client.run(data["token"])
