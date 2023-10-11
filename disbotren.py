#!/usr/bin/env python3

#TODO: setup hook embed message
#TODO: encrypt/hash sql pw and api keys
#TODO: pip dependency update script for venv parity 
#TODO: biden I did that command using overlay


#API DISCORDREN

versionstr = "v2.0.0"


import datetime
import discord #discord
import os, os.path
import random
import re
import requests
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from discord import File
from discord.ext import commands, tasks
import numexpr as ne
from urlextract import URLExtract #urlextract

# import modules.feedreader as fr
import modules.serverset as serv
from modules.commandHandler import cmdHandlerWebQueries as queryCmd
from modules.dice import dice as diceroller
from modules.piltools.dickshadow import executeoverlay #Pillow #numpy #whapi
from modules.figlet import figgletizer 
from modules.goatse import goatse
from modules import quoteshandler as qh
from modules.onmessagetools import onMessageMain
from modules.randomhelpers import genErrorHandle
from modules.timertools import timerExpiryCheck, timerNotify, timerWriter
from modules.timertools.expiryExclaims import exclaimList
from modules.webquerytools.wikipediasearch import wikipediaSearch
from modules.zooo import zooo

intents = discord.Intents().default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        # intents.members = True
        super().__init__(command_prefix = ".", case_insensitive=True, intents=intents)
    
    async def setup_hook(self):
        print(f"starting setup_hook for {self.user}.")
        await load()
        await self.tree.sync()
        print("tree sync complete.")
    
    async def on_ready(self):
        timercheck.start()
        # feedcheck.start()
        channel_bot_testing = bot.get_channel(600430089519497235)
        await channel_bot_testing.send(content="renard online")

        

bot = Bot()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')



renardgenchannel = bot.get_channel(649528092691529749)

deletelog = {}
commandRunningDict = {}
chatLog = []
now = datetime.now() - timedelta(hours=5)
jordan_id = 191688156427321344


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
        print('starting process cmd on message edit')
        await bot.process_commands(after)

@tasks.loop(seconds=300.0)
async def commandRunningDictClear():
    print("clearing commandRunningDict (dict for belay order shit)")
    commandRunningDict.clear()
    chatLog.clear()

@bot.command()
async def cyberwar(ctx, a, b: str = None):
    if ctx.author.id == jordan_id:
        print("got jordan")
        if b == "fire":
            if a == "open":
                cyberWarfareLoop.start(ctx.channel.id)
            elif a == "cease":
                print("got to cease")
                cyberWarfareLoop.stop()
    else:
        await ctx.send("did you really think that would work")

@bot.command()
async def todo(ctx):
    if ctx.author.id == jordan_id:
        with open("todo.txt", 'a') as f:
            f.write("\n- " + ctx.message.content[6:])
            f.close()
        outMsg = "appended"
    else:
        outMsg = "🤖"
    await ctx.send(outMsg)

@tasks.loop(seconds=5.0)
async def cyberWarfareLoop(cyberwarchannelid: int = None):
    print("cyberwarfare engaged")
    freaxchannel = bot.get_channel(cyberwarchannelid)
    await freaxchannel.send(goatse)

@bot.check
async def channel_not_poll(ctx):
    print("starting channel_not_poll check")
    if ctx.channel.id == 1041861487876132885:
        print("channel was poll chan")
        return ctx.command.qualified_name == "poll"
    else:
        print("channel not poll chan")
        return True

@bot.event
async def on_member_update(before, after):
    print("detected presence update")
    if before.nick != after.nick:
        print("nick counter arrive line 1")
        try:
            print("nick changed for user " + str(before.id) + " from " + before.nick + " to " + after.nick)
        except:
            print("user " + str(before.id) + " changed name from one there's no record of to " + after.nick)
        # nickcounterinit = wordcounter(before.id, before.guild.id, after.nick, nicktally=True)
        # nickcounterinit.countprocessor()

