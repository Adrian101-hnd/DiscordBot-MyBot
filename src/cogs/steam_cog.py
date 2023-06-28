import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from services.steam_service import steam_fn
load_dotenv()

#This cog is for executing commands related to the steam API 👍
class steam_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.steam = steam_fn(os.environ.get("STEAM_API_KEY"))

    
    @commands.command(name="game", aliases = ["g", "games"], help = "Gets info on a specific game")
    async def getGame(self,ctx,*args):
        query = " ".join(args)
        steam_id = self.steam.game_search(query)
        players_n = self.steam.player_count(steam_id,query)
        await ctx.send("The number of people playing "+ query + " is "+ str(players_n))

def setup(bot):
    bot.add_cog(steam_cog(bot))