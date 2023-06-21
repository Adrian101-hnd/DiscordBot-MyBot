import discord
from discord.ext import commands
import asyncio

#This cog helps you (I think)🔥
class helper_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="ayuda", aliases = ["a", "ayude"], help = "Auxilio")
    async def help(self,ctx):
        print("DONE")
        await ctx.send("Ayuda dada.")

def setup(bot):
    bot.add_cog(helper_cog(bot))