msgCache = {} #blank dict for coupling ids with message content

@bot.event
async def on_message(message):
    if message.author == bot.user:
        commandRunningDict[message.id] = message.content
        print("bot command logged")
        return
    else:
        chatLog.append(message.content)
    serverid = message.guild.id
    channelid = message.channel.id

    userid = message.author.id
    if channelid == 1041861487876132885 and not message.author == bot.user:
        await message.delete()
    authorfull = str(message.author)
    username = authorfull.split("#")[0]
    channel = message.channel
    print(message.author)
    user = (str(message.author)).split("#")[0]
    timeorig = (message.created_at - timedelta(hours=5))
    mclower = message.content.lower()
    onMessageInit = onMessageMain.onMessageHandler(serverid, channelid, userid, username, timeorig, mclower)
    onMessageResult = onMessageInit.messageHandleMain()
    if onMessageResult[0] != None:
        if onMessageResult[0] == "text":
            print("onMessageResult got text and sending: [" + onMessageResult[1] + "] to channel")
            await channel.send(onMessageResult[1])
        elif onMessageResult[0] == "file":
            await channel.send(file=File(onMessageResult[1]))

    if len(chatLog) >= 3: 
        if chatLog[-1] == chatLog[-2] and chatLog[-2] == chatLog[-3]:
            await channel.send(chatLog[-2])
            chatLog.clear()

    if len(chatLog) >= 3: 
        if chatLog[-1] == chatLog[-2] and chatLog[-2] == chatLog[-3]:
            await channel.send(chatLog[-2])
            chatLog.clear()
    if not mclower.startswith(".") and ("belay that order" in mclower or "cancel that order" in mclower or "cancel that command" in mclower or "delete that timer" in mclower
     or "cancel that timer" in mclower or "erase that timer" in mclower):
        print("belay that in command, checking commandRunning Dict")
        if  commandRunningDict != []:
            print("dict is not empty")
            deletionID = [*commandRunningDict.keys()][-1]
            print("made it to first key acquire")
            msgObj = await channel.fetch_message(deletionID)
            commandMsgStr = commandRunningDict[deletionID]
            print(commandMsgStr)
            if "Timer set for " in commandMsgStr:
                print("timer detected in command")
                authorRegCheck = re.search("[a-zA-Z]+#[0-9]{4}", commandMsgStr)
                if authorRegCheck.group() == str(message.author):
                    print("belay order call was made by timer author")
                    deltable = "timers"
                else:
                    await channel.send("I cannot do that sir, the timer is DNA-locked by Commander " + authorRegCheck.group() + ".")
                    return
            elif commandRunningDict[deletionID].startswith("Quote ") and " added by " in commandRunningDict[deletionID]:
                print("quotes detected in command")
                deltable = "quotes"
            else:
                await msgObj.delete()
                await channel.send("TRANSPHASIC PAYLOAD DROPPED... MESSAGE OBLITERATED")
                return
            await msgObj.delete()
            await channel.send("LAUNCHING " + deltable[:-1].upper() + " TORPEDOES")
        else:
            print("nothing to belay..")
            await channel.send("Nothing to belay Sir.")
    await bot.process_commands(message)

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
    reeactionuserstr = (str(user)).split("#")[0]
    msgOut = None
    if reaction.emoji == '💬' and not user.bot:
        print("speech bubble called")
        quoteAddResult = qh.addQuote(user=msguserstr, quoteStr=messageContent, timestamp=str(ts),
        serverid=serverid, userid=messageuserid)
        quoteId = str(quoteAddResult[1])
        if quoteAddResult[0]:
            msgOut = ("Quote " + quoteId + " added by " + reeactionuserstr + ".")
        else: 
            msgOut = (reeactionuserstr + " tried to add a quote that is already in as " + quoteId + ".")   
    elif (reaction.emoji == Gib or reaction.emoji == '✋') and messageuser.bot:
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

