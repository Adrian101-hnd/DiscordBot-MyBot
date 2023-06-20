import discord
import asyncio
from discord.ext import commands,tasks
import os
from cogs.helper_cog import helper_cog
#Hay un problema con el load dotenv, no se que es lo veo mañana

async def setup_cogs(bot):
    await bot.add_cog(helper_cog(bot))
    print("Done setting cogs")

async def main():
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix="h#",intents = intents)
    await setup_cogs(bot)
    print("Bot succesfuly deployed!")
    await bot.start("")

asyncio.run(main())
