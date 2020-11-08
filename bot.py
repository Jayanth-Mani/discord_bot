import discord
import os
from dotenv import load_dotenv

client = discord.Client()
@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    
    if message.content.startswith("hello"):
        
        if str(message.author) == "Maniman#8394":
            await message.channel.send("Hello good sir, " + str(message.author))
    

load_dotenv(".env") # replace ".env" with whatever you named your file
client_token = os.environ.get('TOKEN')

client.run(client_token)