

class timermonthpass:
    def __init__(self, cmdmsgcontent):
        self.cmdmsgcontent = cmdmsgcontent
    

    def monthpass(self):
        print("starting timer monthpass")
        workingmsg = (self.cmdmsgcontent).split(" ")
        timerparam = (workingmsg[0]).lower()
        if (timerparam.startswith("jan") or
        timerparam.startswith("feb") or
        timerparam.startswith("mar") or
        timerparam.startswith("apr") or
        timerparam.startswith("may") or
        timerparam.startswith("jun") or
        timerparam.startswith("jul") or
        timerparam.startswith("aug") or
        timerparam.startswith("sep") or
        timerparam.startswith("oct") or
        timerparam.startswith("nov") or
        timerparam.startswith("dec")):
            print("user used english words for month, converting to number")
            timeparse = "blank"
            if timerparam.startswith("jan"):
                month = "01"
            if timerparam.startswith("feb"):
                month = "02"
            if timerparam.startswith("mar"):
                month = "03"
            if timerparam.startswith("apr"):
                month = "04"
            if timerparam.startswith("may"):
                month = "05"
            if timerparam.startswith("jun"):
                month = "06"
            if timerparam.startswith("jul"):
                month = "07"
            if timerparam.startswith("aug"):
                month = "08"
            if timerparam.startswith("sep"):
                month = "09"
            if timerparam.startswith("oct"):
                month = "10"
            if timerparam.startswith("nov"):
                month = "11"
            if timerparam.startswith("dec"):
                month = "12"
            if len(workingmsg) == 1:
                print("user provided no date, defaulting to 01")
                date = "01"
                note = 'blank'
                return(month + "/" + date + "|" + note + "|" + timeparse)
            if len(workingmsg) > 1:
                print("something where the date goes, doing firstpass")
                posdate = workingmsg[1]
                posdatenozero = posdate
                if posdate.startswith("0"):
                    print("replacing zero if date starts with 0 to do next check")
                    posdatenozero = posdate.replace("0", "")
                if len(posdate) < 3 and posdatenozero.isdigit():
                    print("value where date goes less than 3 digits and is a number... going to use it as date")
                    date = posdate
                elif len(posdate) == 4 and posdate.isdigit():
                    print("user skipped date to put a year here looks like")
                    date = "01"
                    year = posdate
                    print("monthpassdebugyear: " + year)
                    note = "notestartsatc"
                    return(month + "/" + date + "/" + year + "|" + note + "|" + timeparse)
                else:
                    print("value where date goes does not look like date. setting it as 01")
                    note = "notestartsatb"
                    date = "01"

            if len(workingmsg) < 3:
                print("user provided no year or note")
                note = 'blank'
                return(month + "/" + date + "|" + note + "|" + timeparse)
            if len(workingmsg) > 2:
                print("something where the year goes")
                posyear = (workingmsg[2])
                posyearnocolon = posyear.replace(":","")
                print("posyear: [" + posyear + "], posyearnocolon: [" + posyearnocolon + "]")
                if posyearnocolon.isdigit():
                    print("that something is a number without colon")
                    if len(posyearnocolon) > 4:
                        print("that something is greater than 4 digits without colon, setting as note")
                        note = posyear
                        return(month + "/" + date + "|" + note + "|" + timeparse)
                    elif len(posyearnocolon) == 1 or len(posyearnocolon) == 3:
                        print("that something is 1 digit or 3 digits, setting as time")
                        timeparse = posyearnocolon
                        if len(workingmsg) > 3:
                            print("still more after, setting whatever that is as note value")
                            note = "notestartsatd"
                            return(month + "/" + date + "|" + note + "|" + timeparse)
                        else:
                            print("no note provided")
                            note = 'blank'
                            return(month + "/" + date + "|" + note + "|" + timeparse)
                    elif ":" in posyear and len(posyearnocolon) > 2:
                        print("that something has a colon and is at least 3 digits without colon, setting it as time")
                        timeparse = posyear
                        if len(workingmsg) > 3:
                            print("still more after, setting whatever that is as note value")
                            note = "notestartsatd"
                            return(month + "/" + date + "|" + note + "|" + timeparse)
                        else:
                            print("no note provided")
                            note = 'blank'
                            return(month + "/" + date + "|" + note + "|" + timeparse)
                    else:
                        print("that something is 2 digits or 4 digits and had no colon, assuming it's a year :)")
                        year = posyear
                        if len(workingmsg) > 3:
                            print("still more after, could be a note or a time... no rest for the wicked")
                            workingmsg2nocolon = (workingmsg[3]).replace(":", "")
                            if workingmsg2nocolon.isdigit() and len(workingmsg2nocolon) < 5:
                                print("workingmsg2nocolon was digit and less than 4 characters... setting as timeparse")
                                timeparse = workingmsg2nocolon
                                if len(workingmsg) > 4:
                                    print("STILL more after, assuming it's the note.")
                                    note = 'notestartsate'
                                    return(month + "/" + date + "/" + year + "|" + note + "|" + timeparse)
                                else:
                                    print("nothing after, note is blank")
                                    note = 'blank'
                                    print("testnuts: " + date)
                                    return(month + "/" + date + "/" + year + "|" + note + "|" + timeparse)
                        else:
                            print("no note or time provided provided")
                            note = 'blank'
                            return(month + "/" + date + "/" + year + "|" + note + "|" + timeparse)
                else:
                    print("value where year goes not timer looking for... setting it as note instead")      
                    note = 'notestartsatc'
                    return(month + "/" + date + " | " + note + "|" + timeparse)
    
        else:
            return("nomonth")

monthpassinit = timermonthpass('jan 1 2021 700')
monthpass = monthpassinit.monthpass()
print(monthpass)
            

            
            