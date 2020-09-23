# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is currently active on Discord!')


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

        if '!link' in message.content.lower():
            await message.channel.send('https://github.com/SuperHarmony910 Shameless plug!');

@client.event
async def on_message(message):

    if message.content.startswith('!members'):

        for guild in client.guilds:

            for member in guild.members:
                await message.channel.send(member)
           
client.run(TOKEN)
