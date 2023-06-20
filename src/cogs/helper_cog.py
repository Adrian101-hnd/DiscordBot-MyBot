import discord
from discord.ext import commands
import asyncio

class helper_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="ayuda", aliases = ["a", "ayude"], help = "Auxilio")
    async def help(self,ctx):
        print("DONE")
        await ctx.send("Ayuda dada.")