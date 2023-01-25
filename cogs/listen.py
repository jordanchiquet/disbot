# import discord
from discord.ext import commands
import modules.feedreader as fr

class Listen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="listen", with_app_command=True, description="Give a twitter username or rss feed url to listen for updates to, with an optional keyword filter.")
    async def listen(self, ctx, feed, keyword: str = '', delete: bool = False):
        chanid = ctx.channel.id
        print(f"CHANID {chanid}")
        serverid = ctx.guild.id
        print(f"SERVERID {serverid}")
        await ctx.send(fr.feedReadMain(chanid, serverid, feed, keyword))
        # fr.feedReadMain(feed, keyword)
        # fr.feedSqlWriteNew(feed, keyword)
            # feed modify function in feedreader
        # if keyword:
        #     await ctx.send(f"Listening to feed {feed} with filter for term '{keyword}'!")
        # else:
        #     await ctx.send(f"Listening to feed {feed}!")
    
    
    
    # @commands.hybrid_command(name="")

async def setup(bot):
    await bot.add_cog(Listen(bot))

    

"""
rain in games
peez
tamler
warhammer something or other
from soft
dark and darker
predernATORCESSor
"""