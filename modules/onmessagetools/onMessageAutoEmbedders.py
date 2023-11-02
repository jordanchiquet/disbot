from modules import randomhelpers as rh

class OnMessageAutoEmbedder:

    def __init__(self, msgContent: str):
        self.msgContent = msgContent
        self.twitterOrX = ""
        self.usableLink = ""

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
        if "twitter.com" in self.msgContent and "vxtwitter.com" not in self.msgContent:
            self.twitterOrX = r"twitter"
            return True
        if "x.com" in self.msgContent:
            self.twitterOrX = r"x"
            return True
        else:
            return False
    
    def isInstagramUrl(self) -> bool:
        if "instagram.com" in self.msgContent:
            self.twitterOrX = r"instagram"
            return True

    
    def getEmbedUrl(self) -> str:
        usableLinkSearch = rh.getRegexReturn(query=r"\S+"+self.twitterOrX+r"\.com/\S+", input=self.msgContent)
        if usableLinkSearch == None:
            print("onMessageAutoEmbedders no usable link found")
            return None
        else:
            self.usableLink = usableLinkSearch.group()

        fxTwitterLink = self.usableLink.split(".com/")[1]
        embedUrl = "https://vxtwitter.com/" + fxTwitterLink
        return embedUrl
    
    def getTwitterEmbedUrl(self) -> str:
        usableLinkSearch = rh.getRegexReturn(query=r"\S+"+self.twitterOrX+r"\.com/\S+", input=self.msgContent)
        if usableLinkSearch == None:
            print("onMessageAutoEmbedders no usable link found")
            return None
        else:
            self.usableLink = usableLinkSearch.group()
        fxTwitterLink = self.usableLink.split(".com/")[1]
        embedUrl = "https://vxtwitter.com/" + fxTwitterLink
        return embedUrl


    def isEmbeddedMediaVideo(self) -> bool:
        pass