@bot.event
async def on_reaction_remove(reaction, user):
    Gib = bot.get_emoji(410972413036331008)
    message = reaction.message
    channel = reaction.message.channel
    messageuser = message.author
    messageuserid = messageuser.id
    reactuser = user
    reactionuserid = user.id
    messageContent = message.content   
    outMsg = None
    ts = message.created_at - timedelta(hours=5)
    if reaction.emoji == '💬' and not user.bot:
        qh.deleteQuoteByTime(str(ts))
        outMsg = ("Quote erased from the archive memory :).")
    elif reaction.emoji == Gib:
        removeInit = timerNotify.timerNotify(str(reactionuserid), messageContent)
        timerid = removeInit.removeNotifyUser()
        outMsg = str(reactuser) + " removed from timer " + timerid + " notify list!"
    if outMsg is not None:
        await channel.send(outMsg)


@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound) and "..." not in ctx.message.content:
            print("command not found")

@bot.hybrid_command(name="ping", with_app_command=True, description="Gets latency in ms between Discord server and bot's instance on AWS.")
async def ping(ctx):
    pong = str(bot.latency * 1000)
    await ctx.send("pong!! " + pong[:2] + " ms")

@bot.command()
async def version(ctx):
    embed = discord.Embed(title="disbotren.py", description="Gaming forever in paradise [.help]", color=0xee657)
    embed.add_field(name="Version", value=versionstr)
    embed.add_field(name="Release Notes", value="https://pastebin.com/P63XbH2b")
    await ctx.send(embed=embed)

@bot.hybrid_command(name="notifyme", with_app_command=True, description="Toggles whether you are on the @ mention list for notifications about bot updates and downtime.")
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

## Tasks ##

# @tasks.loop(minutes=0.5)
# async def feedcheck():
#     try:
#         print("feedcheck started")
#         resultArray = fr.feedCheckAll()
#         newLine = "\n"
#         if len(resultArray) > 0:
#             print(f"results in feedcheck:[{newLine.join(resultArray)}]")
#             for result in resultArray:
#                 resultSplit = result.split('|')
#                 link, serverid, chanid, override = resultSplit[0], resultSplit[1], int(resultSplit[2]), resultSplit[3]
#                 print(f"link:[{link}] serverid:[{serverid}] chanid:[{chanid}] override:[{override}]")
#                 if override == "0":
#                     checkForChannel = serv.getServerSetting(serverid, 'botspamchannel')
#                     if checkForChannel:
#                         chanid = checkForChannel
#                 outChannel = bot.get_channel(chanid)
#                 await outChannel.send(link)
#     except Exception as e:
#         genErrorHandle(e)
#         pass
            

@tasks.loop(seconds=5.0)
async def timercheck():
    print(str(datetime.now()) + " timercheck started")
    checked = timerExpiryCheck.expiryCheck()
    print("timerCheck got expiryCheck")
    if len(checked) > 1:
        print("timerCheck got checked longer than 1 char")
        notifyChannel = bot.get_channel(int(checked[1]))
        print("timerCheck got notifyChannel: [" + str(notifyChannel) + "]")
        notifyUser = checked[2]
        print("timerCheck got notifyUser: [" + notifyUser + "]")
        expiryTime = " | " + (checked[3])[:-10] + " "
        print("timerCheck got expiryTimer: [" + expiryTime + "]")
        expiryNote = checked[4]
        print("timerCheck got expiryNote: [" + expiryNote + "]")
        if expiryNote == "":
            exclaim = str(random.choice(exclaimList))
            notifyMessage = (notifyUser + exclaim + expiryTime)
        else:
            notifyMessage = (notifyUser + expiryNote + expiryTime)
        print("timerCheck outgoing notifyMessage: [" + notifyMessage + "]")
        await notifyChannel.send(notifyMessage)
    else:
        return

