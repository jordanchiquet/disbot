#!/usr/bin/env python3

#TODO: pipdependencies script
#TODO: venv on aws
#TODO: owned counter

versionstr = "v6.6.6"


#API DISCORDHACK


import datetime
import discord #discord
import logging
import os, os.path
import modules.feedreader as fr
import mysql.connector #mysql-connector-python 
import random
import re
import requests
import sys
import time
# import tenorpy #tenorpy TODO: deprecated... net to switch to TenGiphPy for gifs
import urllib.parse
import urllib.request
import wikipediaapi #wikipedia-api
from bs4 import BeautifulSoup #bs4
from datetime import datetime, timedelta
from discord import File, app_commands
from discord.ext import commands, tasks
from discord.utils import get
# from discord_slash import SlashCommand,SlashContext
from googleapiclient.discovery import build #google-api-python-client
# from GoogleScraper import scrape_with_config, GoogleSearchError TODO: am i even using this
from googlesearch import search #google
from urlextract import URLExtract #urlextract

import modules.serverset as serv
from modules.countgraphs import GraphMaker
from modules.dice import dice
from modules.piltools.dickshadow import executeoverlay #Pillow #numpy #whapi
from modules.figlet import figgletizer 
from modules.onmessagetools import onMessageMain
from modules import quoteshandler as qh
from modules.webquerytools.gifgrab import getgif
from modules.webquerytools.googleimageapi import imageget
from modules.webquerytools.merriamapi import getmeaning
from modules.randomhelpers import genErrorHandle
from modules.timertools import timerExpiryCheck, timerNotify, timerWriter
from modules.timertools.expiryExclaims import exclaimList
from modules.webquerytools.wikihow import wikihow
from modules.webquerytools.youtube import youtubesearch
from modules.zooo import zooo


# sys.stdout = open('hackbotlogfile.txt', 'w')


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        # intents.reactions = True
        # intents.members = True
        # intents.guilds = True   
        # intents.members = True
        super().__init__(command_prefix = ",", case_insensitive=True, intents=intents) #application_id=608080063019352084
    
    async def setup_hook(self):
        print(f"starting setup_hook for {self.user}.")
        # await load()
        await self.tree.sync()
        print("tree sync complete.")
    
    async def on_ready(self):
        print("ready")
        channel_bot_testing = bot.get_channel(600430089519497235)
        await channel_bot_testing.send(content="hackable online")
        # feedcheck.start()
        print("sent")

bot = Bot()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

# @bot.event
# async def on_ready():
#     print("ready")
#     channel_bot_testing = bot.get_channel(600430089519497235)
#     await channel_bot_testing.send(content="hackable online")
#     print("sent")



# @bot.hybrid_command(name="test", with_app_command=True, description="test1")
# async def test(ctx: commands.Context):
#     await ctx.reply("test")




renardgenchannel = bot.get_channel(649528092691529749)


deletelog = {}
commandRunningDict = {}
chatLog = []
jordan_id = 191688156427321344


now = datetime.now() - timedelta(hours=5)


@bot.event
async def on_message_delete(message):
    if message.id in deletelog:
        dellog = deletelog[message.id]
        print("deleting msg")
        print(dellog)
        await dellog.delete()
        del deletelog[message.id]


@bot.event
async def on_message_edit(before, after):
    if before.id in deletelog:
        edlog = deletelog[before.id]
        ytquery = urllib.parse.urlencode({"search_query": after.content[4:]})
        html_cont = urllib.request.urlopen("http://youtube.com/results?" + ytquery)
        ytresult = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
        delcmd = await edlog.edit(content=("http://youtube.com/watch?v=" + ytresult[0]))
        deletelog[after] = delcmd
    if (after.content).startswith("."):
        # edmessage = msgloginmem[before.id]
        print('starting process cmd')
        await bot.process_commands(after)


@bot.event
async def on_member_join(member):
    if member.guild.id == 237397384676507651:
        channel = bot.get_channel(649528092691529749)
    elif member.guild.id == 688494181727207478:
        channel = bot.get_channel(767847844039753789)
    await channel.send("a pedophile has joined the chatroom")


@tasks.loop(seconds=300.0)
async def commandRunningDictClear():
    print("clearing commandRunningDict (dict for belay order shit)")
    commandRunningDict.clear()
    chatLog.clear()



@bot.event
async def on_member_update(before, after):
    print("detected presence update")
    if before.nick != after.nick:
        print("nick counter arrive line 1")
        try:
            print("nick changed for user " + str(before.id) + " from " + before.nick + " to " + after.nick)
        except:
            print("user " + str(before.id) + " changed name from one there's no record of to " + after.nick)
        #nickcounterinit = wordcounter(before.id, before.guild.id, after.nick, nicktally=True)
        #nickcounterinit.countprocessor()
    user = after.id
    if user == 978091507741499425 and after.nick != "jordanlivingroom":
        print("bot nick reach")
        await before.edit(nick="jordanlivingroom")

