import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from joke_scraper import *
from get_youtube_video import *

client = commands.Bot(command_prefix=";;")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(";;being a bot."))
    print("ManimanBot is ready.")

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

@client.command()
async def youtube(ctx, *args):
    titleSearch = ""
    for arg in args:
        titleSearch = titleSearch + " " + arg

    url = "https://www.youtube.com/watch?v=" + str(getVideo(titleSearch))
    await ctx.send("Here is the top result: " + url)

client.run(client_token)