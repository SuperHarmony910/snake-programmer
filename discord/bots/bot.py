# bot.py
import os
import random


from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client();

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!');


@client.event
async def on_message(message):
        if message.author == client.user:
           return;

        if message.content.startswith('hello' or 'hi'):
            await message.channel.send('Hello 👋 ');

@client.event
async def on_message(message):
        if message.author == client.user:
           return

        if message.content.startswith('poop'):
            await message.channel.send('💩');

        if '!link' in message.content.lower():
            await message.channel.send('https://github.com/SuperHarmony910 Shameless plug!');

        if message.content.startswith('!members'):
            for guild in client.guilds:
                for member in guild.members:
                    await message.channel.send(member)

        if message.content.startswith('!name'):
           for guild in client.guilds:
                for name in guild.name:
                    await message.channel.send(name)

        if message.content.startswith('!banned_users'):
           for guild in client.guilds:
                for banned_users in ctx.guild.bans():
                    await message.channel.send(banned_users)



client.run(TOKEN)