msgCache = {} #blank dict for coupling ids with message content


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         commandRunningDict[message.id] = message.content
#         print("bot command logged")
#         return
#     else:
#         chatLog.append(message.content)
#     serverid = message.guild.id
#     channelid = message.channel.id
#     userid = message.author.id
#     authorfull = str(message.author)
#     username = authorfull.split("#")[0]
#     channel = message.channel
#     print(message.author)
#     user = (str(message.author)).split("#")[0]
#     timeorig = (message.created_at - timedelta(hours=5))
#     mclower = message.content.lower()
#     onMessageInit = onMessageMain.onMessageHandler(serverid, channelid, userid, username, timeorig, mclower)
#     onMessageResult = onMessageInit.messageHandleTestBot()
#     if onMessageResult[0] != None:
#         if onMessageResult[0] == "text":
#             await channel.send(onMessageResult[1])
#         elif onMessageResult[0] == "file":
#             await channel.send(file=File(onMessageResult[1]))

#     if len(chatLog) >= 3: 
#         if chatLog[-1] == chatLog[-2] and chatLog[-2] == chatLog[-3]:
#             await channel.send(chatLog[-2])
#             chatLog.clear()
    
#     if not mclower.startswith(".") and ("belay that order" in mclower or "cancel that order" in mclower or "cancel that command" in mclower or "delete that timer" in mclower
#      or "cancel that timer" in mclower or "erase that timer" in mclower):
#         print("belay that in command, checking commandRunning Dict")
#         if  commandRunningDict != []:
#             print("dict is not empty")
#             deletionID = [*commandRunningDict.keys()][-1]
#             print("made it to first key acquire")
#             msgObj = await channel.fetch_message(deletionID)
#             commandMsgStr = commandRunningDict[deletionID]
#             print(commandMsgStr)
#             if "Timer set for " in commandMsgStr:
#                 print("timer detected in command")
#                 authorRegCheck = re.search("[a-zA-Z]+#[0-9]{4}", commandMsgStr)
#                 if authorRegCheck.group() == str(message.author):
#                     print("belay order call was made by timer author")
#                     deltable = "timers"
#                 else:
#                     await channel.send("I cannot do that sir, the timer is DNA-locked by Commander " + authorRegCheck.group() + ".")
#                     return
#             elif commandRunningDict[deletionID].startswith("Quote ") and " added by " in commandRunningDict[deletionID]:
#                 print("quotes detected in command")
#                 deltable = "quotes"
#             else:
#                 await msgObj.delete()
#                 await channel.send("TRANSPHASIC PAYLOAD DROPPED... MESSAGE OBLITERATED")
#                 return
#             mydb = mysql.connector.connect(
#                 host='3.144.163.74',
#                 user='dbuser',
#                 passwd='e4miqtng')
#             mycursor = mydb.cursor()
#             sql = "DELETE FROM renarddb." + deltable + "\nORDER BY id DESC LIMIT 1"
#             mycursor.execute(sql)
#             mydb.commit()
#             await msgObj.delete()
#             await channel.send("LAUNCHING " + deltable[:-1].upper() + " TORPEDOES")
#         else:
#             print("nothing to belay..")
#             await channel.send("Nothing to belay Sir.")
#     await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    Gib = bot.get_emoji(410972413036331008)
    message = reaction.message
    channel = reaction.message.channel
    serverid = reaction.message.guild.id
    ts = message.created_at - timedelta(hours=5)
    messageuser = message.author
    msguserstr = str(messageuser)
    messageContent = message.content
    messageuserid = messageuser.id
    reactionuser = user.id
    #emotecountinit = wordcounter(reactionuser, serverid, str(user), reacttally=True)
    #emotecountinit.countprocessor()
    msgOut = None
    if reaction.emoji == '🙂' and not user.bot:
        print("speech bubble called")
        quoteAddResult = qh.addQuote(user=msguserstr, quoteStr=messageContent, timestamp=str(ts),
        serverid=serverid, userid=messageuserid)
        quoteId = str(quoteAddResult[1])
        if quoteAddResult[0]:
            msgOut = ("Quote " + quoteId + " added by " + msguserstr + ".")
        else: 
            msgOut = (msguserstr + " tried to add a quote that is already in as " + quoteId)     
    elif reaction.emoji == '🙁' and messageuser.bot:
        print("gib called for bot message")
        extraNotifyInit = timerNotify.timerNotify(str(reactionuser), messageContent)
        result = extraNotifyInit.extraNotifyWrite()
        if result == "timer inactive":
            msgOut= "timer is expired, deleted, or something went wrong, " + (str(user)).split("#")[0]
        elif result == "duplicate userid":
            msgOut = "you are already in the notify list for that timer, " + (str(user)).split("#")[0]
        else:
            msgOut = (str(user) + " added to notify list for timer " + result + ".")
    if msgOut is not None:
        await channel.send(msgOut)


        # timerID = timerExtranNotify.getTimerID(messageContent)
        # #TODO: getting timerID 1 pack everytime, fix this
        # if timerID == "invalid":
        #     print("got invalid for timerID for: [" + messageContent + "]")
        #     return None
        # else:
        #     userid = str(reactionuser)
        #     timerSQL.addNotifyUsers(id=timerID, userid=userid)
        #     print("attempted addNotifyUsers for timer + [" + str(timerID) + 
        #     "] with userid: [" + userid + "]")
        #     #TODO: check for duplicate notify - should not notify original
        #     #user more than once, or add someone already in addNotify
    

        


