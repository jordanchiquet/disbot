#!/usr/bin/env python3


import asyncio
import codecs
import csv
import discord
import json
import os
import os.path
import nltk
nltk.download('brown')
import random
import re
import requests
import sys
import threading
import urllib.parse
import urllib.request
import wikipediaapi
from bs4 import BeautifulSoup
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
from datetime import datetime, timedelta
from discord import File
from discord.ext import commands, tasks
from googleapiclient.discovery import build
from google_images_download import google_images_download
from googlesearch import search
from nltk.corpus import brown
from urlextract import URLExtract
from uszipcode import SearchEngine


client = discord.Client()


bot = commands.Bot(command_prefix='.', case_insensitive=True, description='super computer robot')


bot.remove_command('help')


deletelog = {}


@tasks.loop(seconds=5.0)
async def timercheck():
    print("Timer check starting...")
    now = datetime.now()
    print(now)
    timerdata1 = open("/home/disbotren/discordtimers.csv", "rt")
    newtimerdata1 = open("/home/disbotren/discordtimers2.csv", "a", newline='')
    timereader = csv.reader(timerdata1, delimiter=",")
    timewriter = csv.writer(newtimerdata1)
    print("Opening CSV.")
    for row in timereader:
        channel = bot.get_channel(int(row[10]))
        print("Row read!")
        if now >= datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S.%f'):
            print("Timer pop! Attempting to send channel a message!")
            await channel.send("<@!" + row[1] + "> " + row[2] + " (" + row[3] + " " + row[4] + " " + row[5] + " " +
                               row[6] + " ago) | Timer ID: " + row[0])
        if now < datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S.%f'):
            timewriter.writerow(row)
    timerdata1.close()
    newtimerdata1.close()
    os.system('rm /home/disbotren/discordtimers.csv')
    os.system('mv /home/disbotren/discordtimers2.csv /home/disbotren/discordtimers.csv')
    print("Timer check closing.")


