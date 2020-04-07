from modules.bingimageapi import bingimage
from modules.googleimageapi import imageget
from modules.googleapi import googleget
from modules.listemptystring import listemptystring
from modules.merriamapi import getmeaning
from modules.removefirstindex import removefirstindex
from modules.youtube import youtubesearch


class heycomputer:
    def __init__(self, msgcontent):
        self.msgcontent = (msgcontent.replace(".","")).lower()
        self.msglist = msgcontent.split(" ")
    

    def execute(self):
        print("EXECUTING HEYCOMPUTER")
        getintentresult = self.getintenttext()
        intentparams = getintentresult.split("|")
        print("intentparams: [" + str(intentparams) + "]")
        if getintentresult == "inv":
            print("INTENT WAS INVALID")
            return("inv")
        parseforimagelist = self.parseforimage(self.msglist[0]).split("|")
        if parseforimagelist[0] == "True":
            print("executing heycomputer image search")
            return(self.imageexecute(parseforimagelist[1]))
        elif (self.parsefordefinition().split("|"))[0] == "True":
            print("executing heycomputer merriam webster")
            return(self.definitionexecute())
        elif self.parseforsearch() == True:
            print("parseforsearch was true")
            print("executing heycomputer search")
            return(self.searchexecute())
        elif self.parseforvid(self.msglist[0]) == True:
            print("executing hey computer youtube search")
            return(self.videoexecute)
        elif self.msglist[0] == "terminate":
            return("terminate")
        elif self.msglist[0] == "speed":
            return(self.speedexecute())
        else:
            return(self.nointent(intentparams))


    def getintenttext(self):
        print("starting getintenttext")
        getintentlist1 = ["ay", "ayo", "ayy", "ayyy", "hey", "hello", "hi", "hola", "yo", "comp", "computer", "compadre",
                    "machine", "renard", "retard", "bot", "robot", "please", "fucking", "fuckin", "freaking", "frikking", 
                    "freakin", "frikkin", "go", "a", "head", "ahead", "and", "give", "get", "do"]
        fallbacktoimagesearch = "0"
        loadpull = "0"
        look = "0"
        can = "0"
        for x in getintentlist1:
            if self.msglist[0] == x:
                self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "can":
            can = "1"
            self.msglist = removefirstindex(self.msglist)
            if self.msglist[0] == "i" or self.msglist[0] == "we":
                self.msglist = removefirstindex(self.msglist)
                if self.msglist[0] == "get" or self.msglist[0] == "have":
                    self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "load" or self.msglist[0] == "pull" or self.msglist[0] == "laod" or self.msglist[0] == "lod":
            print("self.msglist[0] was load")
            loadpull = "1"
            self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "look":
            print("self.msglist[0] was look")
            look = "1"
            self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "show" or (self.msglist[0] == "let" and self.msglist[2] == "see"):
            fallbacktoimagesearch = "1"
            self.msglist = removefirstindex(self.msglist)
        getintentlist2 = ["2", "to", "too", "i", "me", "us", "we", "this", "these", "those"]
        for x in getintentlist2:
            if self.msglist[0] == x:
                self.msglist = removefirstindex(self.msglist)
        getintentlist3 = ["asshole", "fuckin", "freakin", "frikkin", "jabroni"]
        for x in getintentlist3:
            if (self.msglist[0]).startswith(x):
                self.msglist = removefirstindex(self.msglist)
        getintentlist4 = ["see", "up", "the", "a", "an"]
        for x in getintentlist4:
            if self.msglist[0] == x:
                self.msglist = removefirstindex(self.msglist)
        finalentryindex = len(self.msglist) - 1
        if self.msglist[finalentryindex] == "me":
            print("finalentryindex was me... checking for \"for\"")
            penultimateentryindex = finalentryindex - 1
            if self.msglist[penultimateentryindex] == "for":
                print("penultimate index was for and last index was me. deleting both.")
                del self.msglist[penultimateentryindex]
                del self.msglist[penultimateentryindex]
                print("new self.msglist after deletion: [" + str(self.msglist) + "]")
        if len(self.msglist) < 1:
            return("inv")            
        else:
            return(fallbacktoimagesearch + "|" + loadpull + "|" + look + "|" + can)


    def canexecute(self):
        print("starting canexecute with self.msglist[0]: [" + self.msglist[0] + "]")
        if (self.msglist[0] == "hot" and self.msglist[1] == "tub") or (self.msglist[0] == "hottub"):
            return("this robot is in NO WAY associated with State Farm but... keep this between us https://youtu.be/Dkvy6K4CwbM")


    def definitionexecute(self):
        if self.msglist[0] == "of":
            removefirstindex(self.msglist)
            if self.msglist[0] == "being" and self.msglist[1] == "lonely":
                return("I know this feeling very well...\nhttps://youtu.be/8L-H7TIRRSs")
        definitionquery = " ".join(self.msglist)
        print("starting definition get with query: [" + definitionquery + "]")
        return(getmeaning(definitionquery))
    
        
    def imageexecute(self, filetype, genericsearch: bool = False):  
        imagecmdlistfull = ["img", "image", "photo", "photograph", "pic", "picture", "snapshot", "bmp", "gif", "jpg", "jpeg", "png",
                            "search", "find", "recon", "seek", "for", "of", "a", "an"]
        for x in imagecmdlistfull:
            if self.msglist[0] == x:
                print("self.msglist[0] in imagecmdlist, removing")
                self.msglist = removefirstindex(self.msglist)
        if len(self.msglist) < 1:
            return("inv")
        print("filetype is: [" + filetype + "]")
        if filetype == "" or filetype == "nonspecific":
            imgquery = " ".join(self.msglist)
            print("starting bingimage with query: [" + imgquery + "]")
            return(bingimage(imgquery))
        else:
            imgquery = " ".join(self.msglist)
            print("starting bingimage with query: [" + imgquery + "]")
            return(imageget(imgquery, filetype))
    

    def searchexecute(self):
        googlequery = " ".join(self.msglist)
        print("starting googleget get with query: [" + googlequery + "]")
        return(googleget(googlequery))


    def parsefordefinition(self):
        pfdlist = ["def", "define", "definition", "meaning"]
        for x in pfdlist:
            if self.msglist[0] == x:
                self.msglist = removefirstindex(self.msglist)
                return("True|notwhat")
        if self.msglist[0].startswith("what") or \
        self.msglist[0].startswith("waht") or \
        self.msglist[0] == "wat" or \
        self.msglist[0] == "wats":
            self.msglist = removefirstindex(self.msglist)
            if self.whatparse() == "whatsthemeaningofthis":
                return("False|whatsthemeaningofthis")
            elif self.whatparse() == "whatif":
                return("True|whatif")
            else:
                return("True|nonspecial")
        else:
            return("False|artificialnull")
    

    def parseforimage(self, intenttext):
        print("starting parseforimage with keyword: [" + intenttext + "]")
        imagecmdlist = ["img", "image", "photo", "photograph", "pic", "picture", "snapshot", "bmp", "gif", "jpg", "jpeg", "png"]
        filetypelist = ["bmp", "gif", "jpg", "jpeg", "png"]
        for x in imagecmdlist:
            if intenttext == x:
                print("self.msglist[0] was found in imagecmdlist: [" + intenttext + "]")
                isimagecmd = "True"
                specificfilesearch = "nonspecific"
                break
        else:
            for x in filetypelist:
                if intenttext == x:
                    print("self.msglist[0] was found in filetypelist: [" + intenttext + "]")
                    isimagecmd = "True"
                    specificfilesearch = intenttext
                    break
            else:
                print("self.msglist[0] was not image command, isimagecmd to False, specificfilesearch to blank")
                isimagecmd = "False"
                specificfilesearch = ""
        return(isimagecmd + "|" + specificfilesearch)


    def parseforsearch(self):
        print("starting parseforsearch with keyword: [" + self.msglist[0] + "]")
        searchcmdlist = ["bing", "google", "search", "find"]
        search = False
        for x in searchcmdlist:
            if self.msglist[0] == x:
                removefirstindex(self.msglist)
                search = True
                break
        if self.msglist[0] == "for" or self.msglist[0] == "of":
            removefirstindex(self.msglist)
        return(search)
    

    def parseforvid(self, intenttext):
        print("starting parse for vid with keyword: [" + intenttext + "]")
        vid = False
        if intenttext.startswith("vid") or intenttext.startswith("movie") or intenttext == "youtube" or intenttext == "yt":
            vid = True
        return(vid)


    def nointent(self, intentparams):
        parseforimagelist = self.parseforimage(self.msglist[len(self.msglist) - 1]).split("|")
        if parseforimagelist[0] == "True":
            print("executing heycomputer image search")
            del self.msglist[len(self.msglist) - 1]
            return(self.imageexecute(parseforimagelist[1]))
        elif self.parseforvid(self.msglist[len(self.msglist) - 1]) == True:
            del self.msglist[len(self.msglist) - 1]
            return(self.videoexecute())
        elif intentparams[0] == "1":
            if self.msglist[0] == "way" and len(self.msglist) == 1:
                return("my queen?")
            return(self.imageexecute("nonspecific"))
        elif intentparams[1] == "1":
            return(self.searchexecute())
        elif intentparams[2] == "1":
            return(self.definitionexecute())
        elif intentparams[3] == "1":
            return(self.canexecute())
        else:
            return("I didn't understand your command because I'm retarded and Jordan gave me a very small vocabulary!")


    def speedexecute(self):
        if self.msglist[1] == "me":
            if self.msglist[2] == "up":
                return("https://youtu.be/dCuCpVPkWDY")
            if self.msglist[2] == "down":
                return("https://youtu.be/iALO4L166WU")
    

    def videoexecute(self):
        vidcmdlist = ["vid", "video", "movie", "movies", "youtube", "youtubes", "yt", "of", "a", "an"]
        for x in vidcmdlist:
            if self.msglist[0] == x:
                removefirstindex(self.msglist)
        vidquery = " ".join(self.msglist)
        return(youtubesearch(vidquery))
        


    def whatparse(self):
        whatlist1 = ["is", "a", "an"]
        for x in whatlist1:
            if self.msglist[0] == x:
                removefirstindex(self.msglist)
        whatlist2 = ["definition", "meaning", "of"]
        if self.msglist[0] == "the":
            for x in whatlist2:
                if self.msglist[0] == x:
                    removefirstindex(self.msglist)
                    if self.msglist[0].startswith("this"):
                        removefirstindex(self.msgcontent)
                        if len(self.msgcontent) < 1:
                            return("whatsthemeaningofthis")
        if self.msglist[0] == "if":
            return("whatif")