@bot.event
async def on_reaction_remove(reaction, user):
    message = reaction.message
    channel = reaction.message.channel
    messageuser = message.author
    reactuser = user
    reactionuserid = user.id
    messageContent = message.content
    outMsg = None
    ts = message.created_at - timedelta(hours=5)
    if reaction.emoji == '🙂' and not user.bot:
        qh.deleteQuoteByTime(str(ts))
        outMsg = ("Quote erased from the archive memory :).")
    elif reaction.emoji == '🙁' and messageuser.bot:
        removeInit = timerNotify.timerNotify(str(reactionuserid), messageContent)
        timerid = removeInit.removeNotifyUser()
        outMsg = str(reactuser) + " removed from timer " + timerid + " notify list!"
    if outMsg is not None:
        await channel.send(outMsg)


@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound) and "..." not in ctx.message.content:
            print("command not found")


# ----------------- Tasks ----------------- #

@tasks.loop(seconds=5.0)
async def feedcheck():
    try:
        print("feedcheck started")
        resultArray = fr.feedCheckAll()
        newLine = "\n"
        if len(resultArray) > 0:
            print(f"results in feedcheck:[{newLine.join(resultArray)}]")
            for result in resultArray:
                resultSplit = result.split('|')
                link, serverid, chanid = resultSplit[0], resultSplit[1], resultSplit[2]
                checkForChannel = serv.getServerSetting(serverid, 'botspamchannel')
                if checkForChannel:
                    chanid = checkForChannel
                outChannel = bot.get_channel(chanid)
                await outChannel.send(link)
    except Exception as e:
        genErrorHandle(e)
        pass
            





# ----------------- Commands ----------------- #
# ---------------------------------------- #
##DEBUGCOMMANDS##
@bot.command()
async def embedobject(ctx):
    async for message in ctx.channel.history(limit=2):
        print(message.content)
        if message.embeds:
            print("debug line embedobject")
            outstr = f"message.embeds[0]: {message.embeds[0]}\n.type: {message.embeds[0].type}\n.description: {message.embeds[0].description}\n.image:{message.embeds[0].image.url}"
            await ctx.send(outstr)
            print(outstr)

@bot.command()
async def hasembedimg(ctx):
    async for message in ctx.channel.history(limit=2):
        if message.embeds:
            outstr = "has embed"
            if message.embeds[0].image:
                outstr += "|has image"
            else:
                outstr += "|no image"
        else:
            outstr = "no embeds"
        await ctx.send(outstr)

@bot.command()
async def feedback(ctx):
    fdbackmsg = ctx.message.content[10:]
    jordan = bot.get_user(191688156427321344)
    await jordan.send(fdbackmsg)
    await ctx.send("feedback sent to creator")


@bot.command()
async def chanid(ctx):
    await ctx.send(ctx.channel.id)


@bot.command()
async def datetest(ctx):
    """test"""
    await ctx.send("datetime.now(): " + str(datetime.now()) + "\n" + 
                   "datetime.now().date(): " + str(datetime.now().date()))


@bot.command()
async def axestupletest(ctx, a):
    print("graphtest cmd called")
    graphInit = GraphMaker(ctx.guild.id, a)
    outMsg = graphInit.main()
    await ctx.send(str(outMsg))


@bot.command()
async def ding(ctx):
    dong = str(bot.latency * 1000)
    await ctx.send("dong!! " + dong[:2] + " ms")


@bot.command()
async def fb(ctx):
    fdbackmsg = ctx.message.content[3:]
    jordan = bot.get_user(191688156427321344)
    await jordan.send(fdbackmsg)
    await ctx.send("feedback sent to creator")


@bot.command()
async def mtn(ctx):
    await ctx.send("this is a test mention message, <@!" + str(ctx.message.author.id) + ">")


@bot.command()
async def ping(ctx):
    pong = str(bot.latency * 1000)
    await ctx.send("pong!! " + pong[:2] + " ms")


@bot.command()
async def strcheck(ctx, a):
    if a == "raw":
        usablestr = ((ctx.message.content).split(a))[1]
        if usablestr[0] == " ":
            usablestr = usablestr[0:]
        await ctx.send(usablestr)
    elif a is None:
        usablestr = "no string to check detected"
    else:
        usablestr = "```" + ctx.message.content[10:] + "```"
    print("strcheck: " + usablestr)
    await ctx.send(usablestr)


@bot.command()
async def todo(ctx):
    if ctx.author.id == jordan_id:
        todoWrite = "\n- " + ctx.message.content[6:]
        with open("todo.txt", 'a') as f:
            f.write(todoWrite)
            f.close()
        outMsg = "appended"
    else:
        outMsg = "🤖"
    await ctx.send(outMsg)



