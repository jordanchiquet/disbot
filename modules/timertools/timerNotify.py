from modules.randomhelpers import getRegexReturn
from modules.timertools import timerSQL


class timerNotify:

    def __init__ (self, userid: str, messageContent: str):
        print("extraNotify initialized")
        self.userid = userid
        self.msgContent = messageContent
        self.timerid = self.getTimerID()
        self.notifyUsers = self.getNotifyUsers()

    
    def extraNotifyWrite(self):
        print("starting extraNotifyMain")
        if not self.isTimerActive():
            extraNotifyWriteOut = "timer inactive"
        elif self.isNotifyDupe():
            extraNotifyWriteOut = "duplicate userid"
        else:
            timerSQL.addNotifyUsers(self.timerid, self.userid)
            extraNotifyWriteOut = str(self.timerid)
        print("extraNotifyWrite returning: [" + extraNotifyWriteOut + "]")
        return(extraNotifyWriteOut)
    

    def getNotifyUsers(self):
        print("starting getNotifyObject")
        getNotifyResults = (timerSQL.getNotifyUsers(self.timerid))
        if getNotifyResults is None:
            getNotifyResults = "no result"
        else:
            getNotifyResults = getNotifyResults[0]
        print("getNotifyResults: [" + str(getNotifyResults) + "]")
        return(getNotifyResults)
    
    def removeNotifyUser(self):
        print("starting removeNotifyUser")
        timerid = self.getTimerID()
        timerSQL.removeNotifyUser(timerid, str(self.userid))
        return(str(timerid))
        #TODO: hook this up to the bot on_reaction_remove

    def isTimerActive(self):
        print("starting isTimerActive")
        if self.notifyUsers == "no result":
            timerActive = False
        else:
            timerActive = True
        print("isTimerActive returning: [" + str(timerActive) + "]")
        return(timerActive)

    def isNotifyDupe(self):
        print("starting isNotifyDupe")
        if self.userid in self.notifyUsers:
            duplicateNotifyUser = True
        else:
            duplicateNotifyUser = False
        print("isNotifyDupe returning: [" + str(duplicateNotifyUser) + "]")
        return(duplicateNotifyUser)


    def getTimerID(self):
        print("starting getTimerID with input: [" + self.msgContent + "]")
        idOut = (getRegexReturn(query=r"\(([^\)]+)\)", input=self.msgContent))[0]
        print("idOut: [" + idOut + "]")
        if not idOut.isdigit():
            idOut = "invalid"
        else:
            idOut = int(idOut)
        return(idOut)

