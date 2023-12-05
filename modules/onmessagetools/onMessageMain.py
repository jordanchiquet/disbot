from modules.onmessagetools import onMessagePicTriggers, onMessageSQLCounter, onMessageJokeTriggers, onMessageHeyComputer, onMessageAutoEmbedders, onMessageContentParser

from modules.randomhelpers import subEmotes

from datetime import timedelta

class onMessageHandler:

    def __init__(self, messageobj: any = None, testBot: bool = False):
        print("onMessageHandler started")
        self.serverid = messageobj.guild.id
        self.serveridStr = str(self.serverid)
        self.channelid = messageobj.channel.id
        self.userid = messageobj.author.id
        self.useridStr = str(self.userid)
        self.username = (str(messageobj.author)).split("#")[0]
        self.timestamp = str(messageobj.created_at - timedelta(hours=5))
        self.msgContentLower = subEmotes((messageobj.content).lower(), "")
        self.msgContentOriginalCase = subEmotes(messageobj.content, "")
        self.messageobj = messageobj
        self.testBot = testBot
    
    def messageHandleMain(self):
        print("messageHandleMain started")
        sqlInit = onMessageSQLCounter.sqlCounterMain(self.serveridStr, self.useridStr, self.msgContentLower, self.username)
        if not self.testBot:
            sqlInit.sqlCounterMain()
        else:
            print("testBot detected, not counting message")
        messageHandleReturn = "none", ""
        autoEmbedderCheck = None
        # if self.userid == 172581464066490369 and self.channelid != 499792227464380428:
        #     return("emote", "didn't ask")
        onMessageHeyComputerInit = onMessageHeyComputer.OnMessageHeyComputer(self.msgContentLower)
        heyComputerCheck = onMessageHeyComputerInit.heyComputerMainHandle()
        thisBitchCheck = onMessagePicTriggers.thisBitchTrigger(self.msgContentLower)
        picTriggerCheck = onMessagePicTriggers.picTriggerMain(self.msgContentLower, self.serverid)
        jokeTriggerCheck = onMessageJokeTriggers.jokeTriggerMain(self.msgContentLower)
        containsEmbed = onMessageContentParser.onMessageContentParserMain(self.messageobj)
        if not containsEmbed:
            autoEmbedderInit = onMessageAutoEmbedders.OnMessageAutoEmbedder(self.msgContentOriginalCase)
            autoEmbedderCheck = autoEmbedderInit.autoEmbedderMain()




        if not self.messageobj.author.bot:
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
        onMessageHeyComputerInit = onMessageHeyComputer.OnMessageHeyComputer(self.msgContentLower)
        messageHandleReturn = "none", ""
        heyComputerCheck = onMessageHeyComputerInit.heyComputerMainHandle()
        thisBitchCheck = onMessagePicTriggers.thisBitchTrigger(self.msgContentLower)
        picTriggerCheck = onMessagePicTriggers.picTriggerMain(self.msgContentLower)
        jokeTriggerCheck = onMessageJokeTriggers.jokeTriggerMain(self.msgContentLower)
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
    
    