# @bot.command()
# async def timerdebug(ctx):
#     timercheckinit = timercl("msgcontent", "user", "channel", "timeorig")
#     response = timercheckinit.timercheck()
#     if response == "no timepops":
#         return
#     else:
#         channel = bot.get_channel(int(response[3]))
#         if response[2] == "":
#             await  channel.send("<@!" + response[1] + "> Ringa ling dong, the time " + (response[4])[:-3] + " has finally come!")
#         else:
#             await channel.send("<@!" + response[1] + "> Sir you must remember: \"" + response[2] + "\" | " + (response[4])[:-3])


@bot.command()
@commands.has_role("High Council of Emoji")
async def close(ctx):
    await ctx.send("Personal PC Computer plugging off online mode shut down - COMPUTER OFF")
    print("terminate request received")
    await sys.exit()

# @bot.command()
# @commands.has_role("High Council of Emoji")
# async def pull(ctx):
#     pullrestart()


@close.error
async def close_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        username = ctx.message.author.display_name
        userid = ctx.message.author.id
        response = [
            "You do not have the clearance for that command... are you retarded?",
            "You aren't a server admin... this is why she left you dude.",
            "Try that shit again and see who gets terminated bitch ;)",
            "It seems like there's a lot you don't know about terminating this bot",
        ]
        await ctx.send(random.choice(response))
        print("insufficient perms to terminate " + username + " " + str(userid))


# ---------------------------------------- #
# documentation
# @bot.command()
# async def help(ctx):
#     await ctx.send("List of commands: https://pastebin.com/dBDALLSX")


@bot.command()
async def version(ctx):
    embed = discord.Embed(title="hackablebot.py", description="jordan test bot", color=0xee657)
    embed.add_field(name="Version", value=versionstr)
    embed.add_field(name="Release Notes", value="shorturl.at/bjwC1")
    await ctx.send(embed=embed)

@bot.command()
async def vers(ctx):
    version.invoke(ctx)

@bot.command()
async def notifyme(ctx):
    print("notifyme called")
    notifyrole = discord.utils.find(lambda r: r.name == 'botnotify', ctx.message.guild.roles)
    print("got notifyme role")
    notifyuser = ctx.message.author
    print("got notifyme user")

    if notifyrole in notifyuser.roles:
        print("found notifyrole in user roles")
        await notifyuser.remove_roles(notifyrole)
        await ctx.send("You will no longer be notified with bot updates.")
    else:
        print("did not find notifyrole in user roles")
        await notifyuser.add_roles(notifyrole)
        await ctx.send("You will be notified with bot updates.")


# ------------------------------------------- #
# practical functions



                
# @tasks.loop(seconds=5.0)
# async def timercheck():
#     print(str(datetime.now()) + " timercheck started")
#     checked = timerExpiryCheck.expiryCheck()
#     print("timerCheck got expiryCheck")
#     if len(checked) > 1:
#         print("timerCheck got checked longer than 1 char")
#         notifyChannel = bot.get_channel(int(checked[1]))
#         print("timerCheck got notifyChannel: [" + str(notifyChannel) + "]")
#         notifyUser = checked[2]
#         print("timerCheck got notifyUser: [" + notifyUser + "]")
#         expiryTime = " | " + (checked[3])[:-10] + " "
#         print("timerCheck got expiryTimer: [" + expiryTime + "]")
#         expiryNote = checked[4]
#         print("timerCheck got expiryNote: [" + expiryNote + "]")
#         if expiryNote == "":
#             exclaim = str(random.choice(exclaimList))
#             notifyMessage = (notifyUser + exclaim + expiryTime)
#         else:
#             notifyMessage = (notifyUser + expiryNote + expiryTime)
#         print("timerCheck outgoing notifyMessage: [" + notifyMessage + "]")
#         await notifyChannel.send(notifyMessage)
#     else:
#         return


@bot.command()
async def timer(ctx, a: str = None):
    timerInit = timerWriter.timerWriter(ctx.author.id, ctx.channel.id, ctx.message.content)
    if a is None:
        messageOut = "https://iknowwhatyoudownload.com/en/peer/"
    if a.startswith == "del":
        timerExpiryCheck.expiryCheck()
        messageOut = "check logs"
    else:
        messageOutTup = timerInit.timerWriterMain()
        if type(messageOutTup) is str:
            messageOut = messageOutTup
        else:
            messageOut = messageOutTup[1]
    await ctx.send(messageOut)



# ------------------------------------------------ #
# random math


@bot.command()
async def add(ctx, a, b):
    await ctx.send(a + b)


@bot.command()
async def div(ctx, a: int, b: int):
    await ctx.send(a / b)


@bot.command()
async def mul(ctx, a: int, b: int):
    await ctx.send(a * b)


