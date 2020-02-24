from datetime import datetime, timedelta
from modules.timermod.dateslashparser import dateslashparser
from modules.timermod.timermonthpass import timermonthpass
from modules.timermod.ogtimer import ogtimer
from modules.timermod.timeparser import timeparser
# from test.modules.timer.dateslashparser import dateslashparser
# from test.modules.timer.timermonthpass import timermonthpass
# from test.modules.timer.ogtimer import ogtimer


import csv
import os


class timercl:
    def __init__(self, msgcontent, user, channel, timeorig, a: str = None, b: str = None, c: str = None, d: str = None):
        self.msgcontent = msgcontent
        self.user = user
        self.channel = channel
        self.timeorig = timeorig
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    async def timerfunc(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        alower = a.lower()
        anocolon = a.replace(":", "")
        channel = self.channel
        msgcontent = self.msgcontent
        cmdmsgcontent = msgcontent[7:]
        now = datetime.now()
        nowdate = str(datetime.now().day)
        nowhour = str(datetime.now().hour)
        nowminute = str(datetime.now().minute)
        nowmonth = str(datetime.now().month)
        timedigit = ''
        timeorig = self.timeorig
        user = self.user
        ampminnote = False
        aslash = False
        donotoverridetime = False
        needdate = False
        timedigitestablished = False
        timepopestablished = False


        print(str(timeorig) + ": timer invoked by user " + str(user) + " in channel " + str(channel))

        if a == "del" or a == "delete":
            print("user passed timer delete argument")
            delid = b
            if delid == "1":
                print("user attempted to delete timer 1, returning invalid")
                return ("Timer 1 is a permanent timer to simplify programmatic looping. You can ask Jordan if you want to know more.")
            else:
                print("attempting to open timer db")
                timerdata = open("/Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv", "rt")
                newtimerdata = open("/Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers1.csv", "a", newline='')
                reader = csv.reader(timerdata, delimiter=",")
                writer = csv.writer(newtimerdata)
                for row in reader:
                    if delid == row[0]:
                        print("timer exists, proceeding")
                        if delid != row[0]:
                            writer.writerow(row)
                    else:
                        print("user requested to delete nonexistent timer, returning invalid")
                        return ("that timer isn't even real")
                timerdata.close()
                newtimerdata.close()
                os.system('rm /Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv')
                os.system('mv /Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers1.csv /Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv')
                print("timer removed")
                return("Timer #" + delid + " deleted.")

        if a == "list":
            print("user requested the timer list")
            return("user requested list")
        
        elif "/" in a:
            print("/ in a, sending to dateparse")
            dateparse = a
            timeornote = b
            aslash = True

        elif a != "del" and a!= "delete" and a != "list" and aslash == False:
            print("starting timermonthpass")
            monthpassinit = timermonthpass(cmdmsgcontent)
            monthpass = monthpassinit.monthpass()
            print("monthpassescape")
            print("monthpass: " + monthpass)
            if monthpass != "nomonth":
                print("monthpass found month, setting dateparse")
                dateparse = monthpass.split("|")[0]
                monthpassnote = monthpass.split("|")[1]
                monthpasstime = monthpass.split("|")[2]
                print("dateparse: " + dateparse)
                print("monthpassnote: " + monthpassnote)
                print("monthpasstime: " + monthpasstime)
                timedigitestablished = True
                if monthpasstime == 'blank':
                    print("monthpasstime was blank")
                    timedigit = "06:00"
                if monthpasstime != 'blank':
                    print("monthpasstime not blank, setting timeparse")
                    timeparse = monthpasstime
                if monthpassnote == 'blank':
                    print("monthpassnote blank")
                    timernote = ''
                elif monthpassnote == 'notestartsatb':
                    print("note was startsatb")
                    timernote = msgcontent.split(a)[1]
                    print("timernote grabbed from monthpass: " + timernote)
                elif monthpassnote == 'notestartsatc':
                    print("note was startsatc")
                    timernote = msgcontent.split(b)[1]
                    print("timernote grabbed from monthpass: " + timernote)
                elif monthpassnote == 'notestartsatd':
                    print("note was startsatd")
                    timernote = msgcontent.split(c)[1]
                    print("timernote grabbed from monthpass: " + timernote)
                elif monthpassnote == 'notestartsate':
                    print("note was startsate")
                    timernote = msgcontent.split(d)[1]
                    print("timernote grabbed from monthpass: " + timernote)

            else:
                print("this is going to ogtimer: [" + a + "]")
                ogtimerinit = ogtimer(str(a))
                dortcheck = ogtimerinit.ogparse()
                needdate = True
                timedigitestablished = True
                print("dortcheck result: [" + dortcheck + "]")
                if dortcheck == 'inv':
                    print("dortcheck returned invalid")
                    return("Returned invalid - to set for specific time use X:XX format or for duration use old format.")
                else:
                    dort = dortcheck.split("|")[0]
                    if dort == 'wastime':
                        print("dort wastime")
                        time = dortcheck.split("|")[1]
                        timeparse = time
                        print("timeparse from dort: [" + timeparse + "]")
                        if b is not None:
                            print("b is not none")
                            timernote = msgcontent.split(a)[1]
                            print("note after dortcheck: [" + timernote + "]")
                        else:
                            timernote = ''
                            print("timernote from dort dbl check: [" + timernote + "]")
                            needdate = True
                            print("timeparse: [" + timeparse + "]")
                            timeparseinit = timeparser(timeparse, timernote)
                            timedigit = timeparseinit.gettime()
                            print("about ot try to print timedigit")
                            print(timedigit)
                    elif dort == 'wasduration':
                        print ("dort wasduration")
                        if a.isdigit():
                            timeval1raw = int(a)
                            unit1 = b.lower()
                            if unit1.startswith("m"):
                                timeval1 = timeval1raw
                            elif unit1.startswith("h"):
                                timeval1 = timeval1raw * 60
                            elif unit1.startswith("d"):
                                timeval1 = timeval1raw * 1440
                            elif unit1.startswith("w"):
                                timeval1 = timeval1raw * 10080
                            elif unit1.startswith("y"):
                                timeval1 = timeval1raw * 525600
                            else:
                                print("invalid unit used")
                                return("Invalid time unit or the bot is broken")
                            if c is not None:
                                if c.isdigit():
                                    timeval2raw = int(c)
                                    unit2 = d.lower()
                                    timernote = msgcontent.split(d)[1]
                                    if unit2.startswith("m"):
                                        timeval2 = timeval2raw
                                    elif unit2.startswith("h"):
                                        timeval2 = timeval2raw * 60
                                    elif unit2.startswith("d"):
                                        timeval2 = timeval2raw * 1440
                                    elif unit2.startswith("w"):
                                        timeval2 = timeval2raw * 10080
                                    elif unit2.startswith("y"):
                                        timeval2 = timeval2raw * 525600
                                    else:
                                        print("invalid unit used")
                                        return("Invalid time unit for second number or the bot is broken.")
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
                            timepop = timeorig + timedelta(minutes=timeval)
                            timepopestablished = True

        print("escapedhere")
        if timedigitestablished == False:
            if timeornote == '' or timeornote is None:
                    print("user provided no note or specific time. setting to defaults. (blank note and 6 AM for time)")
                    timernote = " "
                    timedigit = "06:00"
            if timeornote != '' and timeornote is not None:
                print(timeornote)
                print("timeornote exists")
                notenocolon = (str(timeornote)).replace(":","") 
                print("user provided some value after date, either a note or a time, checking now (all colons will be removed)")
                if notenocolon.isdigit():
                    print("notenocolon is digit, timeparse set to: " + notenocolon)
                    timeparse = notenocolon
                    splitpoint = msgcontent.split(timeornote)[1]
                    splitpointsplit = splitpoint.split(" ")
                    if splitpointsplit is None:
                        print("notenocolon was digit and split is none... setting note to blank")
                        timernote = ""
                    else:
                        print("user provided some fucking dumbass value after the timeparse, defaulting it as timernote")
                        timernote = splitpoint
                if not notenocolon.isdigit():
                    print("notenocolon NOT isdigit()... setting note, defaulting time to 6")
                    timernote = timeornote
                    timedigit = "06:00"
            print("timedigit: [" + timedigit + "]")
            if timernote.startswith(" ") and len(timernote) > 1:
                print("removing space from beginning of note")
                timernote = timernote[1:]
                print("new note: " + timernote)
        if timedigit == '' or timedigit is None:
            print("no timedigit, running timeparser with timeparse: [" + timeparse + "] and timernote: [" + timernote + "]")
            timeparseinit = timeparser(timeparse, timernote)
            timedigit = timeparseinit.gettime()
            print("timeparse class return: " + timedigit)
        if needdate == True:
            print("needdate true after timeparse, doing date comparison")
            nowhournozero = nowhour
            timerhour = timedigit.split(':')[0]
            timerhournozero = timerhour
            if nowhour.startswith("0"):
                print("nowhour starts with 0, replacing")
                nowhournozero = nowhour.replace("0", "")
            if timerhour.startswith("0"):
                print("timerhour starts with 0, replacing")
                timerhournozero = timerhour.replace("0", "")
            if int(nowhournozero) > int(timerhournozero):
                print("time now is greater than time in timer, setting for tomorrow")
                date = str((now + timedelta(days=1)).strftime('%Y-%m-%d'))
            elif int(nowhournozero) < int(timerhournozero):
                print("time now is less than time in timer, setting for today")
                date = nowdate
            elif int(nowhournozero) == int(timerhournozero):
                print("time is same hour as now, need to check min")
                nowminutenozero = nowminute
                timerminute = timedigit.split(':')[1]
                timerminutenozero = timerminute
                if nowminute.startswith("0"):
                    print("nowminute start with zero replacing")
                    nowminutenozero = nowminute.replace("0","")
                    print("replacement success")
                if timerminute.startswith("0"):
                    print("timerminute start with zero, replacing")
                    timerminutenozero = timerminute.replace("0","")
                if int(nowminutenozero) > int(timerminutenozero):
                    print("nowminute greater than timerminute, setting for tomorrow")
                    date = str((now + timedelta(days=1)).strftime('%Y-%m-%d'))
                    print("test: " + date)
                elif int(nowminutenozero) < int(timerminutenozero):
                    print("nowminute less than timerminute, setting for today")
                    date = str(now.strftime('%Y-%m-%d'))
                elif int(nowminutenozero) == int(timerminutenozero):
                    print("timerminute is... now. closing timer and messaging channel")
                    return("Timer set... annnnddd timer expired!")
            print("building timepop")
            timepop = date + " " + timedigit + ":00.000000"
            timepopestablished = True 
            print("timepop: [" + timepop + "]") 
            if timeparseinit.getmornnight() != "am.s":
                print("note started am or pm ")
                timernotesplit = timernote.split(" ")
                timernotesplit1 = (timernotesplit[2:])
                timernote = " ".join(timernotesplit1)
                print("timernote: [" + timernote + "]")
            if timedigit == 'inv':
                print("time invalid... maybe user didn't mean a time")
                return("the bot thinks you entered an invalid time, message me if it's wrong")
        if timepopestablished == False:
            print("building timepop")
            dateparseinit = dateslashparser(dateparse)
            datestr = dateparseinit.getdatewithslashes()
            if datestr == 'date inv':
                print('date invalid, closing timer')
                return("Invalid date my doogie")
            elif datestr == 'month inv':
                print('month invalid, closing timer')
                return("Invalid month, my melon")
                # add fun m words here?
            elif datestr == 'date inv 31':
                print('31 for 30 month, closing timer')
                return("That month only has 30 days my friend")
            elif datestr == 'date inv too many feb':
                print('too many days for february')
                return("February don't have that many days my ")
            elif datestr == 'year inv':
                print("year invalid")
                return("Invalid year my yuengling")
            elif datestr == 'inv leap':
                print("user used 02/29 for nonleap year")
                return("You used Feb 29 for a non-leap year my friend... day is none")
            else:
                timepop = datestr + " " + timedigit + ":00.000000"
        print("timepop: [" + timepop + "]")
        with open("/Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv", "r") as f:
            print("csv open")
            timercsv = f.readlines()
            oldid = timercsv[-1].split(',')[0]
            timerid = (int(oldid) + 1)
            fields = [timerid, user, timernote, timeorig, timepop, channel]
            with open("/Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        f.close()
        return("Timer set for " + timepop[:-10] + "! | ID: " + str(timerid))

    def printtest(self):
        print("file yanked")