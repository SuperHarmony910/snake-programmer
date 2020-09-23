# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return 0;

    if 'hello' or 'hi' in message.content.lower():
        await message.channel.send('👋 Hello!')

@client.event
async def on_message(message):
        if 'poop' in message.content.lower():
            await message.channel.send('💩');
        
           
client.run(TOKEN)
