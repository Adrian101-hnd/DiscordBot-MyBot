import discord
from discord.ext import commands
import asyncio

#This cog is for executing commands related to the steam API 👍
class steam_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name="game", aliases = ["g", "games"], help = "Gets info on a specific game")
    async def getGame(self,ctx,*args):
        query = " ".join(args)
        print(query)
        await ctx.send(query)

def setup(bot):
    bot.add_cog(steam_cog(bot))