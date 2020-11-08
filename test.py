import logging
import os

import discord
from discord.ext import commands
from discord import Member
from dotenv import load_dotenv

import transformers


load_dotenv(".env")
bot = commands.Bot(command_prefix="%", intents=discord.Intents(
    messages = True,
    guilds = True,
    reactions = True,
    members = True,
    presences = True,
))

@bot.command()
async def generate(ctx):
    input_ids = lm_tokenizer.encode(ctx.message.content[10:], add_special_tokens=True, return_tensors='pt')
    beam_output = lm.generate(
        input_ids,
        do_sample=True,
        max_length=200,
        top_k=50,
        top_p=0.95,
    )

    await ctx.send(lm_tokenizer.decode(beam_output[0], skip_special_tokens=True))


@bot.command()
async def status(ctx, member: Member=None):
    if member is None:
        member = ctx.author

    await ctx.send(str(member.activity) + " and " + str(member.status))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    lm = transformers.GPT2LMHeadModel.from_pretrained("gpt2")
    lm_tokenizer = transformers.GPT2Tokenizer.from_pretrained("gpt2")
    logger.info("Ready")
    bot.run(os.getenv("TOKEN"))