@bot.hybrid_command(name="timer", with_app_command=True, description="Set a timer using format '2 h 3 m pizza in oven' or '12/21/2012 2:00 pm pizza party'")
async def timer(ctx: commands.Context, *, timerdetails):
    timerInit = timerWriter.timerWriter(ctx.author.id, ctx.channel.id, ".timer " + timerdetails)
    args = timerdetails.split()
    if args[0] is None:
        messageOut = "https://iknowwhatyoudownload.com/en/peer/"
    else:
        messageOutTup = timerInit.timerWriterMain()
        if type(messageOutTup) is str:
            messageOut = messageOutTup
        else:
            messageOut = messageOutTup[1]
    await ctx.send(messageOut)

@bot.hybrid_command(name="reminder", with_app_command=True, description="See '/timer'")
async def reminder(ctx: commands.Context, *, timerdetails):
    await ctx.invoke(bot.get_command('timer'), timerdetails = timerdetails)

@bot.hybrid_command(name="calculator", with_app_command=True, description="Evaluates an expression (no variables).")
async def calculator(ctx, *, expression):
    res = str(ne.evaluate(expression))
    print("here")
    mathembed = discord.Embed(title=res, description=expression, color=discord.Colour.yellow())
    await ctx.send(embed=mathembed)

@bot.hybrid_command(name="roll", with_app_command=True, description="Roll the dice. e.g. '1d20' or '2d6+3'. appending 'adv' or 'dis' applies advantage or disadv.")
async def roll(ctx: commands.Context, *, dice):
    args = dice.split()
    a, b, c, d, e = args[0], args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None, args[3] if len(args) > 3 else None, args[4] if len(args) > 4 else None


    print("dice initiated")
    if b is None or not b[0].isdigit():
        print("dice is one roll, with or without adv")
        rollinit0 = diceroller(a, b)
        print("made it here")
        if a.startswith("ab"):
            rollresult = rollinit0.abilityroller()
        else:
            rollresult = rollinit0.roller()
    elif a.startswith("ab"):
        rollinit0 = diceroller(a,b)
        rollresult = rollinit0.abilityroller()
    else:
        rollinit0 = diceroller(a)
        print("rollinit0 has launched")
        rollinit1 = diceroller(b)
        print("rollinit1 has launched")
        rollresult = rollinit0.roller() + "\n" + rollinit1.roller()
        if c is not None:
            rollinit2 = diceroller(c)
            print("rollinit2 has launched")
            rollresult = rollresult + "\n" + rollinit2.roller()
        if d is not None:
            rollinit3 = diceroller(d)
            print("rollinit3 has launched")
            rollresult = rollresult + "\n" + rollinit3.roller()
        if e is not None:
            rollinit4 = diceroller(e)
            print("rollinit4 launched")
            rollresult = rollresult + "\n" + rollinit4.roller()
    print("rollresult: [" + rollresult + "]")
    rollembed = discord.Embed(title=rollresult, description=dice, color=discord.Colour.dark_red())
    await ctx.send(embed=rollembed)

@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("That's not how I roll brother...")

@bot.hybrid_command(name="cat", with_app_command=True, description="Gets random picture of cat(s)")
async def cat(ctx):
    catr = requests.get('http://aws.random.cat/meow')
    catf = str(catr.json()['file'])
    await ctx.send(catf)

@bot.hybrid_command(name="coin", with_app_command=True, description="Flips logandollar")
async def coin(ctx):
    coinflip = ("Heads", "Tails")
    await ctx.send(random.choice(coinflip))

@bot.hybrid_command(name="conch", with_app_command=True, description="Consult the conch on a closed (yes/no) question.")
async def conch(ctx):
    path, dirs, files = os.walk("/home/ubuntu/disbot/picfolder/conchfolder").__next__()
    min = 1
    max = len(files)
    conchfile = random.randint(min, max)
    destiny = random.choice(("Yes", "No"))
    file = discord.File(fp = f"/home/ubuntu/disbot/picfolder/conchfolder/conch{conchfile}.png", filename="conch.png")
    embed = discord.Embed(title=destiny, description="", color=discord.Colour.dark_magenta())
    embed.set_image(url="attachment://conch.png")
    delcmd = await ctx.send(file=file, embed=embed)
    deletelog[ctx.message.id] = delcmd

