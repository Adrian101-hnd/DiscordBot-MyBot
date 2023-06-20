import discord
import asyncio
from discord.ext import commands,tasks


async def setup_cogs(bot):
    print("Done setting cogs")

async def main():
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix="h#",intents = intents)
    await setup_cogs(bot)
    print("Bot succesfuly deployed!")

asyncio.run(main())
