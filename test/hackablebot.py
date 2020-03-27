#!/usr/bin/env python3


testroot = "Users/jordanchiquet/personalandfinance/disbotren/test"


import asyncio
import codecs
import csv
import datetime
import discord
import json
import logging
import os
import mysql.connector
import nltk
import random
import re
import requests
import ssl
import sys
import threading
import urllib.parse
import urllib.request
import wikipediaapi #wikipedia-api
from bs4 import BeautifulSoup
from darksky.api import DarkSky, DarkSkyAsync #darksky_weather
from darksky.types import languages, units, weather
from datetime import datetime, timedelta
from discord import File
from discord.ext import commands, tasks
from googleapiclient.discovery import build #google-api-python-client
from google_images_download import google_images_download
# from GoogleScraper import scrape_with_config, GoogleSearchError
from googlesearch import search #google
from nltk.corpus import brown
from urlextract import URLExtract
from uszipcode import SearchEngine

from modules.bingimageapi import bingimage
from modules.timermod.timercl import timercl
from modules.timermod.timeparser import timeparser
from modules.renardusers import renardusers
from modules.dice import dice
from modules.definitionwebscrape import getdefinition
# from modules.googleimageapi import bingimage
from modules.heycomputer import heycomputer
# from modules.timer.timermonthpass import timermonthpass
# from test.modules.timer.ogtimer import ogtimer
# from test.modules.timer.timer import timercl


nltk.download('brown')

client = discord.Client()

bot = commands.Bot(command_prefix=(',', 'jizz '), case_insensitive=True, description='super computer robot')

bot.remove_command('help')

deletelog = {}

