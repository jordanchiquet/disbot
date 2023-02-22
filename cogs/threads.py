from discord.ext import commands

class Threads(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="thread")
    async def thread(self, ctx, *, message):
        pass