@bot.command()
async def roll(ctx, a, b: str = None, c: str = None, d: str = None, e: str = None):
    print("dice initiated")
    if b is None or not b[0].isdigit():
        print("dice is one roll, with or without adv")
        rollinit0 = dice(a, b)
        if a.startswith("ab"):
            rollresult = rollinit0.abilityroller()
        else:
            rollresult = rollinit0.roller()
    elif a.startswith("ab"):
        rollinit0 = dice(a,b)
        rollresult = rollinit0.abilityroller()
    else:
        rollinit0 = dice(a)
        print("rollinit0 has launched")
        rollinit1 = dice (b)
        print("rollinit1 has launched")
        rollresult = rollinit0.roller() + "\n" + rollinit1.roller()
        if c is not None:
            rollinit2 = dice(c)
            print("rollinit2 has launched")
            rollresult = rollresult + "\n" + rollinit2.roller()
        if d is not None:
            rollinit3 = dice(d)
            print("rollinit3 has launched")
            rollresult = rollresult + "\n" + rollinit3.roller()
        if e is not None:
            rollinit4 = dice(e)
            print("rollinit4 launched")
            rollresult = rollresult + "\n" + rollinit4.roller()
    print("rollresult: [" + rollresult + "]")
    await ctx.send(rollresult)


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("That's not how I roll brother...")


@bot.command()
async def sub(ctx, a: int, b: int):
    await ctx.send(a - b)


# ------------------------------------------------ #
# random shit


@bot.command()
async def bird(ctx):
    birdr = requests.get('https://some-random-api.ml/img/birb')
    birdf = str(birdr.json()['link'])
    await ctx.send(birdf)


@bot.command()
async def cat(ctx):
    catr = requests.get('http://aws.random.cat/meow')
    catf = str(catr.json()['file'])
    await ctx.send(catf)


@bot.command()
async def coin(ctx):
    coinflip = ("Heads", "Tails")
    await ctx.send(random.choice(coinflip))


@bot.command()
async def conch(ctx):
    path, dirs, files = os.walk("/home/ubuntu/disbot/picfolder/conchfolder").__next__()
    min = 1
    max = len(files)
    conchfile = random.randint(min, max)
    destiny = ("Yes", "No")
    await ctx.send(file=File("/home/ubuntu/disbot/picfolder/conchfolder/conch" + str(conchfile) + ".png"))
    await ctx.send(random.choice(destiny))


@bot.command()
async def dog(ctx):
    dogr = requests.get('fhttps://dog.ceo/api/breeds/image/random')
    dogf = str(dogr.json()['message'])
    await ctx.send(dogf)

#TODO: flesh out, make separate lists (lunch, quick, dinner, date, etc)
@bot.command()
async def eat(ctx):
    any = (
        "Albasha",
        "Bay Leaf",
        "Burgersmith",
        "City Pork",
        "Curbside",
        "Curry N Kabob",
        "Duang Tuan",
        "Dang's"
        "El Rancho",
        "Elsie's",
        "Fat Cow",
        "La Caretta",
        "Lit",
        "Mooyah",
        "Pluckers",
        "Serops",
        "Superior Grill",
        "Sushi Masa",
        "Tsunami",
        "Umami",
        "Velvet Cactus"
    )
    await ctx.send(random.choice(any))


# @bot.hybrid_command(name="enhance", with_app_command=True, description="Enhance last image in the chat - 20 message cache.")
# async def enhance(ctx):
#     msg = ctx.message
#     channel = ctx.channel
#     history = channel.history
#     print(f"channel:{channel}")
#     haveimg = False
#     bgtitle = "/home/ubuntu/disbot/picfolder/shadowdir/providedbackground.png"
#     if os.path.isfile(bgtitle):
#         os.remove(bgtitle)
#     if not msg.attachments and not msg.embeds:
#         print("enhance message did not have an attachment")
#         async for message in ctx.channel.history(limit=20):
#             print("iterating history")
#             hasembeddedimage = False
#             if message.attachments:
#                 print("attempting to save attachment...")
#                 await message.attachments[0].save(bgtitle)
#                 haveimg = True
#                 break
#             elif message.embeds:
#                 print(f'message.embeds: {message.embeds}')
#                 if message.embeds[0].type == "image":
#                     print("attempting to save embed...")
#                     print(message.embeds[0].url)
#                     urllib.request.urlretrieve(message.embeds[0].url, bgtitle)
#                     haveimg = True
#                     break
#             else:
#                 continue


# @bot.command()
# async def football(ctx, a):
#     print("placeholder")
#     if a == "submit":
#         if ctx.message.author.id == 191688156427321344:
#             usable = (ctx.message.content.split[a]).replace(" ","")
#             sublist = usable.split(",")
#         else:
#             ctx.send("youve notten permission to to this")


@bot.command()
async def fox(ctx):
    foxr = requests.get('https://randomfox.ca/floof/')
    foxf = str(foxr.json()['image'])
    await ctx.send(foxf)


