import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv("token.env") # replace ".env" with whatever you named your file
client_token = os.environ.get("token")
client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("!Shenbot"):
        if str(message.author) == "B$hens#7985":
            await message.channel.send("Hello " + str(message.author) + " the master!")
        else:
            await message.channel.send("I am Shenbot")
    if message.content.startswith("!urmom"):
        await message.channel.send("Gay")
    if message.content.startswith("!joke"):
        await message.channel.send("Your life")
    if str(message.author) == "ManimanTestBot#2912":
        await message.channel.send("ManimanTestBot is my good friend")
    if str(message.channel) == "delete-text" and message.content != "":
        await message.channel.purge(limit=2)
    if str(message.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")
        await modmail_channel.send("["+ message.author.display_name + "] " + message.content)
    if str(message.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="bot-mail")
        await modmail_channel.send("["+ message.author.display_name + "] " + message.content)

client.run(client_token)