@bot.event
async def on_ready():
    # timercheck.start()
    print("logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print(bot.latency)
    print("-----------------------------------")
    channel = bot.get_channel(600430089519497235)
    embed = discord.Embed(title="Computer Online Mode:", description=" [ON] OFF ", color=0xee657)
    await channel.send(embed=embed)


# ----------------- On Message----------------- #
@bot.event
async def on_message_delete(message):
    if message.id in deletelog:
        dellog = deletelog[message.id]
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


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    channel = message.channel
    mclower = message.content.lower()
    if mclower.startswith("hey") or mclower.startswith("hi") or mclower.startswith("hello") or mclower.startswith("hola"):
        mclowersplit = mclower.split(" ")
        if mclowersplit[1].startswith("comput") or mclowersplit[1] == ("compadre") or mclowersplit[1] == "machine" or mclowersplit[1] == "renard":
            heycomputerinit = heycomputer(mclower)
            heycomputeresult = heycomputerinit.heycomputerexecute()
            print("heycomputeresult: [" + heycomputeresult + "]")
            if heycomputeresult == "inv" or heycomputeresult is None:
                await channel.send("a mistake was made... the computer have processed your message but could not... process")
            else:
                if heycomputeresult[0] == "~":
                    heycomputeresult = "```" + heycomputeresult[1:] + "```"
                await channel.send(heycomputeresult)
        else:
            return
    if mclower.startswith("comput") or mclower.startswith("compadre") or mclower.startswith("machine") or mclower.startswith("renard"):
        heycomputerinit = heycomputer(mclower)
        heycomputeresult = heycomputerinit.heycomputerexecute()
        print("heycomputeresult: [" + heycomputeresult + "]")
        if heycomputeresult == "inv" or heycomputeresult is None:
            await channel.send("a mistake was made... the computer have processed your message but could not... process")
        else:
            if heycomputeresult[0] == "~":
                heycomputeresult = "```" + heycomputeresult[1:] + "```"
            await channel.send(heycomputeresult)
    if "bad bot" in mclower:
        await channel.send(
        "dang...")
    if "give me a hand" in mclower:
        await channel.send(
        "https://pbs.twimg.com/media/C3YEwBBXUAE3EoQ.jpg")
    if "good bot" == mclower:
        await channel.send(
        "thanks")
    if "holy fuck" == mclower:
        await channel.send(
        "Wi Tu Lo")
    if "i get up" == mclower:
        await channel.send(
        "https://www.youtube.com/watch?v=qjm9QZT06ig")
    if "i see what you mean" in mclower:
        min = 1
        max = 5
        icwhatumeanfile = random.randint(min, max)
        await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/test/icwhatumeanfolder/icwhatumeanfile" + str(icwhatumeanfile) + ".png"))
    if "love" == mclower:
        await channel.send(
            "is suicide")
    if ("love you" in mclower or
    "love andrew" in mclower or
    "love frank" in mclower or
    "love joey" in mclower or
    "love jordan" in mclower or
    "love logan" in mclower or
    "love seth" in mclower or
    "love trev" in mclower or
    "love tgras" in mclower or
    "miss you" in mclower):
        await channel.send(
            "haha gay!")
    if "meant to be" in mclower:
        await channel.send(
            "https://www.facebook.com/magicmenlive/videos/magic-men"
            "-live-florida-georgia-line-meant-to-be/2147632005458542/")
    if "remind me in" in mclower:
        timertxt = mclower.split("remind me in ")[1]
        timervars = timertxt.split(" ")
        a = timervars[0]
        b = timervars[1]
        c = timervars[2]
        d = timervars[4]
        await timer(message, a, b, c, d)

    if "print time" == mclower:
        await channel.send(datetime.now())
    if "promotion" in mclower:
        await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/promotions.jpg"))
    if "what is your purpose" in mclower:
        await channel.send(
            "My purposes are input, output, processing, and storage.")
    if "bye" in mclower:
        min = 1
        max = 9
        signfile = random.randint(min, max)
        await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/byebyefolder/byebye" + str(signfile) + ".png"))
    if "your sign" in mclower:
        min = 1
        max = 9
        signfile = random.randint(min, max)
        await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/heresyoursignfolder/heresyoursign" + str(signfile) + ".png"))
    if mclower.endswith("this bitch"):
        word = mclower.split(" ")[-3]
        print(word)
        checkword = nltk.FreqDist(t for w, t in brown.tagged_words() if w.lower() == word)
        checkwordres = checkword.most_common()
        if "VB" in str(checkwordres):
            min = 1
            max = 32
            bitchfile = random.randint(min, max)
            await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/bitchfolder/bitchfile" + str(bitchfile) + ".png"))
    if mclower.endswith("on this bitch"):
        await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/bitchfolder/bitchfile" + str(bitchfile) + ".png"))
    if mclower.endswith("this, bitch"):
        min = 1
        max = 32
        bitchfile = random.randint(min, max)
        await channel.send(file=File("/Users/jordanchiquet/personalandfinance/disbotren/test/bitchfolder/bitchfile" + str(bitchfile) + ".png"))
    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    mydb = mysql.connector.connect(
    host='18.216.39.250',
    user='dbuser',
    passwd='e4miqtng')
    mycursor = mydb.cursor(buffered=True)
    Gib = bot.get_emoji(410972413036331008)
    if reaction.emoji == '💬' and not user.bot:
        message = reaction.message
        channel = reaction.message.channel
        ts = message.created_at - timedelta(hours=5)
        messageuser = message.author
        quote = message.content
        sql = "INSERT INTO renarddb.quotes (user, quote, timestamp) VALUES (\"" + str(messageuser) + "\", \"" + str(quote) + "\", \"" + str(ts) + "\");"
        mycursor.execute(sql)
        mydb.commit()
        idquery = "SELECT id FROM renarddb.quotes WHERE timestamp = \"" + str(ts) + "\""
        mycursor.execute(idquery)
        for x in mycursor:
            await channel.send ("Quote " + str(x[0]) + " added by " + str(user) + ".")
    elif reaction.emoji == Gib:
        message = reaction.message
        ts = message.created_at - timedelta(hours=5)
        print(str(ts))
        print(str(user.id))
        gibsql = "SELECT id FROM renarddb.timers WHERE timeorig = \"" + str(ts) + "\""
        mycursor.execute(gibsql)
        for x in mycursor:
            print(str(x))
            checknotifysql = "SELECT extratags FROM renarddb.timers WHERE id = " + str(x[0]) 
            mycursor.execute(checknotifysql)
            for y in mycursor:
                if y[0] is None:
                    print("y[0] is none")
                    addnotifysql = "UPDATE renarddb.timers SET extratags = \"" + str(user.id) + "|\" WHERE id = " + str(x[0])
                    mycursor.execute(addnotifysql)
                    mydb.commit()
                    return    
                else:
                    addnotifysql = "UPDATE renarddb.timers SET extratags = \"" + y[0] + str(user.id) + "|\" WHERE id = " + str(x[0])
                    mycursor.execute(addnotifysql)
                    mydb.commit()
                    return
        else:
            print("no timer to add user notify on gib react")
            return


@bot.event
async def on_reaction_remove(reaction, user):
    mydb = mysql.connector.connect(
    host='18.216.39.250',
    user='dbuser',
    passwd='e4miqtng')
    mycursor = mydb.cursor(buffered=True)
    Gib = bot.get_emoji(410972413036331008)
    if reaction.emoji == '💬' and not user.bot:
        message = reaction.message
        channel = reaction.message.channel
        ts = message.created_at - timedelta(hours=5)
        print("user wants to delete a quote by removing their reaction")
        delsql = "DELETE FROM renarddb.quotes WHERE timestamp = \"" + str(ts) + "\""
        mycursor.execute(delsql)
        mydb.commit()
        await channel.send("Quote erased from the archive memory :).")
    elif reaction.emoji == Gib:
        message = reaction.message
        ts = message.created_at - timedelta(hours=5)
        channel = reaction.message.channel
        delgibsql = "DELETE FROM renarddb.timers WHERE timeorig = \"" + str(ts) + "\""
        mycursor.execute(delgibsql)
        mydb.commit()


@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound) and "..." not in ctx.message.content:
            print("command not found")