@bot.hybrid_command(name="dog", with_app_command=True, description="Gets random picture of dog(s)")
async def dog(ctx):
    dogr = requests.get('https://dog.ceo/api/breeds/image/random')
    dogf = str(dogr.json()['message'])
    await ctx.send(dogf)

@bot.hybrid_command(name="enhance", with_app_command=True, description="Enhance last image in the chat - 20 message cache.")
async def enhance(ctx):
    msg = ctx.message
    channel = ctx.channel
    history = channel.history
    print(f"channel:{channel}")
    haveimg = False
    bgtitle = "/home/ubuntu/disbot/picfolder/shadowdir/providedbackground.png"
    if os.path.isfile(bgtitle):
        os.remove(bgtitle)
    if not msg.attachments and not msg.embeds:
        print("enhance message did not have an attachment")
        async for message in ctx.channel.history(limit=20):
            print("iterating history")
            if message.attachments:
                print("attempting to save attachment...")
                await message.attachments[0].save(bgtitle)
                haveimg = True
                break
            elif message.embeds:
                print(f'message.embeds: {message.embeds}')
                if message.embeds[0].type == "image":
                    print("attempting to save embed...")
                    print(message.embeds[0].url)
                    urllib.request.urlretrieve(message.embeds[0].url, bgtitle)
                    haveimg = True
                    break
                elif message.embeds[0].image:
                    print("attempting to save image within embed...")
                    urllib.request.urlretrieve(message.embeds[0].image.url, bgtitle)
                    haveimg = True
                    break
            else:
                continue
    else:
        print("enhance message had one or more attachments")
        haveimg = True
        await ctx.message.attachments[0].save(bgtitle)
    if haveimg:
        newfilepath = executeoverlay(bgtitle)
        if newfilepath == "inv":
            await ctx.send("sum ting wong...")
        else:
            await ctx.send(file=File(newfilepath))
            os.remove(bgtitle)
            os.remove(newfilepath)
    else:
        await ctx.send("Could not find an image to enhance...")

@bot.hybrid_command(name="figlet", with_app_command=True, description="Turns input into giant bubble letters.")
async def figlet(ctx, *, figgletext):
    await ctx.send("```" + figgletizer(figgletext) + "```")

@bot.hybrid_command(name="gun", with_app_command=True, description="Threatening react images for your various needs")
async def gun(ctx):
    path, dirs, files = os.walk("/home/ubuntu/disbot/picfolder/bitchfolder").__next__()
    min = 1
    max = len(files)
    bitchfile = random.randint(min, max)
    await ctx.send(file=File("/home/ubuntu/disbot/picfolder/bitchfolder/bitchfile" + str(bitchfile) + ".png"))

@bot.hybrid_command(name="loon", with_app_command=True, description="Never know when you might need one of these")
async def loon(ctx):
    await ctx.send("https://youtu.be/asXfA40uudo")

@bot.hybrid_command(name="poll", with_app_command=True, description="Start a poll; delimit items in 'options' with commas.")
async def poll(ctx, question, options: str):
    options = options.split(',')
    if len(options) <= 1:
        await ctx.send("Poll requires at least two options.")
        return
    if len(options) > 10:
        await ctx.send("I can't fucking count that high")
    if len(options) == 2 and options[0].lower() == 'yes' and options[1].replace(" ","").lower() == 'no':
        reactions = ['✅', '❌']
    else:
        reactions = ['🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯']
    polloptions = []
    for x, option in enumerate(options):
        polloptions += f'\n{reactions[x]} {option[1:] if option.startswith(" ") else option}'
    embed = discord.Embed(title=question, description=''.join(polloptions))
    outmessage = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await outmessage.add_reaction(reaction)
    await ctx.start

