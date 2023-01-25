import discord
from discord.ext import commands
import modules.feedreader as fr
import modules.randomhelpers as rh
import modules.sqlHandler as mek

class ServerOptions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="serveroptions", with_app_command=True, description="Specify options for server.")
    async def serveroptions(self, ctx, botspamchannel: str = None):
       
        outputArray = []
        optionWriteColArray = []
        optionWriteValArray =[]
        serverid = ctx.guild.id
        print(f"serveroptions started {serverid}")
        if botspamchannel:
            print('there is a botspamchannel')
            if botspamchannel.isdigit():
                botspamchannelid = int(botspamchannel)
                optionWriteColArray.append('botspamchannel')
                optionWriteValArray.append(str(botspamchannelid))
            else:
                print("not digit")
                try:
                    botspamchannelid = (discord.utils.get(ctx.guild.channels, name=botspamchannel)).id
                    optionWriteColArray.append('botspamchannel')
                    optionWriteValArray.append(str(botspamchannelid))
                    
                    outputArray.append(f"Wrote {botspamchannel} as new bot spam channel.")

                except Exception as e:
                    rh.genErrorHandle(e)
                    outputArray.append(f"Error getting channel for {botspamchannel}.")

        writeColumns, writeVals = ",".join(optionWriteColArray), ",".join(optionWriteValArray)
        print("getting here")
        mek.sqlMektanixDevilDog(purpose='update',table='serversettings',resultColumn=writeColumns,queryColumn='serverid',queryField=str(serverid),insertData=writeVals)
        newLine="\n"
        await ctx.send(f"Thank you for using Pizza Hut Discord ordering service. {newLine.join(outputArray)}")
        # fr.feedReadMain(feed, keyword)
        # fr.feedSqlWriteNew(feed, keyword)
            # feed modify function in feedreader
        # if keyword:
        #     await ctx.send(f"Listening to feed {feed} with filter for term '{keyword}'!")
        # else:
        #     await ctx.send(f"Listening to feed {feed}!")
    
    
    # @commands.hybrid_command(name="")

async def setup(bot):
    await bot.add_cog(ServerOptions(bot))
