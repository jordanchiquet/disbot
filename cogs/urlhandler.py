import discord

from discord.ext import commands
import pyshorteners



class UrlHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="hyperlink", with_app_command=True, description="Shorten a url.")
    async def tinyurl(self, ctx, url, displaytext):
        embed = discord.Embed()
        embed.description = f"[{displaytext}]({url})"
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(UrlHandler(bot))