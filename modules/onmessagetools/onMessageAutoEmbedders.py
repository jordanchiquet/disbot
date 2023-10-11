from modules import randomhelpers as rh

class OnMessageAutoEmbedder:

    def __init__(self, msgContent: str):
        self.msgContent = msgContent
        self.twitterOrX = ""

    def autoEmbedderMain(self):
        if self.containsDotCom():
            if self.isTwitterUrl():
                embedUrl = self.getEmbedUrl()
                return embedUrl


    def containsDotCom(self) -> bool:
        if ".com" in self.msgContent:
            return True
        else:
            return False

    def isTwitterUrl(self) -> bool:
        if "twitter.com" in self.msgContent:
            self.twitterOrX = r"twitter"
            return True
        if "x.com" in self.msgContent:
            self.twitterOrX = r"x"
            return True
        else:
            return False

    def getEmbedUrl(self) -> str:
        usableLink = rh.getRegexReturn(query=r"\S+f"+self.twitterOrX+r"\.com/\S+", input=self.msgContent)
        fxTwitterLink = usableLink.split(".com/")[1]
        embedUrl = "https://vxtwitter.com/" + fxTwitterLink
        return embedUrl
    