from datetime import datetime, timedelta
from modules.timermod.dateslashparser import dateslashparser
from modules.timermod.timermonthpass import timermonthpass
from modules.timermod.ogtimer import ogtimer
from modules.timermod.timeparser import timeparser
from modules.renardusers import renardusers
# from test.modules.timer.dateslashparser import dateslashparser
# from test.modules.timer.timermonthpass import timermonthpass
# from test.modules.timer.ogtimer import ogtimer


import csv
import mysql.connector
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
        # alower = a.lower()
        # anocolon = a.replace(":", "")
        channel = self.channel
        msgcontent = self.msgcontent
        cmdmsgcontent = msgcontent[7:]
        now = datetime.now()
        nowdate = str(datetime.now().day)
        nowhour = str(datetime.now().hour)
        nowminute = str(datetime.now().minute)
        # nowmonth = str(datetime.now().month)
        timedigit = ''
        timeorig = self.timeorig
        user = self.user
        # ampminnote = False
        aslash = False
        # donotoverridetime = False
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
            if b is not None:
                timeornote = b
            else:
                timeornote = ""
            print("after slash, timeornote is: [" + timeornote +"]")
            if c is not None:
                ampm = c
            else:
                ampm = None
            aslash = True

        elif a != "del" and a!= "delete" and a != "list" and aslash == False:
            print("starting timermonthpass")
            monthpassinit = timermonthpass(cmdmsgcontent)
            monthpass = monthpassinit.monthpass()
            print("monthpassescape")
            print("monthpass: " + monthpass)
            if monthpass != "nomonth":
                ampm = d
                getthatsplit = self.timernotnomonth(msgcontent, monthpass, a, b, c, d)
                splitted = getthatsplit.split("|")
                if splitted[0] == "blank":
                    print("made it out of timernotnomonth")
                    timernote = ""
                else:
                    timernote = splitted[0]
                    timernote = timernote[1:]
                print("timernote return: [" + timernote + "]")
                dateparse = splitted[3]
                if splitted[1] == "notimedigit":
                    print("notimedigit from notnomonth")
                    timeornote = splitted[2]
                    timedigit = ""
                else:
                    timedigit = splitted[1]
                    timedigitestablished = True    
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
                            timeparseinit = timeparser(timeparse, ampm, timernote)
                            timedigit = timeparseinit.gettime()
                            print("about ot try to print timedigit")
                            print(timedigit)
                    elif dort == 'wasduration':
                        print ("dort wasduration")
                        timedigit = "ph"
                        originaltimer = self.timerold(msgcontent, str(timeorig), a, b, c, d)
                        ogtimerstr = str(originaltimer)
                        if ogtimerstr.startswith("timepop"):
                            timepop = ogtimerstr.split("|")[1]
                            timernote = ogtimerstr.split("|")[2]
                            timepopestablished = True
                        else:
                            return(ogtimerstr)

        print("escapedhere")
        if timepopestablished == False:
            if timedigitestablished == False:
                print("timedigitestablished false")
                if timeornote == '' or timeornote is None:
                        print("user provided no note or specific time. setting to defaults. (blank note and 6 AM for time)")
                        timernote = " "
                        print(self.timerdefaultcheck())
                        if self.timerdefaultcheck() == None:
                            print("user has no default time, setting to 6")
                            timedigit = "06:00"
                        else: 
                            print("user has default time")
                            timedigit = self.timerdefaultcheck()
                            print("setting to: [" + timedigit +"]")
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
                            print("timeornote before split: [" + timeornote + "]")
                            print("after split but before indexing: [" + str(msgcontent.split(timeornote)) + "]")
                            timernotesplit = msgcontent.split(timeornote)[1:]
                            print("timernotesplit: [" + str(timernotesplit) + "]")
                            timernote = " ".join(timernotesplit)
                    if not notenocolon.isdigit():
                        print("notenocolon NOT isdigit()... setting note, defaulting time to 6")
                        timernotesplit = msgcontent.split(timeornote)[1:]
                        timernotesplit1 = " ".join(timernotesplit)
                        timernote = timeornote + timernotesplit1
                        if self.timerdefaultcheck() == None:
                            print("user has no default time, setting to 6")
                            timedigit = "06:00"
                        else: 
                            print("user has default time")
                            timedigit = self.timerdefaultcheck()
                            print("setting to: [" + timedigit +"]")
                print("timedigit: [" + timedigit + "]")
                if timernote.startswith(" ") and len(timernote) > 1:
                    print("removing space from beginning of note")
                    timernote = timernote[1:]
                    print("new note: " + timernote)
            if timedigit == '' or timedigit is None:
                print("no timedigit, running timeparser with timeparse: [" + timeparse + "] and timernote: [" + timernote + "]")
                timeparseinit = timeparser(timeparse, ampm, timernote)
                timedigit = timeparseinit.gettime()
                if timedigit == "inv":
                    return("my blockchain techniligies cannot read that time")
                print("timeparse class return: " + timedigit)
                if timeparseinit.getmornnight() != "am.s":
                    print("note started am or pm ")
                    timernotesplit = timernote.split(" ")
                    timernotesplit1 = (timernotesplit[1:])
                    timernote = " ".join(timernotesplit1)
                    print("timernote: [" + timernote + "]")
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
                print("building timepop (a)")
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
                print("building timepop (b)")
                print("starting dateparseinit with dateparse: [" + str(dateparse) +"]")
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
        mydb = mysql.connector.connect(
            host='18.216.39.250',
            user='dbuser',
            passwd='e4miqtng')
        mycursor = mydb.cursor()
        sql = "INSERT INTO renarddb.timers (user, timernote, timepop, channel, timeorig) VALUES (%s, %s, %s, %s, %s);"
        val = [user, timernote, timepop, channel, timeorig]
        mycursor.execute(sql, val)
        mydb.commit()
        # with open("/Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv", "r") as f:
        #     print("csv open")
        #     timercsv = f.readlines()
        #     oldid = timercsv[-1].split(',')[0]
        #     timerid = (int(oldid) + 1)
        #     fields = [timerid, user, timernote, timeorig, timepop, channel]
        #     with open("/Users/jordanchiquet/personalandfinance/disbotren/test/discordtimers.csv", "a", newline='') as f:
        #         writer = csv.writer(f)
        #         writer.writerow(fields)
        # f.close()
        return("Timer set for " + timepop[:-10] + "!")

    def printtest(self):
        print("file yanked")

    def timerdefaultcheck(self):
        print("starting sql query for default time")
        usertimeinit = renardusers(self.user, "timerdefault")
        print("reached users class")
        usertimerdefaultcheck = usertimeinit.userread()
        print("reached userread func, result: [" + str(usertimerdefaultcheck) + "]")
        if usertimerdefaultcheck is None:
            print("result was none")
            return(usertimerdefaultcheck)
        else:
            print("made it to concatenate default str")
            print("sql result: [" + str(usertimerdefaultcheck) + "]")
        return(usertimerdefaultcheck[0])
    
    def timerdefaultwrite(self): 
        timerdefaultinit = renardusers(self.user, "timerdefault", self.b)
        timerdefaultinit.userwrite()
        return("timer default write complete")
    
    def timernotnomonth(self, msgcontent, monthpass, a: str = None, b: str = None, c: str = None, d: str = None):
            print("monthpass found month, setting dateparse")
            dateparse = monthpass.split("|")[0]
            monthpassnote = monthpass.split("|")[1]
            monthpasstime = monthpass.split("|")[2]
            print("dateparse: " + dateparse)
            print("monthpassnote: " + monthpassnote)
            print("monthpasstime: " + monthpasstime)
            
            if monthpasstime == 'blank':
                print("monthpasstime was blank")
                if self.timerdefaultcheck() == None:
                    print("user has no default time, setting to 6")
                    timedigit = "06:00"
                else: 
                    print("user has default time")
                    timedigit = self.timerdefaultcheck()
                    print("setting to: [" + timedigit +"]")
            if monthpasstime != 'blank':
                print("monthpasstime not blank, setting timeparse")
                timeparse = monthpasstime
                timedigit = ''
            if monthpassnote == 'blank':
                print("monthpassnote blank")
                timernote = 'blank'
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
            else:
                print("note was startsate")
                timernote = msgcontent.split(d)[1]
                print("timernote grabbed from monthpass: " + timernote)
            if timedigit == '':
                print("timedigit none from notnomonth")
                return(timernote + "|notimedigit|" + timeparse + "|" + dateparse)
            else:
                print("timedigt not none from notnomonth")
                return(timernote + "|" + timedigit + "|notimeparse|" + dateparse)

    def timerold(self, msgcontent, timeorig, a, b, c: str = None, d: str = None):
        print("timerold started")
        print("this is the timeorig we getting [" + timeorig +"]")
        if a.isdigit():
            print("a is digit, continuing")
            timeval1raw = int(a)
            unit1 = b.lower()
            if unit1.startswith("m"):
                timeval1 = timeval1raw
            elif unit1.startswith("h"):
                print("sanity can confirm hour")
                timeval1 = timeval1raw * 60
            elif unit1.startswith("d"):
                timeval1 = timeval1raw * 1440
            elif unit1.startswith("w"):
                timeval1 = timeval1raw * 10080
            elif unit1.startswith("y"):
                timeval1 = timeval1raw * 525600
            else:
                print("invalid unit used")
                return("Invalid duration unit OR you tried to name a specific time without using a colon.")
            if c is not None:
                if c.isdigit():
                    timeval2raw = int(c)
                    unit2 = d.lower()
                    timernote = msgcontent.split(d)[1]
                    timernote = timernote[1:]
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
                        return("Invalid duration unit OR you tried to name a specific time without using a colon.")
                if not c.isdigit():
                    timeval2 = 0
                    timeval2raw = ""
                    unit2 = ""
                    timernote = msgcontent.split(b)[1]
                    timernote = timernote[1:]
            if c is None:
                print("sanity can confirm c is none")
                timeval2 = 0
                timeval2raw = ""
                unit2 = ""
                timernote = ""
            timeval = timeval1 + timeval2
            timeorig = datetime.strptime(timeorig, '%Y-%m-%d %H:%M:%S.%f')
            print(timeorig)
            timepop = timeorig + timedelta(minutes=timeval)
            print("made it to timepop at end of original timer: [" + str(timepop) + "]")
            return ("timepop|" + str(timepop) + "|" + timernote)                   

    def timercheck(self):
        checknow = datetime.now()
        print("Timer check starting... [" + str(checknow) + "]")
        mydb = mysql.connector.connect(
            host='18.216.39.250',
            user='dbuser',
            passwd='e4miqtng')
        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT timepop FROM renarddb.timers"
        mycursor.execute(sql)
        for x in mycursor:
            if len(x[0]) < 20:
                timepopval = x[0] + ".000000"
            else: 
                timepopval = x[0]
            # print("timepopval: [" + timepopval + "]")
            if checknow <= datetime.strptime(timepopval, '%Y-%m-%d %H:%M:%S.%f'):
                continue
            else:
                print("Time pop for [" + timepopval + "]! Removing record and messaging channel.")
                infosql = "SELECT id, user, timernote, channel, extratags FROM renarddb.timers WHERE timepop = \"" + x[0] + "\""
                mycursor.execute(infosql)
                for y in mycursor:
                    y = y + (x[0],)
                    print(y)
                    removesql = "DELETE FROM renarddb.timers WHERE timepop = \"" + x[0] + "\";"
                    mycursor.execute(removesql)
                    mydb.commit()
                    return(y)



