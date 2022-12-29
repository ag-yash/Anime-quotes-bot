import discord
import os
import requests
import json
from dotenv import load_dotenv


url = "https://animechan.vercel.app/api/random"

response = requests.request("GET", url)
res = json.loads(response.text)
quote = res["quote"]



intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        response = requests.request("GET", url)
        res = json.loads(response.text)
        character = res["character"]
        anime = res["anime"]
        quote = res["quote"]
        await message.channel.send(f'"{quote}"\n -{character} ({anime})')

load_dotenv()
client.run(os.getenv('TOKEN'))