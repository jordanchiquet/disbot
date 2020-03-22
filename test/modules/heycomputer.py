class heycomputer:
    def __init__(self, msgcontent):
        self.msgcontent = msgcontent.replace(".","")
    

    def defineintent(self):
        intenttextlist = self.getintenttext()
        if intenttextlist == "blankintent":
            return("blankintent")
            #come back to this
        if intenttextlist[0] == "a" or intenttextlist[0] == "an":
            del intenttextlist[0]
        if len(intenttextlist) < 1:
            return("inv")
        intenttext = intenttextlist[0]
        del intenttextlist[0]
        msg = self.msgcontent
        print("intenttextstrtest: [" + intenttext + "]")
        afterintentlist1 = msg.split(intenttext + " ")
        if len(afterintentlist1) < 2:
            afterintent = ""
        else:
            afterintent = str(msg.split((intenttext + " "))[1])
        if intenttext.startswith("image") or intenttext.startswith("img") or intenttext.startswith("pic") or intenttext.startswith("photo"):
            print("intenttext image")
            imgquery = self.imageintentparse(afterintent)
            print("imgquery: [" + imgquery + "]")
            if imgquery == "inv":
                return("inv")
            else:
                return("image|" + imgquery)
        elif intenttext.startswith("google"):
            return("google|" + afterintent)
        elif intenttext.startswith("def"):
            return("define|" + intenttext)
        elif intenttext.startswith("remind") or intenttext.startswith("timer"):
            timerintentresult = self.timerintentparse(afterintent)
            if timerintentresult == "inv":
                return("inv")
            else:
                return("timer|" + intenttext)
        else:
            return("inv")
        #reminder parse need to write
        print("placeholder")


    def getintenttext(self):
        msg = (self.msgcontent).lower()
        msgspacesplit = msg.split(" ")
        if len(msgspacesplit) == 1:
            return("blankintent")
        if msgspacesplit[0].startswith("hey") or msgspacesplit[0].startswith("hello") or msgspacesplit[0].startswith("hi") or msgspacesplit[0].startswith("hola"):
            del msgspacesplit[0]
        if len(msgspacesplit) < 2:
            return("blankintent") 
        elif msgspacesplit[1] == "load":
            if len(msgspacesplit) < 3:
                return("blankintent")
            elif msgspacesplit[2] == "me":               
                if len(msgspacesplit) < 4:
                    return("blankintent")
                elif msgspacesplit[3] == "up":
                    if len(msgspacesplit) < 5:
                        return("blankintent")
                    else:
                        intentchecktext = msgspacesplit[4]
            elif msgspacesplit[2] == "up":
                if len(msgspacesplit) < 4:
                    return("blankintent")
                else:
                    intentchecktext = msgspacesplit[3]
            else:
                intentchecktext = msgspacesplit[2]
        else:
            intentchecktext = msgspacesplit[1]
        msgspacesplit.insert(0, intentchecktext)
        return(msgspacesplit)


    def imageintentparse(self, afterintent):
        if afterintent == "":
            return("inv")
        print("starting img with afterintent: [" + afterintent + "]")
        afterintentlist = afterintent.split(" ")
        if afterintentlist[0] == "of" or afterintentlist[0] == "from":
            del afterintentlist[0]
            if len(afterintentlist) < 1:
                return("inv")
        if afterintentlist[0] == "a" or afterintentlist[0] == "an":
            del afterintentlist[0]
            if len(afterintentlist) < 1:
                return("inv")
        imgquery = (" ".join(afterintentlist))
        return(imgquery)
    

    def timerintentparse(self, afterintent):
        afterintentlist = afterintent.split(" ")
        metoout = afterintent.replace("me to ", "")
        if len(afterintentlist) < 2:
            print("afterintentlist was less than 2 length")
            return("inv")
        if afterintentlist[0] == "me":
            if len(afterintentlist) < 2:            
                print("afterintentlist was less than 2 length")
                return("inv")
            elif afterintentlist[1] == "to":
                if "in" in afterintent:
                    timersplit = metoout.split(" in ")
                    if len(timersplit) < 2:
                        return("inv")
                    else:
                        timernoteval = timersplit[0]
                        timeraonwardval = timersplit[1]
                if "on" in afterintent:
                    timersplit = metoout.split(" on ")
                    if len(timersplit) < 2:
                        return("inv")
                    else:
                        timernoteval = timersplit[0]
                        timeraonwardval = timersplit[1]
                else:
                    return("inv")
            elif afterintentlist[1] == "on" or afterintentlist == "in":
                if "to" in afterintent:
                    timersplit = metoout.split(" to ")
                    timeraonwardval = timersplit[0]
                    if len(timersplit) < 2:
                        timernoteval = ""
                    else:
                        timernoteval = timersplit[1]
                else:
                    timeraonwardval = afterintent
                    timernoteval = ""
            else:
                if "on" in afterintent:
                    timersplit = metoout.split(" on ")
                    timernoteval = timersplit[0]
                    if len(timersplit) > 1:
                        parseindex = len(timersplit)
                        timeraonwardval = timersplit[parseindex]
                elif "in" in afterintent:
                    timersplit = metoout.split(" in ")
                    timernoteval = timersplit[0]
                    if len(timersplit) > 1:
                        parseindex = len(timersplit)
                        timeraonwardval = timersplit[parseindex]
            return(timeraonwardval + "|" + timernoteval)
        else:
            return("inv")
                

