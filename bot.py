"""
This is code for Mr. Charles, a discord bot for the Wayland CS Club Server
"""

# discord
import discord
from discord.ext import commands

# other modules
import random

# my modules
from my_token import my_token
from mockery import memify
from eight import responses
from users import *
from channels import general
# DOCS: https://discordpy.readthedocs.io/en/latest/ext/commands/index.html

# setting up bot:
intents = discord.Intents(messages = True, guilds = True, reactions = True,
                         members = True, presences = True)
                         
client = commands.Bot(command_prefix='!', description="Mr. Charles is here to help",
                      intents=intents)
        
# CLIENT COMMANDS:

# will mock anything you send after !mock
@client.command()
async def mock(ctx, *, message):
    text = memify(message)
    await ctx.send(text)

#NOTE: this command will clear messages --be careful
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# gives you the latency of the bot
@client.command()
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(client.latency*1000)))

# eight ball command
@client.command(aliases=['8ball', 'future'])
async def _8ball(ctx, *, question):
    response = random.choice(responses)
    
    # to troll users
    # if str(ctx.author) == user_1:
    #     response = responses[len(responses)-1]
    # if str(ctx.author) == user_2:
    #     response = responses[0]

    await ctx.send(f'Question: \"{question}\"\nAnswer: ' + response)
            

# CLIENT EVENTS: https://stackoverflow.com/questions/52689954/what-it-really-is-client-event-discord-py
@client.event
async def on_ready():
    print("Mr. Charles is ready")
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(int(general))
    await channel.send(f'{member} finally decided to show up.')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(int(general))
    await channel.send(f'{member} just left the server!')
    
client.run(my_token)

# Written by Andrew Boyer