@bot.event
async def on_ready():
    timercheck.start()
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
        await channel.send(file=File("/home/disbotren/icwhatumeanfolder/icwhatumeanfile" + str(icwhatumeanfile) + ".png"))
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
    if "print time" == mclower:
        await channel.send(datetime.now())
    if "promotion" in mclower:
        await channel.send(file=File("/home/disbotren/promotions.jpg"))
    if "same sex" in mclower:
        await channel.send(file=File("/home/disbotren/dmx.png"))
    if "what is your purpose" in mclower:
        await channel.send(
            "My purposes are input, output, processing, and storage.")
    if "bye" in mclower:
        min = 1
        max = 9
        signfile = random.randint(min, max)
        await channel.send(file=File("/home/disbotren/byebyefolder/byebye" + str(signfile) + ".png"))
    if "your sign" in mclower:
        min = 1
        max = 9
        signfile = random.randint(min, max)
        await channel.send(file=File("/home/disbotren/heresyoursignfolder/heresyoursign" + str(signfile) + ".png"))
    if mclower.endswith("this bitch"):
        word = mclower.split(" ")[-3]
        print(word)
        checkword = nltk.FreqDist(t for w, t in brown.tagged_words() if w.lower() == word)
        checkwordres = checkword.most_common()
        if "VB" in str(checkwordres):
            min = 1
            max = 32
            bitchfile = random.randint(min, max)
            await channel.send(file=File("/home/disbotren/bitchfolder/bitchfile" + str(bitchfile) + ".png"))
    if mclower.endswith("on this bitch"):
        await channel.send(file=File("/home/disbotren/bitchfolder/bitchfile" + str(bitchfile) + ".png"))
    if mclower.endswith("this, bitch"):
        min = 1
        max = 32
        bitchfile = random.randint(min, max)
        await channel.send(file=File("/home/disbotren/bitchfolder/bitchfile" + str(bitchfile) + ".png"))
    if "what is a" in mclower:
        query = "define:" + mclower.split("what is a ")[1]
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            await channel.send(j)
    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '💬' and not user.bot:
        message = reaction.message
        channel = reaction.message.channel
        ts = message.created_at
        with open("/home/disbotren/discordquote.csv", "r") as f:
            quotecvs = f.readlines()
            quoteid = quotecvs[-1].split(',')[0]
            newid = (int(quoteid) + 1)
            fields = [newid, ts, message.author, message.content]
            with open("/home/disbotren/discordquote.csv", "a") as f:
                quotewriter = csv.writer(f)
                quotewriter.writerow(fields)
        await channel.send('{} added quote '.format(user.name) + str(newid))
        f.close()


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
async def timerdebug(ctx):
    print("Timer check starting...")
    now = datetime.now()
    print(now)
    timerdata1 = open("/home/disbotren/discordtimers.csv", "rt")
    newtimerdata1 = open("/home/disbotren/discordtimers2.csv", "a", newline='')
    timereader = csv.reader(timerdata1, delimiter=",")
    timewriter = csv.writer(newtimerdata1)
    print("Opening CSV.")
    for row in timereader:
        print("Found a row!")
        channel = row[10]
        if now >= datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S.%f'):
            print("Timer pop! Attempting to send channel a message!")
            await channel.send("<@!" + row[1] + "> " + row[2] + " (" + row[3] + " " + row[4] + " " + row[5] + " " +
                               row[6] + " ago) | Timer ID: " + row[0])
        if now < datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S.%f'):
            timewriter.writerow(row)
    timerdata1.close()
    newtimerdata1.close()
    os.system('rm /home/disbotren/discordtimers.csv')
    os.system('mv /home/disbotren/discordtimers2.csv /home/disbotren/discordtimers.csv')
    print("Timer check closing.")


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
        variable = [
            "You do not have the clearance for that command... are you retarded?",
            "You aren't a server admin... this is why she left you dude.",
            "Try that shit again and see who gets terminated bitch ;)",
            "It seems like there's a lot you don't know about terminating this bot",
        ]
        await ctx.send(random.choice(variable))
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
        variable = [
            "You do not have the clearance for that command... are you retarded?",
            "You aren't a rebooter... this is why she left you dude.",
            "Try that shit again and see who gets rebooted bitch ;)",
            "It seems like there's a lot you don't know about rebooting this pi",
        ]
        await ctx.send(random.choice(variable))
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
@bot.command()
async def timer(ctx, a: str = None, b: str = None, c: str = None, d: str = None):
    alower = a.lower()
    channel = ctx.channel.id
    timeorig = ctx.message.created_at - timedelta(hours=6)
    user = ctx.message.author.id
    if a == "del" or a == "delete":
        delid = b
        if delid == "1":
            await ctx.send ("Timer 1 is a permanent timer to simplify programmatic looping. You can ask Jordan if you want to know more.")
            return
        else:
            timerdata = open("/home/disbotren/discordtimers.csv", "rt")
            newtimerdata = open("/home/disbotren/discordtimers1.csv", "a", newline='')
            reader = csv.reader(timerdata, delimiter=",")
            writer = csv.writer(newtimerdata)
            for row in reader:
                if delid != row[0]:
                    writer.writerow(row)
            timerdata.close()
            newtimerdata.close()
            os.system('rm /home/disbotren/discordtimers.csv')
            os.system('mv /home/disbotren/discordtimers1.csv /home/disbotren/discordtimers.csv')
            await ctx.send("Timer #" + delid + " deleted.")
            return
    if a == "list":
        await ctx.send(file=File("/home/disbotren/discordtimers.csv"))
        return
    if (alower.startswith("jan") or
    alower.startswith("feb") or
    alower.startswith("mar") or
    alower.startswith("apr") or
    alower.startswith("may") or
    alower.startswith("jun") or
    alower.startswith("jul") or
    alower.startswith("aug") or
    alower.startswith("sep") or
    alower.startswith("oct") or
    alower.startswith("nov") or
    alower.startswith("dec")):

        if alower.startswith("jan"):
            month = "01"
        if alower.startswith("feb"):
            month = "02"
        if alower.startswith("mar"):
            month = "03"
        if alower.startswith("apr"):
            month = "04"
        if alower.startswith("may"):
            month = "05"
        if alower.startswith("jun"):
            month = "06"
        if alower.startswith("jul"):
            month = "07"
        if alower.startswith("aug"):
            month = "08"
        if alower.startswith("sep"):
            month = "09"
        if alower.startswith("oct"):
            month = "10"
        if alower.startswith("nov"):
            month = "11"
        if alower.startswith("dec"):
            month = "12"
        
        print(month)
        print(datetime.now().month)
        print(":oooooo:")
        testdate = (datetime.now().year + 1)
        print(testdate)

        
        

        if len(b) < 2:
            b = "0" + b
            print(b)
        if c is None:
            c = ""
            print("C was none")
        if int(month) < datetime.now().month:
            print("month should be next year")
            popyear = (datetime.now().year + 1)
            print(popyear)
        if int(month) >= datetime.now().month:
            print("month is this year")
            popyear = datetime.now().year
            print(popyear)
        
        timepop = str(popyear) + "-" + month + "-" + b + " 10:20:00.000000"
        print("-----\n" + timepop + "\n-----")

        with open("/home/disbotren/discordtimers.csv", "r") as f:        
            timercsv = f.readlines()
            oldid = timercsv[-1].split(',')[0]
            timerid = (int(oldid) + 1)
            timeval1raw = "ph"
            unit1 = datetime.now().date
            timeval2raw = "ph"
            unit2 = "ph"
            timeval = "ph"
            print("i made it this far")
            fields = [timerid, user, c, timeval1raw, datetime.now().date, timeval2raw, unit2,
                     timeorig, timeval, timepop, channel]
            print("fields was concatenatedsedes")
            with open("/home/disbotren/discordtimers.csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
            print("line was written with date timer reminder timer reminding time :)")
        f.close()
    else:
        timeval1raw = int(a)
        unit1 = b.lower()
        msgcontent = ctx.message.content

        if unit1.startswith("m"):
            timeval1 = timeval1raw
        if unit1.startswith("h"):
            timeval1 = timeval1raw * 60
        if unit1.startswith("d"):
            timeval1 = timeval1raw * 1440
        if unit1.startswith("w"):
            timeval1 = timeval1raw * 10080
        if unit1.startswith("y"):
            timeval1 = timeval1raw * 525600

        if c is not None:
            if c.isdigit():
                timeval2raw = int(c)
                unit2 = d.lower()
                timernote = msgcontent.split(d)[1]
                if unit2.startswith("m"):
                    timeval2 = timeval2raw
                if unit2.startswith("h"):
                    timeval2 = timeval2raw * 60
                if unit2.startswith("d"):
                    timeval2 = timeval2raw * 1440
                if unit2.startswith("w"):
                    timeval2 = timeval2raw * 10080
                if unit2.startswith("y"):
                    timeval2 = timeval2raw * 525600

            if not c.isdigit():
                timeval2 = 0
                timeval2raw = ""
                unit2 = ""
                timernote = msgcontent.split(b)[1]

        if c is None:
            timeval2 = 0
            timeval2raw = ""
            unit2 = ""
            timernote = ""

        timeval = timeval1 + timeval2

 ` `

        await ctx.send("Timer set! | ID: " + str(timerid))
        if timeval1raw > 60:
            await ctx.send("btw do you think it's funny to use these big stupid fucking numbers?")


@bot.command()
async def reminder(ctx):
    await timer.invoke(ctx)


# @timer.error
# async def timer_error(ctx, error):
#    if isinstance(error, commands.CommandInvokeError):
#        await ctx.send("you fucked that up somehow, format is \".timer 11 min kid cuisine in oven\" ")


@bot.command()
async def todo(ctx):
    user = str(ctx.message.author.id)
    task = ctx.message.content[6:]
    taskwritetime = datetime.now()
    todolistfile = ('/home/disbotren/todo/' + user + ".csv")
    if os.path.isfile(todolistfile):
        with open(todolistfile, "r") as todoread:
            todolist = todoread.readlines()
            oldid = todolist[-1].split(',')[0]
            todoid = (int(oldid) + 1)
            fields = [todoid, task, taskwritetime]
            with open(todolist, "a", newline='') as todoappend:
                writer = csv.writer(todoappend)
                writer.writerow(fields)
        todoread.close()
        todoappend.close()
    else:
        with open(todolistfile, 'wb') as newtodo:
            fields = ["1", task, taskwritetime]
            writer = csv.writer(newtodo, delimiter=',')
            writer.writerow(fields)
        todolistfile.close()


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
async def roll(ctx, a):
    msg = ctx.message.content
    mult = int(a[0])
    if "+" in msg:
        numsplit1 = a.split("+")[0]
        numsplit2 = a.split("+")[1]
        d = int(numsplit1[2:])
        print(numsplit2)
        print(d)
    if "+" not in msg:
        d = int(a[2:])
        numsplit2 = 0
    min = 1
    max = d
    reslist = []
    for x in range(mult):
        res = random.randint(min, max)
        reslist.append(res)
        pass
    rollsum = sum(reslist)
    addsum = rollsum + int(numsplit2)
    if numsplit2 == 0:
        await ctx.send(str(addsum) + " " + str(reslist))
    else:
        await ctx.send(str(addsum) + " " + str(reslist) + " + " + numsplit2)
    reslist.clear()


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
        "https://youtu.be/_O89Y0VwdPs \n ICE COLD COORS LIGHT STRAIGHT FROM THE ROCKY MOUNTAINS",
        "the champagne of beers",
        "Miller time....",
        "PBR"
        ""
    )
    expensive = (
        "Squatters"
     )
    await ctx.send(random.choice(cheap))


