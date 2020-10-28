from modules.renardusers import renardusers

class wordcounter:

    def __init__(self, userid, serverid, username, message: str = None, nicktally: bool = False, reacttally: bool = False):
        # super().__init__()
        self.userid = userid
        self.serverid = serverid
        self.username = username
        self.message = message
        self.nicktally = nicktally
        self.reacttally = reacttally


    def countprocessor(self):
        if self.nicktally:
            self.counter("nicknames", 1)
            return
        if self.reacttally:
            self.counter("reactions", 1)
            return
        self.counter("msgcount", 1)
        self.counter("wordcount", None, " ")
        if "fuck" in self.message:
            self.counter("fuckcount", None, "fuck")
        if "in any case" in self.message:
            self.counter("inanycase", None, "in any case")
        if "no" in self.message:
            self.counter("nocount", None, "no ")
            self.counter("nocount", None, "no.")
            self.counter("nocount", None, "no!")
            self.counter("nocount", None, "no?")
            self.counter("nocount", None, "no,")
        if "no" == self.message:
            self.counter("nocount", None, "no")
        if "nah" in self.message:
            self.counter("nocount", None, "nah")
        if "yes" in self.message:
            self.counter("yescount", None, "yes ")
            self.counter("yescount", None, "yes.")
            self.counter("yescount", None, "yes!")
            self.counter("yescount", None, "yes?")
            self.counter("yescount", None, "yes,")
        if "yah" in self.message:
            self.counter("yescount", None, "yah ")
        if "yee" in self.message:
            self.counter("yescount", None, "yee ")
        if "dude" in self.message:
            self.counter("dudecount", None, "dude")
        if self.message.startswith(".img"):
            self.counter("imgsearchcount", 1)
        if "like" in self.message:
            self.counter("likecount", None, "like")
        southlist = ["yall", "ya'll", "y'all", "aint", "ain't", "he don't", "she don't", "he dont", "she dont" "it dont", "it don't", "not no", "dont got", "don't got", "they was", "we was", "you was",
        "up a storm", "yonder", "that dont", "that don't", "lick of sense", "reckon", "fixin to", "fixing to", "fixin' to", "finna", "bowed up", "hanker", "howdy", "lickety", "ornery", "purdy", "purty", "rile", "riling",
        "skidaddle", "skedaddle", "skidaddling", "skedaddling", "tarnation", "varmint", "yankee", "crawfish", "we's", "we is", "theys", "they is", "they's", "them dudes", "lagniappe", "mawmaw", "pawpaw", "cross the way",
        "damn near"]
        issouth = [s for s in southlist if(s in self.message)]
        if issouth:
            self.counter("southcount", 1)

    def counter(self, countfield, tallycount: int = None, countstring: str = None):
        countinit = renardusers(self.userid, countfield, username=self.username, serverid=self.serverid)
        if tallycount is None:
            tallycount = (self.message).count(countstring)
        if countfield == "wordcount":
            tallycount = tallycount + 1
            if self.message.startswith("."):
                tallycount = tallycount - 1
        if countfield == "fuckcount":
            if self.message.startswith(".fuck"):
                tallycount = tallycount - 1
        if tallycount != 0:
            for num in range(tallycount):
                countinit.userintwrite()