# ----------------- Commands ----------------- #
# ---------------------------------------- #
# admin and debug shit
@bot.command()
async def feedback(ctx):
    fdbackmsg = ctx.message.content[10:]
    admin = ctx.message.guild.owner
    await discord.DMChannel.send(admin, fdbackmsg)
    await ctx.send("feedback sent to creator")


@bot.command()
async def chanid(ctx):
    await ctx.send(ctx.channel.id)


@bot.command()
async def datetest(ctx):
    await ctx.send("datetime.now(): " + datetime.now() + "\n" + 
                    "datetime.now().date: " + datetime.now().date)

@bot.command()
async def fb(ctx):
    fdbackmsg = ctx.message.content[3:]
    admin = ctx.message.guild.owner
    await discord.DMChannel.send(admin, fdbackmsg)
    await ctx.send("feedback sent to creator")


@bot.command()
async def mtn(ctx):
    await ctx.send("this is a test mention message, <@!" + str(ctx.message.author.id) + ">")


@bot.command()
async def ping(ctx):
    pong = str(bot.latency * 1000)
    await ctx.send("pong!! " + pong[:2] + " ms")


@bot.command()
async def ding(ctx):
    dong = str(bot.latency * 1000)
    await ctx.send("dong!! " + dong[:2] + " ms")


@bot.command()
async def strcheck(ctx):
    print("strcheck: " + ctx.message.content[10:])
    await ctx.send("```" + ctx.message.content[10:] + "```")


@bot.command()
async def timerdebug(ctx):
    timercheckinit = timercl("msgcontent", "user", "channel", "timeorig")
    response = timercheckinit.timercheck()
    if response == "no timepops":
        return
    else:
        channel = bot.get_channel(int(response[3]))
        if response[2] == "":
            await channel.send("<@!" + response[1] + "> Ringa ling dong, the time " + (response[4])[:-3] + " has finally come!")
        else:
            await channel.send("<@!" + response[1] + "> Sir you must remember: \"" + response[2] + "\" | " + (response[4])[:-3])

@bot.command()
@commands.has_role("High Council of Emoji")
async def close(ctx):
    await ctx.send("Personal PC Computer plugging off online mode shut down - COMPUTER OFF")
    print("terminate request received")
    await client.close()
    await sys.exit()


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


