from discord.ext import commands
import pyshorteners



class UrlHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="tinyurl", with_app_command=True, description="Shorten a url.")
    async def tinyurl(self, ctx, url):
        s = pyshorteners.Shortener()
        await ctx.send(s.tinyurl.short(url))

async def setup(bot):
    await bot.add_cog(UrlHandler(bot))