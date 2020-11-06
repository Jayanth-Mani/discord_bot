import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv("token.env") # replace ".env" with whatever you named your file
client_token = os.environ.get("token")
client = commands.Bot(command_prefix="$")

@client.command()
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

@client.command()
async def echo(ctx, *args):
    text = ""
    for arg in args:
        text = text + " " + arg
    await ctx.send(text)

@client.command()
async def hello(message):
    await message.channel.send("Hello " + message.author.display_name)

@client.command()
async def bm(ctx, *args):
    message = ""
    for arg in args:
        message = message + " " + arg
    if str(ctx.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")
        await modmail_channel.send("["+ ctx.author.display_name + "] " + message)


client.run(client_token)