@bot.command()
@commands.has_role("rebooter")
async def reboot(ctx):
    embed = discord.Embed(title="Computer Online Mode:", description=" ON [OFF] ", color=0xff0000)
    await ctx.send(embed=embed)
    print("terminate request received")
    os.system ('echo e4miqtng | sudo systemctl restart disbotren.service')


@bot.command()
@commands.has_role("rebooter")
async def piboot(ctx):
    embed = discord.Embed(title="Computer Online Mode:", description=" ON [OFF] ", color=0xff0000)
    await ctx.send(embed=embed)
    print("terminate request received")
    os.system ('echo e4miqtng | sudo -S reboot')


@reboot.error
async def reboot_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        username = ctx.message.author.display_name
        userid = ctx.message.author.id
        now = datetime.now()
        response = [
            "You do not have the clearance for that command... are you retarded?",
            "You aren't a rebooter... this is why she left you dude.",
            "Try that shit again and see who gets rebooted bitch ;)",
            "It seems like there's a lot you don't know about rebooting this pi",
        ]
        await ctx.send(random.choice(response))
        print(now + " insufficient perms to reboot " + username + " " + str(userid))


# ---------------------------------------- #
# documentation
@bot.command()
async def help(ctx):
    await ctx.send("List of commands: https://pastebin.com/dBDALLSX")


@bot.command()
async def vers(ctx):
    embed = discord.Embed(title="ROBORENARD MK I", description="Gaming forever in paradise", color=0xee657)
    embed.add_field(name="Version", value="0.81111cum")
    await ctx.send(embed=embed)


# ------------------------------------------- #
# practical functions

@tasks.loop(seconds=5.0)
async def timercheck():
    timercheckinit = timercl("msgcontent", "user", "channel", "timeorig")
    response = timercheckinit.timercheck()
    if response is None:
        return
    else:
        print("made it to timercheck else")
        print(response[3])
        channel = bot.get_channel(int(response[3]))
        if response[4] is None:
            if response[2] == "":
                await channel.send("<@!" + response[1] + "> Ringa ling dong, the time " + (response[5])[:19] + " has finally come!")
            else:
                await channel.send("<@!" + response[1] + "> Sir you must remember: \"" + response[2] + "\" | " + (response[5])[:-3])
        else:
            notifylist = response[4].split("|")
            if response[2] == "":
                await channel.send("<@!" + response[1] + "> Ringa ling dong, the time " + (response[5])[:19] + " has finally come!")
            else:
                await channel.send("<@!" + response[1] + "> Sir you must remember: \"" + response[2] + "\" | " + (response[5])[:-3])
            for x in notifylist[:-1]:
                await channel.send("<@!" + x + ">,  you too have been notified!")


@bot.command()
async def timer(ctx, a: str = None, b: str = None, c: str = None, d: str = None):
    channel = ctx.channel.id
    msgcontent = ctx.message.content
    timeorig = (ctx.message.created_at - timedelta(hours=5))
    # timeorig = (datetime.now())
    user = ctx.message.author.id
    timerinit = timercl(msgcontent, user, channel, timeorig, a, b, c, d)
    if a == "default":
        if b == None:
            await ctx.send("Use \".timer default 07:00\" to set your default time for calendar reminders")
        else:
            print("user attempting to write default time")
            timeparseinit = timeparser(b, c)
            writetime = timeparseinit.gettime()
            if writetime == "inv":
                await ctx.send("jordan timeparse returned that time invalid")
            else:
                print("this is writetime after sending from default write: [" + str(writetime) + "]")
                timerinit = timercl(msgcontent, user, channel, timeorig, a, writetime, c, d)
                timerinit.timerdefaultwrite()
                await ctx.send("New default time for your calendar reminders written.")
    else:
        response = await timerinit.timerfunc()
        if response == "user requested list":
            await ctx.send("list in development")
        else:
            await ctx.send(response)


# ------------------------------------------------ #
# random math
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@bot.command()
async def div(ctx, a: int, b: int):
    await ctx.send(a / b)


@bot.command()
async def mul(ctx, a: int, b: int):
    await ctx.send(a * b)


