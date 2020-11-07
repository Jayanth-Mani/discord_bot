import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import torch
import transformers


load_dotenv(".env")
bot = commands.Bot(command_prefix="%")

@bot.command(name='generate')
async def gen(ctx):
    input_ids = lm_tokenizer.encode(ctx.message.content[10:], add_special_tokens=True, return_tensors='pt')
    beam_output = lm.generate(
        input_ids,  
        do_sample=True,
        max_length=200, 
        top_k=50, 
        top_p=0.95, 
    )

    await ctx.send(lm_tokenizer.decode(beam_output[0], skip_special_tokens=True))

if __name__ == "__main__":
    lm = transformers.GPT2LMHeadModel.from_pretrained("gpt2")
    lm_tokenizer = transformers.GPT2Tokenizer.from_pretrained("gpt2")
    bot.run(os.getenv("TOKEN"))
