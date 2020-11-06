import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")
cli = discord.Client()

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
async def hello(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@cli.event
async def on_message(message):
    if str(message.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")
        await modmail_channel.send("["+ message.author.display_name + "] " + message.content)

client.run("Nzc0MDgzNTExNDA1MjQ4NTMy.X6Sncg.2miOxdZQkRdwku6K9bRGHb0xWOM")