@bot.command()
async def roll(ctx, a, b: str = None):
    rollinit = dice(a, b)
    await ctx.send(rollinit.roller())


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
    conchimg = (
        "https://i.ytimg.com/vi/WAzGNbuu3LU/maxresdefault.jpg",
        "https://pbs.twimg.com/profile_images/416370357743144960/xIpWXsBH.jpeg",
        "http://i.imgur.com/b2IAcwY.jpg",
        "https://i.ytimg.com/vi/-S6VvSoeeP4/maxresdefault.jpg",
        "https://i.etsystatic.com/15079744/r/il/e26c07/1255333255/il_794xN.1255333255_epc0.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSyMXvA_Fxw_YfwtNGDdbP3YzW9TgYIHPQyNTQNaW7OTI3pEl-")
    destiny = ("Yes", "No")
    await ctx.send(random.choice(conchimg))
    await ctx.send(random.choice(destiny))


@bot.command()
async def dog(ctx):
    dogr = requests.get('https://dog.ceo/api/breeds/image/random')
    dogf = str(dogr.json()['message'])
    await ctx.send(dogf)


@bot.command()
async def drink(ctx):
    cheap = (
        "Bud Light",
        "Budweiser",
        "https://youtu.be/_O89Y0VwdPs\n ICE COLD COORS LIGHT STRAIGHT FROM THE ROCKY MOUNTAINS",
        "the champagne of beers",
        "Miller time....",
        "PBR"
        ""
    )
    # expensive = (
    #     "Squatters"
    #  )
    await ctx.send(random.choice(cheap))


@bot.command()
async def eat(ctx):
    any = (
        "Albasha",
        "Bay Leaf",
        "City Pork",
        "Curbside",
        "Curry and Kabob",
        "Duang Tuan",
        "El Rancho",
        "Elsie's",
        "Fat Cow",
        "La Caretta",
        "Pluckers",
        "Serops",
        "Superior Grill",
        "Sushi Masa",
        "Tsunami",
        "Umami",
        "Velvet Cactus"
    )
    await ctx.send(random.choice(any))


@bot.command()
async def fox(ctx):
    foxr = requests.get('https://randomfox.ca/floof/')
    foxf = str(foxr.json()['image'])
    await ctx.send(foxf)


@bot.command()
async def loon(ctx):
    await ctx.send("https://www.youtube.com/watch?v=asXfA40uudo")


@bot.command()
async def qp(ctx):
    msg = ctx.message
    print(msg.content)
    await msg.add_reaction('<:Jeff:601576645807046656>')
    await msg.add_reaction('<:What:370701344232701952>')


@bot.command()
async def quote(ctx, a: str = None, b: str = None):
    mydb = mysql.connector.connect(
    host='18.216.39.250',
    user='dbuser',
    passwd='e4miqtng')
    mycursor = mydb.cursor(buffered=True)
    if a is None:
        qlist = []
        sql = "SELECT * FROM renarddb.quotes"
        mycursor.execute(sql)
        for x in mycursor:
            qlist.append(x)
        quoteunparsed = random.choice(qlist)
        print("made randome choice: [" + str(quoteunparsed) + "]")
        qid = quoteunparsed[0]
        name = quoteunparsed[1]
        qtxt = quoteunparsed[2]
        date = quoteunparsed[3]
        if len(qtxt) > 256:
            await ctx.send("\"" + qtxt + "\" | " + name + " | " + date[:16] + " | ID:" + str(qid))
            return
        else:
            embed = discord.Embed(title=qtxt, description=("Quote #" + str(qid) + " by " + name + " - " + date[:16]), color=0x800080)
            await ctx.send(embed=embed)
        qlist.clear()
    
    if a.isdigit():
        print("a was digit in quote cmd, user looking for specific quote")
        sql = "SELECT id, user, quote, timestamp FROM renarddb.quotes WHERE id LIKE " + a
        mycursor.execute(sql)
        x = None
        for x in mycursor:
            result = x
            print("resultstr: [" + str(result) + "]")
            qid = result[0]
            name = result[1]
            qtxt = result[2]
            date = result[3]
            if len(qtxt) > 256:
                await ctx.send("\"" + qtxt + "\" | " + name + " | " + date[:16] + " | ID:" + str(qid))
                return
            else:
                embed = discord.Embed(title=qtxt, description=("Quote #" + str(qid) + " by " + name + " - " + date[:16]), color=0x800080)
                await ctx.send(embed=embed)
        if x is None:
            await ctx.send("quote not found dog")
    
    if a == "del":
        print("user wants to delete a quote: [" + a + "]")
        sql = "SELECT * FROM renarddb.quotes WHERE id LIKE " + a
        mycursor.execute(sql)
        for x in mycursor:
            delsql = "DELETE FROM renarddb.quotes WHERE id LIKE " + a 
            mycursor.execute(delsql)
            mydb.commit()
            await ctx.send("Quote " + a + "erased from the archive memory :).")
        else:
            await ctx.send("WTF i can't FUCKING find that one!?!?!?!?!")
    
    if a == "list":
        await ctx.send("list in development >_<")


