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

# Will commands be created in @client.event?

@client.event
async def on_message(message):
        if message.author == client.user:
           return;

        if message.content.startswith('poop'):
            await message.channel.send('💩');

        if message.content.startswith('!members'):
            for guild in client.guilds:
                for member in guild.members:
                    await message.channel.send(member)

        if message.content.startswith('!name'):
           for guild in client.guilds:
                for name in guild.name:
                    await message.channel.send(name)

        if message.content.startswith('hello'):
            await message.channel.send('Hello! 👋')

client = commands.Bot(command_prefix = "!")

@client.command(
     link = "https://github.com/SuperHarmony910 Shameless plug!"
)
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)

client.run(TOKEN)
