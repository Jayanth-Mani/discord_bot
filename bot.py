import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from bot_jokes import *

client = commands.Bot(command_prefix=";;")

@client.command()
async def echo(ctx, *args):
    message = ''
    for arg in args:
       message = message + " " + arg
    await ctx.send(message)

@client.command()
async def joke(ctx):
    await ctx.send(getJoke())    
load_dotenv(".env") # replace ".env" with whatever you named your file
client_token = os.environ.get('TOKEN')

client.run(client_token)