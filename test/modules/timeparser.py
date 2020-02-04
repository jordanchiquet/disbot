class timeparser:
    def __init__(self, timeparse, timernote):
        self.timeparse = timeparse
        self.timernote = timernote
    
        def getmornnight(self):
        if len(self.timernote) > 4 or len(self.timernote) < 2:
            print("timernote too long or too short to be what I'm looking for, defaulting to AM")
            return("am")
        else:
            workingnote = (self.timernote).lower()
            if not workingnote.startswith("a") and
            not workingnote.startswith("p"):
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
        if len(self.timeparse) > 4 or not self.timeparse.isdigit():
            print("Timeparse value too many characters or not digit.")
            return("inv")
        else: 
            if len(workingtime) == 1 :
                print("workingtime is one digit")
                if workingtime == "0":
                    print("workingtime is one digit 0, returning 12 am")
                    return("00:00")
                else:
                    if self.getmornnight() == "am":
                        print("getmornnight returned am, keeping time")
                        return("0" + workingtime + ":00")
                    else:
                        print("getmornnight returned pm, adding 12 to time")
                        newtime = str(int(workingtime) + 12)
                        return(newtime + ":00")
            if len(workingtime) == 2:
                print("workingtime is two digits")
                if int(workingtime) > 23:
                    print("two digit time greater than 23, nothing I can do with that")
                    return("inv")
                else:
                    print("two digits less than 24, continuing")
                    if not workingtime.startswith("0"):
                        if int(workingtime) > 12:
                            print("two digits greater than 12... assuming user wants PM (mil time)")
                            return(workingtime + ":00")
                        elif workingtime == "12":
                            print("time is 12, checking getmornnight")
                            if self.getmornnight() == "am":
                                print("12 and am, converting to 00:00)
                                return("00:00")
                            if self.getmornnight() == "pm":
                                print("12 and pm, keeping as noon")
                                return("12:00")
                    else:
                        print("two digits are 10 or 11 or start with 0, checking getmornnight")
                        if self.getmornnight() == "am":
                            print("getmornnight is am, adding :00")
                            return(workingtime + ":00")
                        if self.getmornnight() == "pm":
                            print("getmornnight is pm, adding 12 hour")
                            newtime = str(int(workingtime) + 12)
                            return(newtime + ":00")
            if len(workingtime) == 3:
                print("workingtime is 3 digits")
                workinghour = workingtime[0]
                workingminutes = workingtime[-2:]
                if not workingminutes.startswith("0"):
                    print("workingminutes does not start with 0, checking to see if > 59")
                    if int(workingminutes) > 59:
                        print("workingminutes more than 59, nothing i can do with that")
                        return("inv")        
                    else:
                        print("workingminutes less than 59, continuing")
                if workinghour = "0":
                    print("workinghour is 0, returning midnight plus workingminutes")
                    return("00:" + workingminutes)
                else:
                    print("workinghour is valid and not 0, checking getmornnight")
                    if self.getmornnight() == "am":
                        print("returned am")
                        return("0" + workinghour + ":" + workingminutes)
                    if self.getmornnight() == "pm":
                        print("returned pm, adding 12")
                        newtime = str(int(workinghour) + 12)
                        return(newtime + ":" + workingminutes)
            if len(workingtime) == 4:
                print("workingtime is 4 digits")
                workinghour = workingtime[:2]
                workingminutes = workingtime[-2:]
                if not workinghour.startswith("0"):
                    
            






        