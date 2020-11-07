"""
This is code for Mr. Charles, a discord bot for the Wayland CS Club Server
"""
import discord
from discord.ext import commands
from my_token import my_token
from mockery import memify
# DOCS: https://discordpy.readthedocs.io/en/latest/ext/commands/index.html

# setting up bot:
intents = discord.Intents(messages = True, guilds = True, reactions = True,
                         members = True, presences = True)
client = commands.Bot(command_prefix='!', description="Mr. Charles is here to help",
                      intents=intents)

# FUNCTIONS: 
def args_text(*args):
    t = ""
    for arg in args:
        t = t + " " + arg
    return t
        
# CLIENT COMMANDS:
@client.command()
async def mock(ctx, *args):
    text = memify(args_text(*args))
    await ctx.send(text)

# CLIENT EVENTS: https://stackoverflow.com/questions/52689954/what-it-really-is-client-event-discord-py
@client.event
async def on_ready():
    print("Mr. Charles is ready")
    
@client.event
async def on_member_join(member):
    print(f'{member} finally decided to show up.')

@client.event
async def on_member_remove(member):
    print(f'{member} just left the server!')
    
client.run(my_token)

# Written by Andrew Boyer
