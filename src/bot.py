import discord
import asyncio
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
from cogs.helper_cog import helper_cog
from cogs.steam_cog import steam_cog
import importlib


load_dotenv()


async def setup_cogs(bot):
    await bot.add_cog(helper_cog(bot))
    await bot.add_cog(steam_cog(bot))
    print("Done setting cogs")

async def main():
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix="h#",intents = intents)
    await setup_cogs(bot)
    print("Bot succesfuly deployed!")
    await bot.start(os.environ.get("BOT_KEY"))
    
asyncio.run(main())