@bot.command()
async def q(ctx):
    await quote.invoke(ctx)


@bot.command()
async def xfile(ctx):
    xfiletxt = "/Users/jordanchiquet/personalandfinance/disbotren/test/xfile.txt"
    xfileline = open(xfiletxt).read().splitlines()
    xfileres = random.choice(xfileline)
    extractor = URLExtract()
    for url in extractor.gen_urls(str(xfileres)):
        await ctx.send("LOADING SECRET FILE...\n" + url)


@bot.command()
async def zoo(ctx):
    zootxt = "/Users/jordanchiquet/personalandfinance/disbotren/test/zoo.txt"
    zooline = open(zootxt).read().splitlines()
    zoores = random.choice(zooline)
    extractor = URLExtract()
    for url in extractor.gen_urls(str(zoores)):
        await ctx.send("HAVE YOU BEEN DRINKKIN DANIMAALLS...\n" + url)


# ------------------------------------------------- #
# web search utilities

gapi = "AIzaSyDse_e2vwSyvENfJiYM_oQNDOA06dR4a3g"
gsource = build("customsearch", 'v1', developerKey=gapi).cse()


@bot.command()
async def d(ctx):
    print("d called")
    meaning = getdefinition(ctx.message.content[3:])
    delcmd = await ctx.send("```" + meaning + "```")
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
async def gifold(ctx):
    imgquery = ctx.message.content[5:]
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":imgquery,"limit":1,"no_download":True,"format":"gif"}
    imgresult = response.download(arguments)
    print("gifresult: [" + str(imgresult) + "]")
    if "[]" in str(imgresult):
        delcmd = await ctx.send("Sorry player... gif is none")
        deletelog[ctx.message.id] = delcmd
    extractor = URLExtract()
    for url in extractor.gen_urls(str(imgresult)):
        if "fbsbx" in url:
            delcmd = await ctx.send(url)
            deletelog[ctx.message.id] = delcmd
        else:
            embeddableurl = url.split("?")[0]
            delcmd = await ctx.send(embeddableurl)
            deletelog[ctx.message.id] = delcmd


@bot.command()
async def img(ctx):
    imgquery = ctx.message.content[5:]
    delcmd = await ctx.send(bingimage(imgquery))
    deletelog[ctx.message.id] = delcmd


@bot.command()
async def imgtwo(ctx):
    rawresult = gsource.list(q=ctx.message.content[8:], searchType='image',
                            cx='016515025707600383118:gqogcmpp7ka').execute()
    try:
        firstresult = rawresult['items'][1]
        imgresult = firstresult['link']
        delcmd = await ctx.send(imgresult)
        deletelog[ctx.message.id] = delcmd
    except KeyError:
        delcmd = await ctx.send("how you say? not any image find for that image")
        deletelog[ctx.message.id] = delcmd

@bot.command()
async def imgold(ctx):
    imgquery = ctx.message.content[8:]
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":imgquery,"limit":1,"no_download":True}
    imgresult = response.download(arguments)
    extractor = URLExtract()
    if "[]" in str(imgresult):
        delcmd = await ctx.send("how you say? not any image find for that image")
        deletelog[ctx.message.id] = delcmd
    for url in extractor.gen_urls(str(imgresult)):
        delcmd = await ctx.send(url)
        deletelog[ctx.message.id] = delcmd


