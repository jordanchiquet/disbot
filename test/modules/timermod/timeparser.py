

class timeparser:
    def __init__(self, timeparse, timernote : str = None):
        self.timeparse = timeparse
        self.timernote = timernote

    def timetoobig(self, workingduration, workingunit):
        print("starting timetoobig check")
        if workingduration.startswith("0"):
            print("duration starts with 0 and automatically passes timetoobig check :) returning FALSE")
            return False
        else:
            print("duration does not start with 0, continuing")
            if workingunit == "h":
                print("workingunit is h, check for greater than 24")
                if int(workingduration) > 24:
                    print("working duration greater than 24, returning TRUE :(")
                    return True
                else:
                    print("working duration less than or equal to 24, returning FALSE :)")
                    return False
            elif workingunit == "m":
                print("workingunit is m, check for greater than 59")
                if int(workingduration) > 59:
                    print("working duration is greater than 59, returning TRUE :(")
                    return True
                else:
                    print("working duration is less than or equal to 59, returning FALSE :)")
                    return False
            else:
                print("wtf, working unit was not h or m... script dont know what to do :(")
                return("inv")


    def getmornnight(self):
        print("starting getmornnight")
        note = self.timernote
        if note.startswith(" "):
            print("note started with space, removing for parse")
            note = note[1:]
            note = note.split(" ")[0]
        if note is None or note == '':
            print("timernote was none, defaulting am")
            return("am")
        elif len(note) > 4 or len(note) < 2:
            print("timernote too long or too short to be what I'm looking for, defaulting to AM")
            return("am.s")
        else:
            workingnote = (note.lower())
            if not workingnote.startswith("a") and not workingnote.startswith("p"):
                print("timernote did not start with a or p, defaulting am")
                return("am")
            else:
                workingnote = workingnote.replace(".", "")
                if workingnote == "am":
                    print("note is am, returning am")
                    return("am")
                elif workingnote == "pm":
                    print("note is pm, returning pm")
                    return("pm")
                else:
                    print("note is not am or pm, defaulting to am")
                    return("am")


    def gettime(self):
        workingtime = self.timeparse
        workingtime = workingtime.replace(":", "")
        if len(workingtime) > 4 or not workingtime.isdigit():
            print("Timeparse value too many characters or not digit.")
            return("inv")
        else: 
            if len(workingtime) == 1 :
                print("workingtime is one digit")
                if workingtime == "0":
                    print("workingtime is one digit 0, returning 12 am")
                    return("00:00")
                else:
                    if self.getmornnight() == "am" or self.getmornnight() == "am.s":
                        print("getmornnight() returned am, keeping time")
                        return("0" + workingtime + ":00")
                    else:
                        print("getmornnight() returned pm, adding 12 to time")
                        newtime = str(int(workingtime) + 12)
                        return(newtime + ":00")
            if len(workingtime) == 2:
                print("workingtime is two digits")
                if self.timetoobig(workingtime, "h") == True:
                    print("TIMETOOBIG... returning inv for timeparse")
                    return("inv")
                if workingtime == "24" or workingtime == "00":
                    print("workingtime was 24 or 00... assuming user wants midnight")
                    return("00:00")
                if workingtime == "12":
                    print("working time is 12, checking getmornnight")
                    if self.getmornnight() == "am" or self.getmornnight() == "am.s":
                        print("returned am, setting midnight")
                        return("00:00")
                    if self.getmornnight() == "pm":
                        print("returned pm, setting noon")
                        return("12:00")
                else:
                    addtime = workingtime
                    if workingtime.startswith("0"):
                        print("workingtime started with 0, removing for addtime")
                        addtime = addtime[1]
                    if int(addtime) > 12:
                        print("working time greater than 12, assuming PM military time")
                        return(workingtime + ":00")
                    print("workingtime is valid, wasn't automatically midnight or military time, and wasn't 12, checking getmornnight")
                    if self.getmornnight() == "am" or self.getmornnight() == "am.s":
                        print("got am, keeping the same")
                        return(workingtime + ":00")
                    if self.getmornnight() == "pm":
                        print("got pm, need to add 12")
                        newtime = int(addtime) + 12
                        return(str(newtime) + ":00")
            if len(workingtime) == 3:
                print("workingtime is 3 digits")
                workinghour = workingtime[0]
                workingminutes = workingtime[-2:]
                if self.timetoobig(workingminutes, "m") == True:
                    print("TIMETOOBIG... returning inv for timeparse")
                    return("inv")
                elif workinghour == "0":
                    print("workinghour is 0, returning midnight plus workingminutes")
                    return("00:" + workingminutes)
                else:
                    print("workinghour is valid and not 0, checking getmornnight")
                    if self.getmornnight() == "am" or self.getmornnight() == "am.s":
                        print("returned am")
                        return("0" + workinghour + ":" + workingminutes)
                    if self.getmornnight() == "pm":
                        print("returned pm, adding 12")
                        newtime = str(int(workinghour) + 12)
                        return(newtime + ":" + workingminutes)
            if len(workingtime) == 4:
                print("workingtime is 4 digits")
                workinghour = workingtime[:2]
                print("workinghour: [" + workinghour + "]")
                workingminutes = str(workingtime[-2:])
                print("workingminutes: [" + workingminutes + "]")
                if self.timetoobig(workinghour, "h") == True or self.timetoobig(workingminutes, "m") == True:
                    print("TIMETOOBIG... returning inv for timeparse")
                    return("inv")
                elif workinghour == "00" or workinghour == "24":
                    print("workinghour was 00 or 24... assuming user wants midnight")
                    return("00:" + workingminutes)
                elif workinghour == "12":
                    print("working hour is 12, checking getmornnight")
                    if self.getmornnight() == "am" or self.getmornnight() == "am.s":
                        print("returned am, setting midnight")
                        return("00:00")
                    if self.getmornnight() == "pm":
                        print("returned pm, setting noon")
                        return("12:00")
                else:
                    addhour = workinghour
                    print("made it to addhour: [" + workinghour + "]")
                    if workinghour.startswith("0"):
                        print("workinghour started with 0, removing for addhour")
                        addhour = addhour[1]
                    if int(addhour) > 12:
                        print("workinghour greater than 12, assuming PM military time")
                        return(workinghour + ":" + workingminutes)
                    print("workinghour is valid, wasn't automatically midnight or military time, and wasn't 12, checking getmornnight")
                    if self.getmornnight() == "am" or self.getmornnight() == "am.s":
                        print("got am, keeping the same")
                        return(workinghour + ":" + workingminutes)
                    if self.getmornnight() == "pm":
                        print("got pm, need to add 12")
                        newhour = int(addhour) + 12
                        return(str(newhour) + ":" + workingminutes)
            
# timeparseinit = timeparser("354", "")
# print("timeparse class return: " + timeparseinit.gettime())