@bot.command()
async def qp(ctx):
    msg = ctx.message
    print(msg.content)
    if ctx.guild.id == 237397384676507651:
        await msg.add_reaction('<:Jeff:601576645807046656>')
        await msg.add_reaction('<:What:370701344232701952>')
    else:
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')


@bot.hybrid_command(name="quote", with_app_command=True, description="Call quote from server. Optionally specify a specific number. Optionally enter 'yes' for delete.")
async def quote(ctx, id: str = None, delete: str = None):
    serverid = ctx.guild.id
    doNotEmbedList = [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".webm", ".webp"]
    doEmbed = False
    noQuote = False
    if id is None:
        quoteToUse = qh.getRandomQuote(serverid)
        qtxt, qid, name, date = quoteToUse[0], quoteToUse[1], quoteToUse[2], quoteToUse[3]
    else:
        print("else")
        id = id.replace("#", "")
        if id.isdigit():
            print("quote cmd called with id: [" + id + "]")
            quoteToUse = qh.getQuoteById(id)
            if quoteToUse is None:
                noQuote = True
                outMsg = ("Quote not found dog")
            else:
                qtxt, qid, name, date = quoteToUse[0], id, quoteToUse[1], quoteToUse[2]
        if delete is not None:
            delete = delete.lower()
            if  delete == 'yes' or delete == "true" or delete.startswith('del'):
                noQuote = True
                if id is not None:
                    id = id.replace('#','')
                if id is None or not id.isdigit(): 
                    print("user provided no delete value")
                    outMsg = ("Provide a quote to delete!!")
                else:
                    print("user wants to delete a quote: [" + id + "]")
                    role = discord.utils.get(ctx.guild.roles, name="High Council of Emoji")
                    isAdmin = False
                    print("debug line dog")
                    if role in ctx.message.author.roles:
                        isAdmin = True
                    print("debug line cat")
                    userid = ctx.message.author.id
                    outMsg = qh.deleteQuote(isAdmin, id, str(userid))
        if id == "list":
            noQuote = True
            outMsg = "https://bit.ly/renardquotes"
        if not id.isdigit() and id != "list":
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

@bot.hybrid_command(name="xfile", with_app_command=True, description="Get random lore from the archive")
async def xfile(ctx):
    xfiletxt = "/home/ubuntu/disbot/xfile.txt"
    xfileline = open(xfiletxt).read().splitlines()
    xfileres = random.choice(xfileline)
    extractor = URLExtract()
    for url in extractor.gen_urls(str(xfileres)):
        await ctx.send("LOADING SECRET FILE...\n" + url)

@bot.hybrid_command(name="zoo", with_app_command=True, description="Get an animal from a list I made of ones I like")
async def zoo(ctx):
        await ctx.send(zooo())

@bot.hybrid_command(name="define", with_app_command=True, description="Get definition for term(s) from Merriam-Webster")
async def define(ctx: commands.Context, *, term):
    print("define called")
    delcmd = await ctx.send(f"**{term.upper()}**\n" + queryCmd("d", term))
    deletelog[ctx.message.id] = delcmd

@bot.command()
async def d(ctx):
    await define.invoke(ctx)

@bot.hybrid_command(name="g", with_app_command=True, description="First result from google.com")
async def g(ctx, *, query):
    delcmd = await ctx.send(queryCmd("g", query) + f"\n[{query}]")
    deletelog[ctx.message.id] = delcmd
        
@bot.hybrid_command(name="gif", with_app_command=True, description="Gets gif; uses Tenor")
async def gif(ctx, *, query):
    gifembed = discord.Embed(title='', description=query, color=discord.Colour.dark_orange())
    gifembed.set_image(url = queryCmd("gif", query))
    delcmd = await ctx.send(embed=gifembed)
    deletelog[ctx.message.id] = delcmd

