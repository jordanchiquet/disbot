# import discord
from discord.ext import commands
import modules.feedreader as fr

class Listen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="listen", with_app_command=True, description="Give a twitter username or rss feed url to listen for updates to, with optional filter keyword(s).")
    async def listen(self, ctx, feed, keyword: str = '', defaultchanneloverride: bool = False, delete: bool = False):
        chanid = ctx.channel.id
        print(f"CHANID {chanid}")
        serverid = ctx.guild.id
        print(f"SERVERID {serverid}")
        await ctx.send(fr.feedReadMain(chanid, serverid, feed, keyword))


async def setup(bot):
    await bot.add_cog(Listen(bot))


