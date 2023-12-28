from modules.sqlHandler import sqlMektanixDevilDog as mek
from modules.randomhelpers import getSpaceList



class sqlCounterMain:

    def __init__(self, serverid, userid, msgContent, username):
        self.serverid = str(serverid)
        self.userid = str(userid)
        self.queryField = (self.serverid + "|" + self.userid)
        self.msgContent = msgContent
        self.username = username
        self.filterarray = [940975831910604811, 1185999723958653098]
    

    def sqlCounterMain(self):
        print("sqlCounterMain starting")
        for server in self.filterarray:
            if self.serverid == server:
                return
        self.msgCounter()
        self.wordCounter()
        self.specificCounter()
        self.sqlCounterNameUpdater()

        #TODO: msgCounter, wordCounter, fuckCounter, 
        # iMeanCounter, dudeCounter, shitCounter

    def msgCounter(self):
        self.sqlCounterIntAdder("msg", 1)
    
    def wordCounter(self):
        addInt = len(getSpaceList(self.msgContent))
        self.sqlCounterIntAdder("word", addInt)
    
    def specificCounter(self):
        self.countDictInit()
        for key in self.countDict:
            intAdd = (self.msgContent).count(key)
            if intAdd > 0:
                itemColumn = self.countDict[key]
                self.sqlCounterIntAdder(itemColumn, intAdd)
    
    def countDictInit(self):
        self.countDict = {
            "dude": "dude",
            "i mean": "imean",
            "retard": "retard",
            "shit": "shit"
            }
        for key in ["fuck", "fck"]:
            self.countDict[key] = "fuck"
        for key in ["please", "pls", "plz"]:
            self.countDict[key] = "please"
        for key in ["retard", "retahd", "ret6"]:
            self.countDict[key] = "retard"
        for key in ["thank", "ty", "thx", "appreciate it", "appreciate that", "tyvm"]:
            self.countDict[key] = "thanks"


    def sqlCounterIntAdder(self, countColumn: str, countAddend: int):
        mek(purpose="increment", table="userstats", resultColumn=countColumn+"count",
        queryColumn="serveriduserid", queryField=self.queryField, insertData=countAddend,
        intOp="+")
    
    def sqlCounterNameUpdater(self):
        mek(purpose="update", table="userstats", queryColumn="serveriduserid",
        resultColumn="username", queryField=self.queryField, insertData=f'"{self.username}"')

#  updateSql = ("INSERT INTO " + table + "(" + queryColumn + "," + 
#     resultColumn + ") VALUES (\"" + queryField + "\",\"" + insertData +
#     "\") ON DUPLICATE KEY UPDATE " + resultColumn + " = \"" + insertData + "\"")