# discord imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
# my other imports
import random
import os
import itertools as it
import pyjokes
from weather_command import *


load_dotenv("ultimate.env") # replace ".env" with whatever you named your file
client_token = os.environ.get("token")
client = commands.Bot(command_prefix="$")


def alias_creator(s): # this makes it so that you can use any combination of uppercase and lowercase to call a command
    lu_sequence = ((c.lower(), c.upper()) for c in s)
    product = [''.join(x) for x in it.product(*lu_sequence)]
    for word in product:
        if word == str(s):
            product.remove(word)
    return product
    

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")
    await member.channel.send(f"{member} has joined the server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")
    await member.channel.send(f"{member} has left the server.")

# gives you the latency of the bot
@client.command(aliases = alias_creator("ping"))
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(client.latency*1000)))

@client.command(aliases = alias_creator("server"))
async def server(ctx):
    name = str(ctx.guild.name)
    desc = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        Description=desc,
        color=discord.Color.blue()    
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@client.command(aliases = alias_creator("echo"))
async def echo(ctx, *args): # $echo + stuff will return the same things inputed.
    text = ""
    for arg in args:
        text = text + " " + arg
    await ctx.send(text)

@client.command(aliases = alias_creator("mock"))
async def mock(ctx, *args): # $echo + stuff will return the same things inputed.
    text = ""
    for arg in args:
        text = text + " " + arg
    translation = ""
    for x in text:
        rand = random.randint(1,11)
        if rand<=5:
            translation = translation + x.upper()
        else:
            translation = translation + x.lower()
    await ctx.send(translation)

@client.command(aliases = alias_creator("hello"))
async def hello(message): # $hello will return "Hello + your username"
    await message.channel.send("Hello " + message.author.display_name)

@client.command(aliases = alias_creator("bm"))
async def bm(ctx, *args): # using the command $bm while DMing the bot will put it int mod-mail
    message = ""
    for arg in args:
        message = message + " " + arg
    if str(ctx.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")
        await modmail_channel.send("["+ ctx.author.display_name + "] " + message)

@client.command()
async def sup_b_shens(ctx):
    await ctx.channel.send(f"Sup {ctx.author.display_name}.")

@client.command(aliases = alias_creator("joke"))
async def joke(ctx):
    await ctx.channel.send(pyjokes.get_joke(language="en"))

@client.command(aliases = alias_creator("weather"))
async def weather(ctx):
    query = ctx.message.content[9:]
    result = weather_report(query)
    desc = result[0]
    temp = result[1]
    feel = result[2]

    embed = discord.Embed(
        title=query + " Weather Data",
        Description= "This is the data from the city you asked for",
        color=discord.Color.blue()    
    )
    icon = str("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.le89Xert7ixw1G9XibizoQAAAA%26pid%3DApi&f=1")
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Weather: ", value=desc, inline=True)
    embed.add_field(name="Temperature: ", value=temp, inline=True)
    embed.add_field(name="Feels like: ", value=feel, inline=True)

    await ctx.send(embed=embed)

@client.command(aliases = alias_creator("forecast"))
async def forecast(ctx):
    query = ctx.message.content[10:]
    result = weather_forecast(query)
    day1 = result["day 1"]
    day2 = result["day 2"]
    day3 = result["day 3"]
    day4 = result["day 4"]
    day5 = result["day 5"]

    embed = discord.Embed(
        title=query + " Weather Forecast",
        Description= "This is the forecast from the city you asked for",
        color=discord.Color.blue()    
    )
    icon = str("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.le89Xert7ixw1G9XibizoQAAAA%26pid%3DApi&f=1")
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Day 1: ", value=day1, inline=False)
    embed.add_field(name="Day 2: ", value=day2, inline=False)
    embed.add_field(name="Day 3: ", value=day3, inline=False)
    embed.add_field(name="Day 4: ", value=day4, inline=False)
    embed.add_field(name="Day 5: ", value=day5, inline=False)

    await ctx.send(embed=embed)

client.run(client_token)

#coded by Brendan Shens