@bot.command()
async def eat(ctx):
    any = (
        "Albasha",
        "Bay Leaf",
        "City Pork",
        "Curbside",
        "Curry N Kabob",
        "Duang Tuan",
        "El Rancho",
        "Elsie's",
        "Fat Cow",
        "La Caretta",
        "Lit",
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
    await ctx.send("https://youtu.be/asXfA40uudo")


@bot.command()
async def qp(ctx):
    msg = ctx.message
    print(msg.content)
    await msg.add_reaction('<:Jeff:601576645807046656>')
    await msg.add_reaction('<:What:370701344232701952>')


@bot.command()
async def quote(ctx, a: str = None, b: str = None):
    col = 3
    qlist = []
    if a is None:
        with open("/home/disbotren/discordquote.csv", "r") as f:
            quotereader = csv.reader(f)
            data = [(row[col-1], row[col], row[col-2], row[col-3]) for row in quotereader]
            result = (random.choice(data))
            name = result[0]
            qtxt = result[1]
            date = result[2]
            qid = result[3]
            if len(qtxt) > 256:
                await ctx.send("\"" + qtxt + "\" | " + name + " | " + date + " | ID:" + qid)
                return
            else:
                embed = discord.Embed(title=qtxt, description=("Quote #" + qid + " by " + name + " - " + date), color=0x800080)
                await ctx.send(embed=embed)
    if a.isdigit():
        with open("/home/disbotren/discordquote.csv", "rt") as f:
            quotereader = csv.reader(f, delimiter=",")
            found = False
            for row in quotereader:
                if a == row[0]:
                    found = True
                    if len(str(row[3])) > 256:
                        await ctx.send("\"" + row[3] + "\" | " + row[2] + " | " + row[1] + " | ID:" + row[0])
                        return
                    else:
                        embed = discord.Embed(title=row[3], description=("Quote #" + row[0] + " by " + row[2] + " - " + row[1]),
                                              color=0x800080)
                        await ctx.send(embed=embed)
            if not found:
                await ctx.send("Quote not found dog")
    if a == "del":
        with open("/home/disbotren/discordquote.csv", "rt") as f, open("/home/disbotren/discordquote1.csv", "a", newline='') as out:
            quotereader = csv.reader(f, delimiter=",")
            quotewriter = csv.writer(out)
            found = False
            for row in quotereader:
                if b == row[0]:
                    found = True
                if b != row[0]:
                    quotewriter.writerow(row)
        os.system('rm /home/disbotren/discordquote.csv')
        os.system('mv /home/disbotren/discordquote1.csv /home/disbotren/discordquote.csv')
        if found:
            await ctx.send("Quote removed.")
        if not found:
            await ctx.send("How can you delete that which is... dead?")
    if a == "list":
        await ctx.send(file=File("/home/disbotren/discordquote.csv"))
    if a is not None and not a.isdigit() and a != "del" and a != "list" :
        qlist = []
        with open("/home/disbotren/discordquote.csv", "rt") as f:
            quotereader = csv.reader(f, delimiter=",")
            found = False
            for row in quotereader:
                if a in row:
                    found = True
                    qlist.append(row)
            if not found:
                await ctx.send("No results, make sure you include the whole account with identifier. Search is case sensitive.")
        qran = random.choice(qlist)
        if len(str(qran[3])) > 256:
            await ctx.send("\"" + qran[3] + "\" | " + qran[2] + " | " + qran[1] + " | ID:" + qran[0])
            return
        else:
            embed = discord.Embed(title=qran[3], description=("Quote #" + qran[0] + " by " + qran[2] + " - " +
                                                              qran[1]),color=0x800080)
            await ctx.send(embed=embed)
        qlist.clear()
        
    f.close()


@bot.command()
async def q(ctx):
    await quote.invoke(ctx)


@bot.command()
async def xfile(ctx):
    xfiletxt = "/home/disbotren/xfile.txt"
    xfileline = open(xfiletxt).read().splitlines()
    xfileres = random.choice(xfileline)
    extractor = URLExtract()
    for url in extractor.gen_urls(str(xfileres)):
        await ctx.send("LOADING SECRET FILE...\n" + url)


@bot.command()
async def zoo(ctx):
    zootxt = "/home/disbotren/zoo.txt"
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
    drequest = ctx.message.content[3:]
    durlfriendly = drequest.replace(" ", "%20")
    dhtml = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/"+durlfriendly)
    dsoup = BeautifulSoup(dhtml.read(), 'html.parser')
    dmeaning = dsoup.findAll("meta")
    delcmd = await ctx.send(dmeaning + "\nhttps://www.merriam-webster.com/dictionary/"+durlfriendly)
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
async def gif(ctx):
    imgquery = ctx.message.content[5:]
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":imgquery,"limit":1,"no_download":True,"format":"gif"}
    imgresult = response.download(arguments)
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
    rawresult = gsource.list(q=ctx.message.content[5:], searchType='image',
                             cx='016515025707600383118:gqogcmpp7ka').execute()
    try:
        firstresult = rawresult['items'][0]
        imgresult = firstresult['link']
        delcmd = await ctx.send(imgresult)
        deletelog[ctx.message.id] = delcmd
    except KeyError:
        delcmd = await ctx.send("how you say? not any image find for that image")
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
    user = ctx.message.author
    if a == "set":
        with open("/home/disbotren/weatherloc.csv", 'rt') as f, open("/home/disbotren/weatherloc1.csv", "a", newline='') as out:
            reader = csv.reader(f, delimiter=",")
            writer = csv.writer(out)
            for row in reader:
                if str(user) not in row:
                    writer.writerow(row)
            zippo = b
            wfields = [user, zippo]
            writer.writerow(wfields)
        os.system('rm /home/disbotren/weatherloc.csv')
        os.system('mv /home/disbotren/weatherloc1.csv /home/disbotren/weatherloc.csv')
        await ctx.send("Location set!")
        f.close()
        out.close()
    if a is None:
        try:
            with open("/home/disbotren/weatherloc.csv", 'rt') as f:
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


bot.run("NTk4OTI0ODQ5MDU4MDIxMzkz.XVNA9g.zDqCySYZRc9Xmxg9aMFXoTNhVzA", reconnect=True)
