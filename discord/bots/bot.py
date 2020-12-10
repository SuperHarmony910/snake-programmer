# SuperHarmony910's first Discord bot.
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
    print(f'{client.user} has connected to Discord!')

client = commands.Bot(command_prefix='./')

@client.event
async def on_message(message):
        if message.author == client.user:
           return;

        if message.content.startswith('poop'):
            await message.channel.send('💩');

        if message.content.startswith('!members'):
            for guild in client.guilds:
                for members in guild.members:
                    await message.channel.send(members)

        if message.content.startswith('!name'):
           for guild in client.guilds:
                for name in guild.name:
                    await message.channel.send(name)

        if message.content.startswith('hello'):
            await message.channel.send('Hello! 👋')




@client.command()
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)

async def on_message(message):
    link = "https://github.com/SuperHarmony910 Shameless plug!"
    if message.content('link'):
        await ctx.channel.send(link)



client.run(TOKEN)