@bot.command()
async def fuck(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("fuckcount", serverid)
    elif a == "total" or a == "count":
        getgraph("fuckcount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def south(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("southcount", serverid)
    elif a == "total":
        getgraph("southcount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def inanycase(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("inanycase", serverid)
    elif a == "total":
        getgraph("inanycount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def nicks(ctx):
    serverid = ctx.guild.id
    getgraph("nicknames", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def positive(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("yescount", serverid)
    elif a == "total":
        getgraph("yescount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def negative(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("nocount", serverid)
    elif a == "total":
        getgraph("nocount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def dude(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("dudecount", serverid)
    elif a == "total":
        getgraph("dudecount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def imgcount(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("imgsearchcount", serverid)
    elif a == "total":
        getgraph("imgsearchcount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def like(ctx, a: str = None):
    serverid = ctx.guild.id
    if a is None:
        getgraph("likecount", serverid)
    elif a == "total":
        getgraph("likecount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def count(ctx):
    serverid = ctx.guild.id
    getgraph("msgcount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def words(ctx):
    serverid = ctx.guild.id
    getgraph("wordcount", serverid, True)
    await ctx.send(file=File("graph.png"))
    os.remove('graph.png')


@bot.command()
async def word(ctx):
    words.invoke(ctx)


@bot.command()
async def figlet(ctx):
    await ctx.send("```" + figgletizer(ctx.message.content[8:]) + "```")


@bot.command()
async def gun(ctx):
    path, dirs, files = os.walk("/home/ubuntu/disbot/picfolder/bitchfolder").__next__()
    min = 1
    max = len(files)
    bitchfile = random.randint(min, max)
    await ctx.send(file=File("/home/ubuntu/disbot/picfolder/bitchfolder/bitchfile" + str(bitchfile) + ".png"))


@bot.command()
async def loon(ctx):
    await ctx.send("https://youtu.be/asXfA40uudo")


@bot.command()
async def pepocheer(ctx):
    await ctx.send(file=File("home/ubuntu/disbot/picfolder/pepocheer.gif"))


@bot.command()
async def cheer(ctx):
    await pepocheer.invoke(ctx)


@bot.command()
async def qp(ctx):
    msg = ctx.message
    print(msg.content)
    if ctx.guild.id == 237397384676507651:
        await msg.add_reaction('<:Jeff:601576645807046656>')
        await msg.add_reaction('<:What:370701344232701952>')
    elif ctx.guild.id == 688494181727207478:
        await msg.add_reaction('<:3578_dewit:695735256631738419>')
        await msg.add_reaction('<:5480_PutinRages:695735613407887452>')


@bot.command()
async def quote(ctx, a: str = None, b: str = None):
    print("quote called")
    print("debug line one")
    serverid = ctx.guild.id
    print("debug line 2")
    doNotEmbedList = [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".webm", ".webp"]
    doEmbed = False
    noQuote = False
    if a is None:
        quoteToUse = qh.getRandomQuote(serverid)
        qtxt, qid, name, date = quoteToUse[0], quoteToUse[1], quoteToUse[2], quoteToUse[3]
    else:
        print("else")
        a = a.replace("#", "")
        if a.isdigit():
            print("quote cmd called with id: [" + a + "]")
            quoteToUse = qh.getQuoteById(a)
            if quoteToUse is None:
                noQuote = True
                outMsg = ("Quote not found dog")
            else:
                qtxt, qid, name, date = quoteToUse[0], a, quoteToUse[1], quoteToUse[2]
        elif a.startswith("del"):
            noQuote = True
            if b is not None:
                b = b.replace('#','')
            if b is None or not b.isdigit(): 
                print("user provided no delete value")
                outMsg = ("Provide a quote to delete!!")
            else:
                print("user wants to delete a quote: [" + b + "]")
                role = discord.utils.get(ctx.guild.roles, name="High Council of Emoji")
                isAdmin = False
                print("debug line dog")
                if role in ctx.message.author.roles:
                    isAdmin = True
                print("debug line cat")
                userid = ctx.message.author.id
                outMsg = qh.deleteQuote(isAdmin, b, str(userid))
        elif a == "list":
            noQuote = True
            outMsg = "https://bit.ly/renardquotes"
        else:
            noQuote = True
            outMsg = ("*Dobby relished his groinsaw's roar as he withdrew the flesh-choked blade from the astronaut's ruined skull. He turned to Harry, thrusting his bloody, retina-covered pelvis with elfin fervor. 'How does Ronnie Ron taste, master?'*")
    if not noQuote:
        doEmbed = True
        if len(qtxt) > 256:
                doEmbed = False
        for item in doNotEmbedList:
            if item in qtxt:
                doEmbed = False
        if not doEmbed:
            outMsg = ("\"" + qtxt + "\" | " + name + " | " + date[:16] + " | ID:" + str(qid))
        else:
            outMsg = discord.Embed(title=(qtxt.replace("\\n", "\n")), description=("Quote #" + str(qid) + " by " + name + " - " + date[:16]), color=0x800080)
    if doEmbed:
        await ctx.send(embed=outMsg)
    else:
        await ctx.send(outMsg)

@bot.command()
async def q(ctx):
    await quote.invoke(ctx)



@bot.command()
async def xfile(ctx):
    xfiletxt = "/home/ubuntu/disbot/xfile.txt"
    xfileline = open(xfiletxt).read().splitlines()
    xfileres = random.choice(xfileline)
    extractor = URLExtract()
    for url in extractor.gen_urls(str(xfileres)):
        await ctx.send("LOADING SECRET FILE...\n" + url)


@bot.command()
async def zoo(ctx):
        await ctx.send("HAVE YOU BEEN DRINKKIN DANIMAALLS...\n" + zooo())


# ------------------------------------------------- #
# web search utilities

gapi = "AIzaSyDse_e2vwSyvENfJiYM_oQNDOA06dR4a3g"
gsource = build("customsearch", 'v1', developerKey=gapi).cse()


@bot.command()
async def d(ctx):
    print("d called")
    meaning = getmeaning(ctx.message.content[3:])
    if meaning == "inv":
        print("got inv")
        delcmd = await ctx.send(file=File("/home/ubuntu/disbot/picfolder/archivememory.png"))
        deletelog[ctx.message.id] = delcmd
    else:    
        delcmd = await ctx.send(meaning)
        deletelog[ctx.message.id] = delcmd


@bot.command()
async def define(ctx):
    print("define called")
    meaning = getmeaning(ctx.message.content[8:])
    if meaning == "inv":
        print("got inv")
        delcmd = await ctx.send(file=File("/home/ubuntu/disbot/picfolder/archivememory.png"))
        deletelog[ctx.message.id] = delcmd
    else:    
        delcmd = await ctx.send(meaning)
        deletelog[ctx.message.id] = delcmd



@bot.command()
async def g(ctx):
    rawresult = gsource.list(q=ctx.message.content[3:],
                             cx='016515025707600383118:gqogcmpp7ka').execute()
    try:
        firstresult = rawresult['items'][0]
        gresult = firstresult['link']
        delcmd = await ctx.send(gresult)
        deletelog[ctx.message.id] = delcmd
    except KeyError:
        delcmd = await ctx.send("wtf no results? should have used bing...")
        deletelog[ctx.message.id] = delcmd
        

@bot.command()
async def gif(ctx, a: str = None, b: str = None):
    #TODO: upgrade to TenGiphPy
    # await ctx.send("this command is being upgraded, please be patient with jordan")
    reptilelist = ["lizard", "gecko", "reptile", "geico"]
    geckotriggers = ["lizard dance", "gecko dance", "cgi dancing lizard"]
    gifquery = ctx.message.content[5:]
    if b is not None:
        if (a.startswith("danc") and b in str(reptilelist)) or (b.startswith("danc") and a in str(reptilelist) or gifquery in str(geckotriggers)):
            await ctx.send(file=File("/home/ubuntu/disbot/picfolder/gecko_dance.gif"))
            return
    delcmd = await ctx.send(getgif(gifquery))
    deletelog[ctx.message.id] = delcmd


@bot.command()
async def how(ctx):
    howquery = ctx.message.content[5:]
    delcmd = await ctx.send(wikihow(howquery))
    deletelog[ctx.message.id] = delcmd


# # @bot.command()
# @bot.hybrid_command(name="hackimg", with_app_command=True, description="Gets first embeddable google image result.")
# async def hackimg(ctx: commands.Context, *, query):
#     imgquery = query
#     print(f"arg: [{query}]")
#     args = imgquery.split()
#     a = args[0]
#     if "spoil," == a or "spoiler," == a or "spoil" == a or "spoiler" == a:
#         delcmd = await ctx.send("||" + imageget(imgquery) + "||")
#         deletelog[ctx.message.id] = delcmd
#     else:
#         delcmd = await ctx.send(imageget(imgquery))
#         deletelog[ctx.message.id] = delcmd


@bot.command()
async def ing(ctx):
    await img.invoke(ctx)


@bot.command()
async def sky(ctx):
    print("sky called")
    url = "https://earthsky.org/tonight"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    skyhtml = urllib.request.urlopen(req)
    skysoup = BeautifulSoup(skyhtml.read(), 'html.parser')
    print("reqwuesrt succesful")
    image = skysoup.findAll("img", src=True)
    # print(skysoup)
    print(image[1])
    splitone = str(image[1]).split("src=")[1]
    splittwo = splitone.split(" ")[0]
    delcmd2 = await ctx.send(" \nhttps://earthsky.org/tonight")
    deletelog[ctx.message.id] = delcmd2
    delcmd = await ctx.send(splittwo.replace("\"", ""))
    deletelog[ctx.message.id] = delcmd



@bot.command()
async def spell(ctx):
    spellresult = gsource.list(q=ctx.message.content[7:],
                             cx='016515025707600383118:zzbf7g7bqty').execute()
    try:
        firstresult = spellresult['items'][0]
        spellresultfinal = firstresult['link']
        delcmd = await ctx.send(spellresultfinal)
        deletelog[ctx.message.id] = delcmd
    except KeyError:
        delcmd = await ctx.send("knowledge of that spell is forbidden...")
        deletelog[ctx.message.id] = delcmd
 
 
@bot.command()
async def ud(ctx):
    udrequest = ctx.message.content[4:]
    udurlfriendly = udrequest.replace(" ", "%20")
    udhtml = urllib.request.urlopen("https://www.urbandictionary.com/define.php?term="+udurlfriendly)
    udsoup = BeautifulSoup(udhtml.read(), 'html.parser')
    udmeaning = udsoup.findAll("div", "meaning")
    udresult = udmeaning[0].get_text().replace("\n","")
    delcmd = await ctx.send(udresult.replace("&apos", "'"))
    deletelog[ctx.message.id] = delcmd


@ud.error
async def ud_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        delcmd = await ctx.send("I CANT FIND THIS WORD SOMEBODY HELP ME")
        deletelog[ctx.message.id] = delcmd


@bot.command()
async def war(ctx, a: str = None, b: str = None):
    print("war were declared")
    userid = ctx.message.author.id
    authorfull = str(ctx.message.author)
    username = authorfull.split("#")[0]
    if a is None:
        battlenetcheckinit = renardusers(userid, "battlenet", serverid="uni")
        print("warzone reached users class")
        battlenetcheck = battlenetcheckinit.userread()
        print("battlenetcheck: [" + str(battlenetcheck) +"]")
        if battlenetcheck is None or battlenetcheck[0] is None:
            await ctx.send("No user found! Use \".war register battlenettagwithnumbersignandnumbers\"")
        else:
            battlenettag = battlenetcheck[0]
            numberlen = len(battlenettag.split("#")[1])
            print("battlecheck[0] was not None, continuing")
            if numberlen == 4 or numberlen == 5:
                platform = "battle"
            if numberlen == 7:
                platform = "uno"
            warzoneresponse = warzonestats(str(battlenetcheck[0]), platform)
    elif a == "register" or a == "reg":
        battlenetcheckinit = renardusers(userid, "battlenet", b, username, "uno")  
        print("warzone reached users class")
        battlenetcheckinit.userwrite()
        print("warzone wrote battlenet tag: [" + a + "]")
        await ctx.send("new gamertag stored")
    else:
        battlenettag = a
        numberlen = len(battlenettag.split("#")[1])
        if numberlen == 4 or numberlen == 5:
            platform = "battle"
        if numberlen == 7:
            platform = "uno"
            print("got uno")
        warzoneresponse = warzonestats(a, platform)
    if warzoneresponse == "inv":
        print("got inv")
        await ctx.send(file=File("/home/ubuntu/disbot/picfolder/archivememory.png"))
    else:
        if platform == "uno":
            platformfullurl = "atvi"
        else:
            platformfullurl = "battlenet"
        warstats = warzoneresponse.split("|")
        level = warstats[0]
        kills = warstats[1]
        deaths = warstats[2]
        suicides = warstats[3]
        ratio = warstats[4]
        wins = warstats[5]
        top5 = warstats[6]
        top10 = warstats[7]
        games = warstats[8]
        namebeforenumber = battlenettag.split("#")[0]
        numberaftername = battlenettag.split("#")[1]
        embed = discord.Embed(title = namebeforenumber + " Level " + level, 
                            description ="[more stats...](https://cod.tracker.gg/warzone/profile/" + platformfullurl + "/" + namebeforenumber + "%23" + numberaftername + "/overview)", 
                            color = 0x00badf)
        embed.set_thumbnail(url="https://i.insider.com/55a3e234eab8eab243028ac8?width=300&format=jpeg&auto=webp")
        embed.add_field(name="KILLS", value=kills)
        embed.add_field(name="DEATHS", value=deaths)
        embed.add_field(name="K/D", value=ratio)
        embed.add_field(name="WINS", value=wins + " (" + str(int(wins)*100/int(games))[:4] + "%)")
        embed.add_field(name="TOP 5", value=top5 + " (" + str(int(top5)*100/int(games))[:4] + "%)")
        embed.add_field(name="TOP 10", value=top10 + " (" + str(int(top10)*100/int(games))[:4] + "%)")
        embed.add_field(name="GAMES", value=games)
        await ctx.send(embed=embed)


@bot.command()
async def wiki(ctx):
    wikirequest = ctx.message.content[6:]
    wikiurlfriendly = wikirequest.replace(" ", "_")
    wikiq = wikipediaapi.Wikipedia('en')
    wikipage = wikiq.page(wikiurlfriendly)
    if not (wikipage.exists()):
        delcmd = await ctx.send("damn thats fucked up dude i dont see this page nowheres")
        deletelog[ctx.message.id] = delcmd
    else:
        delcmd = await ctx.send(wikipage.fullurl)
        deletelog[ctx.message.id] = delcmd


@bot.command()
async def yt(ctx):
    delcmd = await ctx.send(youtubesearch(ctx.message.content[4:]))
    deletelog[ctx.message.id] = delcmd

botkey = os.environ.get('DISCORDHACK')
bot.run(botkey, reconnect=True)