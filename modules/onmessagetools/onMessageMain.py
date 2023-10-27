from modules.onmessagetools import onMessagePicTriggers, onMessageSQLCounter, onMessageJokeTriggers, onMessageHeyComputer, onMessageAutoEmbedders, onMessageContentParser

from modules.randomhelpers import subEmotes

class onMessageHandler:

    def __init__(self, serverid: int, channelid: int,
    userid: int, username: str, timestamp, messageContent: str, messageobj: any = None):
        print("onMessageHandler started")
        print(messageContent)
        self.serverid = serverid
        self.serveridStr = str(serverid)
        self.channelid = channelid
        self.userid = userid
        self.useridStr = str(userid)
        self.username = username
        self.timestamp = str(timestamp)
        self.msgContent = subEmotes(messageContent.lower(), "")
        self.messageobj = messageobj
    
    def messageHandleMain(self):
        print("messageHandleMain started")
        sqlInit = onMessageSQLCounter.sqlCounterMain(self.serveridStr, self.useridStr, self.msgContent, self.username)
        sqlInit.sqlCounterMain()
        messageHandleReturn = "none", ""
        autoEmbedderCheck = None
        # if self.userid == 172581464066490369 and self.channelid != 499792227464380428:
        #     return("emote", "didn't ask")
        onMessageHeyComputerInit = onMessageHeyComputer.OnMessageHeyComputer(self.msgContent)
        heyComputerCheck = onMessageHeyComputerInit.heyComputerMainHandle()
        thisBitchCheck = onMessagePicTriggers.thisBitchTrigger(self.msgContent)
        picTriggerCheck = onMessagePicTriggers.picTriggerMain(self.msgContent, self.serverid)
        jokeTriggerCheck = onMessageJokeTriggers.jokeTriggerMain(self.msgContent)
        containsEmbed = onMessageContentParser.containsEmbed(self.messageobj)
        if not containsEmbed:
            autoEmbedderInit = onMessageAutoEmbedders.OnMessageAutoEmbedder(self.msgContent)
            autoEmbedderCheck = autoEmbedderInit.autoEmbedderMain()


        if thisBitchCheck[0]:
            messageHandleReturn = "file", thisBitchCheck[1]
        elif picTriggerCheck[0]:
            messageHandleReturn = "file", picTriggerCheck[1]
        elif jokeTriggerCheck[0]:
            messageHandleReturn = "text", jokeTriggerCheck[1]
        elif heyComputerCheck[0]:
            messageHandleReturn = heyComputerCheck[1], heyComputerCheck[2]
        elif autoEmbedderCheck:
            messageHandleReturn = "text", autoEmbedderCheck
        
        print("messageHandleReturn: [" + str(messageHandleReturn) + "]")
        return(messageHandleReturn)
    
    def messageHandleTestBot(self):
        print("messageHandleMain started")
        onMessageHeyComputerInit = onMessageHeyComputer.OnMessageHeyComputer(self.msgContent)
        messageHandleReturn = "none", ""
        heyComputerCheck = onMessageHeyComputerInit.heyComputerMainHandle()
        thisBitchCheck = onMessagePicTriggers.thisBitchTrigger(self.msgContent)
        picTriggerCheck = onMessagePicTriggers.picTriggerMain(self.msgContent)
        jokeTriggerCheck = onMessageJokeTriggers.jokeTriggerMain(self.msgContent)
        if thisBitchCheck[0]:
            messageHandleReturn = "file", thisBitchCheck[1]
        elif picTriggerCheck[0]:
            messageHandleReturn = "file", picTriggerCheck[1]
        elif jokeTriggerCheck[0]:
            messageHandleReturn = "text", jokeTriggerCheck[1]
        elif heyComputerCheck[0]:
            messageHandleReturn = heyComputerCheck[1], heyComputerCheck[2]
        print("messageHandleReturn: [" + str(messageHandleReturn) + "]")
        return(messageHandleReturn)
    
    
