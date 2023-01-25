from modules.timertools.timerEntryValidation import timeEntryValidation as tEV
from modules.timertools.timerSQL import defaultRead, defaultWrite, timerWrite, getTimerId, expiryRemove 
from modules.sqlHandler import sqlMektanixDevilDog as mek
from modules.randomhelpers import getSpaceList, getFirstWordGoneString

class timerWriter:

    def __init__(self, userid: int, channelid: int, messageContent: str):
        print("timerWriter started with userid: [" + str(userid) + 
        "] and messageContet: [" + messageContent + "]")
        self.userid = str(userid)
        self.channelid = str(channelid)
        self.messageContent = messageContent.lower()
        self.tEV = tEV(self.messageContent)

    
    def timerWriterMain(self):
        print("starting timerWriterMain")
        if (self.messageContent[7:]).startswith("def"):
            print("default in messageContent beginning; timerWriterMain")
            timerWriterMainOutput = self.defaultWriter()
        elif (self.messageContent[7:]).startswith("del"):
            print("delete in messageContent beginning; timerWriterMain")
            timerWriterMainOutput = self.timerDelete()
        elif (self.messageContent[7:]).startswith("list"):
            print("list in messageContent beginning; timerWriterMain")
            timerWriterMainOutput = self.getTimerList()
        else:
            print("no 'default' cmd in messageContent beginning, starting regular timerparse; timerWriterMain")
            timerWriterMainOutput = self.parseValidatorOutput()
        return(timerWriterMainOutput)

    def parseValidatorOutput(self):
        print("starting parseValidatorOutput")
        timeEntryValidated = tEV(self.messageContent).inputParserMain()
        if timeEntryValidated[0] == "fail":
            print("fail in timeEntryValidated: [" + 
            str(timeEntryValidated) + "]")
            parserResult = ("fail", "It's not you, it's me")
        else:
            print("no fail in timeEntryValidated: [" +
            str(timeEntryValidated) + "]")
            expiryTime = self.defaultChecker(timeEntryValidated[0])
            timeEntryValidated = (expiryTime, timeEntryValidated[1])
            self.expiryWriter(timeEntryValidated)
            timerID = str(getTimerId(timeEntryValidated[0])[0])
            parserResult = ("pass", "Timer written for " + expiryTime[:-10] + "! | ID: " + (timerID.replace(",","")))
        return(parserResult)

    
    def defaultChecker(self, timeExpiry: str):
        print("starting defaultChecker with input: [" + timeExpiry + "]")
        nonoString = "noHour:noMinute"
        if nonoString in timeExpiry:
            defaultResult = defaultRead(self.userid)
            if defaultResult is None:
                timeReplace = "12:00"
            else:
                timeReplace = defaultResult[0]
            timeExpiry = timeExpiry.replace(nonoString, timeReplace)
        print("ending defaultChecker with output: [" + timeExpiry + "]")
        return(timeExpiry)
    

    def defaultWriter(self):
        print("defaultWriter started")
        defaultValidate = self.tEV.colonAndMeridiemHandler(getSpaceList(self.messageContent)[2:])
        print("defaultValidate: [" + str(defaultValidate) + "]")
        hR, mN, = defaultValidate[0], defaultValidate[1]
        if hR == "noHour":
            defaultWriterOut = "blame Jordan, I didn't understand that"
        else:
            if len(hR) == 1:
                hR = "0" + hR
            defaultWrite(self.userid, hR + ":" + mN)
            defaultWriterOut = "new default time written for date-only timers"
        print("defaultWriter ending with output: [" + defaultWriterOut + "]")
        return(defaultWriterOut)
    
    def expiryWriter(self, timer: tuple):
        print("expiryWriter started")
        writeData = self.userid, self.channelid, timer[0], timer[1]
        timerWrite(writeData)
    
    def timerDelete(self):
        print("timerDelete started")
        id = (getSpaceList(self.messageContent))[2]
        if id is None or not id.isdigit():
            timerDeleteOut = "invalid timer ID"
        else:
            timerIDSearch = mek(purpose = "read", table = "timers",
            resultColumn="expiry", queryColumn="idtimers",
            queryField = int(id))
            if timerIDSearch is None:
                timerDeleteOut = "maybe a dingo ate this timer"
            else:
                expiryRemove(int(id))
                timerDeleteOut = "I wouldn't worry about that timer ;)"
        return(timerDeleteOut)
    
    def getTimerList(self):
        return("https://bit.ly/renardtimers")