@bot.hybrid_command(name="how", with_app_command=True, description="Searches wikihow with whatver you enter")
async def how(ctx, *, query):
    howquery = ctx.message.content[5:]
    howResult = queryCmd("how", query)
    delcmd = await ctx.send(queryCmd("how", query) + f"\n[{query}]")
    deletelog[ctx.message.id] = delcmd

@bot.hybrid_command(name="img", with_app_command=True, description="Gets first embeddable google image result.")
async def img(ctx: commands.Context, *, query):
    print(f"img command arg: [{query}]")

    imgembedlink = queryCmd("img", query)
    
    if "sorry" in imgembedlink:
        delcmd = await ctx.send(imgembedlink)
    else:
        imgembed = discord.Embed(title ='', description=query, color=discord.Colour.dark_orange())
        imgembed.set_image(url = imgembedlink)
        delcmd = await ctx.send(embed=imgembed)
    deletelog[ctx.message.id] = delcmd

@bot.hybrid_command(name="dalle", with_app_command=True, description="Get AI generated image with DALLE2")
async def dalle(ctx, *, prompt):
    await ctx.defer(ephemeral=False)
    dalle_embed=discord.Embed(title='', description='', color=discord.Colour.dark_teal())
    url = queryCmd("dalle", prompt)
    if url.startswith("error"):
        if "\n" in url:
            dalle_embed.title = url.splitlines()[0]
            dalle_embed.description = "\n".join(url.splitlines()[2:-1])
        else:
            dalle_embed.title = url.split("|")[0]
            dalle_embed.description = url.split("|")[1]

    else:
        dalle_embed.title = prompt
        dalle_embed.set_image(url = queryCmd("dalle", prompt))
    await ctx.send(embed=dalle_embed)


@bot.hybrid_command(name="stablediffusion", with_app_command=True, description="Get AI generated image with Stable Diffusion (WIP)")
async def stablediffusion(ctx, *, prompt):
    await ctx.defer(ephemeral=False)
    stablediff_embed=discord.Embed(title='', description='', color=discord.Colour.dark_teal())
    url = queryCmd("stablediffusion", prompt)
    if url.startswith("error"):
        await ctx.send(url)
    else:
        file = discord.File(fp="stablediffresult.png", filename="stablediffresult.png")
        # await ctx.send(file=file)
        stablediff_embed.title = prompt
        stablediff_embed.set_image(url="attachment://stablediffresult.png")
        await ctx.send(file=file, embed=stablediff_embed)
        os.remove("stablediffresult.png")

@bot.command()
async def ing(ctx):
    await img.invoke(ctx)

@bot.hybrid_command(name="ud", with_app_command=True, description="Gets first Urban Dictionary definition.")
async def ud(ctx, *, query):
    delcmd = await ctx.send(f"**{query.upper()}**\n" + queryCmd("ud", query))
    deletelog[ctx.message.id] = delcmd

@bot.hybrid_command(name="wiki", with_app_command=True, description="Search wikipedia")
async def wiki(ctx, *, query):
    wikiresult = wikipediaSearch(query)
    if wikiresult[0] == 0:
        delcmd = await ctx.send(wikiresult[1].url)
    elif wikiresult[0] == 1:
        delcmd = await ctx.send(wikipediaSearch(wikiresult[1][0])[1].url)
    if wikiresult[0] == 2:
        delcmd = await ctx.send(f"no result for {query}")

    deletelog[ctx.message.id] = delcmd

@bot.hybrid_command(name="yt", with_app_command=True, description="Gets first youtube result (for an anonymous user)")
async def yt(ctx, *, query):
    delcmd = await ctx.send(queryCmd("yt", query) + f"\n[{query}]")
    deletelog[ctx.message.id] = delcmd



botkey = os.environ.get('DISCORDREN')
bot.run(botkey, reconnect=True)