@bot.command()
async def ing(ctx):
    await img.invoke(ctx)


@bot.command()
async def rev(ctx):
    await ctx.send("Working on it...")
    revquery = ctx.message.attachments[0].url
    response = google_images_download.googleimagesdownload()
    arguments = {"similar_images": revquery,"limit":1,"no_download":True}
    revresult = response.download(arguments)
    extractor = URLExtract()
    for url in extractor.gen_urls(str(revresult)):
        await ctx.send("Found this:\n" + url)
 
 
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
async def w(ctx, a: str = None, b: str = None):
    userid = ctx.message.author.id
    if a == "set" and b.isdigit():
        zipwriteinit = renardusers(userid, "zip", str(b))

    if a is None:
        try:
            with open("/Users/jordanchiquet/personalandfinance/disbotren/test/weatherloc.csv", 'rt') as f:
                for line in f:
                    if str(user) in line:
                        zipparse = line.split(',')
                        zipp = zipparse[1]
                        zipsearch = SearchEngine(simple_zipcode=True)
                        zipres = zipsearch.by_zipcode(int(zipp))
                        citystatename = zipres.post_office_city
                        wlat = zipres.lat
                        wlng = zipres.lng
                        darksky = DarkSky("7d2873772103272916b9cc1e357b6331")
                        wbase = darksky.get_forecast(wlat, wlng, extend=False, lang=languages.ENGLISH, units=units.US,
                                                        exclude=[weather.MINUTELY, weather.ALERTS])
                        wsum = wbase.currently.summary
                        wtemp = str(wbase.currently.temperature)[:2]
                        wfeel = str(wbase.currently.apparent_temperature)[:2]
                        wfore = wbase.daily.summary
                        print(str(wbase.currently.temperature)[:2])
                        print(wbase.daily.summary)
                        embed = discord.Embed(title=citystatename, description=wsum + ", "+ wtemp + "\n" +
                                              "Feels like: " + wfeel, color=0x800080)
                        embed.add_field(name="Forecast:", value=wfore)
                        await ctx.send(embed=embed)
            f.close()
        except:
            await ctx.send("provide a zip code to get weather for or use \".w set [zipcode]\" to register one for"
                           "your username.")
    elif a.isdigit():
        try:
            zipsearch = SearchEngine(simple_zipcode=True)
            zipres = zipsearch.by_zipcode(int(a))
            citystatename = zipres.post_office_city
            wlat = zipres.lat
            wlng = zipres.lng
            darksky = DarkSky("7d2873772103272916b9cc1e357b6331")
            wbase = darksky.get_forecast(wlat, wlng, extend=False, lang=languages.ENGLISH, units=units.US,
                                         exclude=[weather.MINUTELY, weather.ALERTS])
            wsum = wbase.currently.summary
            wtemp = str(wbase.currently.temperature)[:2]
            wfeel = str(wbase.currently.apparent_temperature)[:2]
            wfore = wbase.daily.summary
            print(str(wbase.currently.temperature)[:2])
            print(wbase.daily.summary)
            embed = discord.Embed(title=citystatename, description=wsum + ", " + wtemp + "\n" +
                                                                   "Feels like: " + wfeel, color=0x800080)
            embed.add_field(name="Forecast:", value=wfore)
            await ctx.send(embed=embed)
        except:
            await ctx.send("dude wtf... I can't find zip code \"" + a + "\". Maybe it was erased from the archive memory.")

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
    ytquery = urllib.parse.urlencode({"search_query" : ctx.message.content[4:]})
    html_cont = urllib.request.urlopen("http://youtube.com/results?"+ytquery)
    ytresult = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
    delcmd = await ctx.send("https://youtu.be/" + ytresult[0])
    deletelog[ctx.message.id] = delcmd


bot.run("NjA4MDgwMDYzMDE5MzUyMDg0.XfAB8w.ZlM1cYDxkMiHrElbQ3GjAt3IFk4", reconnect=True)
