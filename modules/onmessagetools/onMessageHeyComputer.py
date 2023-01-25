from modules import randomhelpers as rh
from modules import commandHandler as ch


class OnMessageHeyComputer:

    def __init__(self, msgContent: str):
        print("onMessageHeyComputer initialized")
        self.msgWordList = rh.getSpaceList(msgContent)

    
    def heyComputerMainHandle(self):
        print("heyComputerMainHandle started")
        heyComputerMainOut = (False, "", "")
        if self.lookForCommand():
            print("looking for command in heyComputerMain")
            if self.tryGetQueryCommand():
                if self.tryGetParam():
                    heyComputerMainOut = (True, "text", ch.cmdHandlerWebQueries(self.command, self.param))
                else:
                    print("placeholder")
                    #TODO: cmdOnlyHandler
            elif self.tryGetOtherCommand():
                print("placeholder")
                #TODO:big big doozy here huh
        return(heyComputerMainOut)
    

    def lookForCommand(self) -> bool:
        print("lookForCommand started with self.msgWordList: [" + str(self.msgWordList) + "]")
        lookingForCommand = False
        #TODO: bug here with command 'computer, load up a dog image' ; always returning False
        if self.msgWordList[0] in str(greetingIgnoreList):
            print("greeting found as first entry: [" + self.msgWordList[0] + "]")
            self.msgWordList = rh.removefirstindex(self.msgWordList)
            print("self.msgWordList after greeting removal: [" + str(self.msgWordList) + "]")
        if len(self.msgWordList) >= 2:
            lfcCheck = rh.getRegexReturn(query=computerPrefixTriggerRegex, input=self.msgWordList[0])
            if lfcCheck is not None:
                print("regex match in lookForCommand {}".format(lfcCheck))
                self.msgWordList = rh.removefirstindex(self.msgWordList)
                self.msgString = " ".join(self.msgWordList)
                lookingForCommand = True
        else:
            print("self.msgWordList: [" + str(self.msgWordList) + "] found to not be >= 2 len")
        print("lookForCommand returning: [" + str(lookingForCommand) + "]")
        return(lookingForCommand)

    def commandDictInit(self):
        print("commandDictInit started")
        self.queryCommandDict = {}
        for key in ["defin", "meaning"]:
            self.queryCommandDict[key] = "d"
        for key in ["picture", "pictograph", "pic", "photograph", "photo", "image", "img"]:
            self.queryCommandDict[key] = "img"
        for key in ["video", "clip", "vid"]:
            self.queryCommandDict[key] = "yt"
        for key in ["wikipedia", "wiki"]:
            self.queryCommandDict[key] = "wiki"
        for key in ["google", "bing", "search"]: #this needs to be last,
            #because 'search' might be used in command term for the other ones
            self.queryCommandDict[key] = "g"
        self.otherCommandDict = {}
        print("self.queryCommandDict initialized and declared")

    def articleListInit(self):
        print("articleListInit started")
        self.articleList = ["a", "an"]

    def tryGetQueryCommand(self) -> bool:
        print("tryGetQueryCommand started")
        self.commandDictInit()
        for key in self.queryCommandDict:
            if rh.getRegexReturn(query=key, input=self.msgString) is not None:
                self.command = self.queryCommandDict[key]
                self.cmdMsgSplit = key
                print(key + "found command: [" + self.command + "]")
                return(True)
        return(False)

    def tryGetOtherCommand(self) -> bool:
        print("tryGetOtherCommand started")
        
        return(False)

    def tryGetParam(self) -> bool:
        print("tryGetParam started with self.cmdMsgSplit: [{}]".format(self.cmdMsgSplit))
        self.cmdRemovalList = (self.msgString).split(self.cmdMsgSplit)
        self.articleListInit()
        if self.tryGetQueryAfterCmd():
            return(True)
        elif self.tryGetQueryBeforeCmd():
            return(True)
        else:
            return(False)

    def tryGetQueryAfterCmd(self) -> bool:
        print("tryGetQueryAfterCmd started with [1] of self.cmdRemovalList: [" + 
        str(self.cmdRemovalList) + "]")
        gotParam = False
        self.workingParam = (self.cmdRemovalList[1])
        self.paramEndingCleanser()
        self.queryFinalGauntlet()
        if self.workingParam != "":
            self.param = self.workingParam[2:]
            print("HEY COMPUTER GOING FORWARD WITH QUERY: [" + self.param + "]")
            gotParam = True
        return(gotParam)

    def tryGetQueryBeforeCmd(self) -> bool:
        print("tryGetQueryBeforeCmd started with [0] of self.cmdRemovalList: [" + 
        str(self.cmdRemovalList) + "]")
        gotParam = False
        self.workingParam = self.cmdRemovalList[0]
        self.queryBeginningCleanser()
        self.queryFinalGauntlet()
        if self.workingParam != "":
            self.param = self.workingParam[:-1]
            print("HEY COMPUTER GOING FORWARD WITH QUERY: [" + self.param + "]")
            gotParam = True
        return(gotParam)
    
    def queryBeginningCleanser(self):
        print("queryBeginningCleanser started")
        beginningPruneList = ["please", "can you", "can i get you to", "do",
        "load up", "load for me" "load me up", "load", 
        "give me", "give to me", "give", 
        "show me", "show to me", "show",
        "can i have", "can i get"
        ]
        for item in beginningPruneList:
            if (self.workingParam).startswith(item):
                self.workingParam = self.workingParam[len(item)+1:]
                for item in self.articleList:
                    if (self.workingParam).startswith(item):
                        self.workingParam = self.workingParam[len(item)+1:]
                # ^this may need to be len +1

    def paramEndingCleanser(self):
        print("paramEndingCleanser started")
        endingPruneList = ["please", "pls", "plz", "thanks", "thx", 
        "thank you", "for me"]
        for item in endingPruneList:
            if (self.workingParam).endswith(item):
                print("paramEndingCleanser; self.workingParam: [" + self.workingParam + "]"
                "found to end with endingPruneList item: [" + item + "]")
                self.workingParam = self.workingParam[:-len(item)]
            
    def queryFinalGauntlet(self):
        print("queryFinalGauntlet started")
        if self.cmdMsgSplit != "search":
            if (self.workingParam).startswith("search"):
                self.workingParam = self.workingParam[7:] #may need to be 6 or 8
        for item in [" ", "for", "of"]:
            if (self.workingParam).startswith(item):
                self.workingParam = self.workingParam[len(item)+1:]
        print("self.param AFTER FINAL GAUNTLET: [" + self.workingParam + "]")
    
    def queryCmdHandler(self):
        print("queryCmdHandler started")
        thatList = ["that", "the", "this"]
        for item in thatList:
            if self.param == item:
                print("self.param was that the this")
                #TODO return to bot that we need previous message, then process it


    




        

computerPrefixTriggerRegex = (
    r"comp\w+|"
    r"jarvis|"
    r"machine|"
    r"^(robo)?renard|"
    r"^(ro)?bot\b|"
    r"techbride\b" #having | at the end makes the empty string after caught
)

greetingIgnoreList = [
    "hey",
    "ayo",
    "ay",
    "mister",
    "hello",
    "mr",
    "yo",
    "please"
]

