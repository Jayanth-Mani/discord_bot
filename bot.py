import discord

client = discord.Client()
@client.event

async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    
    if message.content.startswith("hello"):
        
        if str(message.author) == "Maniman#8394":
            await message.channel.send("Hello good sir, " + str(message.author))

        await message.channel.send('Shenbot is my good friend')
    
    if str(message.author) == "B$hens#7985":
        await message.channel.send("Ahh, B Shen, creator of Shenbot, my good friend")

# add your token instead
client.run('NzY2NDgzOTExMjM2MTI0Njcy.X4kBxQ.W-6fVSq7Xk5_Ch2f6X0MtOlvIOQ')

