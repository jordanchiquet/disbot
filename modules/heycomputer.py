from modules.bingimageapi import bingimage
from modules.googleimageapi import imageget
from modules.googleapi import googleget
from modules.listemptystring import listemptystring
from modules.merriamapi import getmeaning
from modules.removefirstindex import removefirstindex


class heycomputer:
    def __init__(self, msgcontent):
        self.msgcontent = (msgcontent.replace(".","")).lower()
        self.msglist = msgcontent.split(" ")
    

    def execute(self):
        print("EXECUTING HEYCOMPUTER")
        getintentresult = self.getintenttext()
        if getintentresult == "inv":
            print("INTENT WAS INVALID")
            return("inv")
        getintentresultlist = getintentresult.split(":")
        fallbacktoimagesearch = getintentresultlist[1]
        parseforimagelist = self.parseforimage().split("|")
        if parseforimagelist[0] == "True":
            print("executing heycomputer image search")
            return(self.imageexecute(parseforimagelist[1]))
        elif (self.parsefordefinition().split("|"))[0] == "True":
            print("executing heycomputer merriam webster")
            return(self.definitionexecute())
        #MARK set up parse for search and clean up search execute. 
        elif self.msglist[0] == "terminate":
            return("terminate")
        elif self.msglist[0] == "speed":
            return("speed")
            # if getintentresultsplit[1] == "me":
            #     if getintentresultlist[2].split(" ")[2] == "up":
            #         return("https://youtu.be/dCuCpVPkWDY")
            #     if getintentresultlist[3].split(" ")[2] == "down":
            #         return("https://youtu.be/iALO4L166WU")

        else:
            return("nothing")


    def getintenttext(self):
        print("starting getintenttext")
        getintentlist1 = ["ay", "ayo", "ayy", "ayyy", "hey", "hello", "hi", "hola", "yo", "comp", "computer", "compadre",
                    "machine", "renard", "retard", "bot", "robot", "please", "fucking", "fuckin", "freaking", "frikking", 
                    "freakin", "frikkin", "go", "a", "head", "ahead", "and", "give", "look", "do"]
        fallbacktoimagesearch = "fallbacktoimagesearch:False"
        loadpull = "loadpull:False"
        for x in getintentlist1:
            if self.msglist[0] == x:
                self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "load" or self.msglist[0] == "pull":
            print("self.msglist[0] was load")
            loadpull = "loadpull:True"
            self.msglist = removefirstindex(self.msglist[0])
        if self.msglist[0] == "show" or (self.msglist[0] == "let" and self.msglist[2] == "see"):
            fallbacktoimagesearch = "fallbacktoimagesearch:True"
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
            return(fallbacktoimagesearch + "|" + loadpull)


    def definitionexecute(self):
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
        print("starting searchexecute")
        searchcmdlistfull = ["bing", "google", "g", "ggl", "gogle", "duckduckgo", "search", "look"]
        for x in searchcmdlistfull:
            if self.msglist[0] == x:
                print("self.msglist[0] in searchcmdlist, removing")
                self.msglist = removefirstindex(self.msglist)
        print("escaped searchexecute searcmd loop")
        if self.msglist[0] == "up":
            print("self.msglist[0] was up, deleting self.msglist[0]")
            self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "a" or self.msglist[0] == "an":
            print("self.msglist[0] was a or an, deleting self.msglist[0]")
            self.msglist = removefirstindex(self.msglist)
        if self.msglist[0] == "for" or self.msglist[0] == "of":
            print("self.msglist[0] was for or of, deleting self.msglist[0]")
            self.msglist = removefirstindex(self.msglist)
        msglist = self.msgcontent.split(" ")
        transitiontoimage = self.parseforimage()
        print("transition to image sanity: [" + transitiontoimage + "]")
        print("made it out of image check after searchexecute")
        searchqueryindex = msglist.index(self.msglist[0])
        print("searchqueryindex: [" + str(searchqueryindex) + "]")
        print("that index is: [" + msglist[searchqueryindex] + "]")
        if transitiontoimage.split("|")[0] == "True":
            print("generic search is for an image! transitioning to image search")
            imgfiletype = transitiontoimage[1]
            imgfromsearchres = self.imageexecute(imgfiletype)
            return(imgfromsearchres)
        else:
            print("not an image search after searchexecute :)")
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
            print("made it to searchexecute else")
            queryjoinindex = msglist[searchqueryindex:]
            print("queryjoinindex : [" + str(queryjoinindex) + "]")
            searchquery = " ".join(queryjoinindex)
            print("searchquery: [" + searchquery + "]")
        finalsearchresult = googleget(searchquery)
        print("finalsearchresult: [" + finalsearchresult + "]")
        return(finalsearchresult)


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
    

    def parseforimage(self):
        print("starting parseforimage with keyword: [" + self.msglist[0] + "]")
        imagecmdlist = ["img", "image", "photo", "photograph", "pic", "picture", "snapshot", "bmp", "gif", "jpg", "jpeg", "png"]
        filetypelist = ["bmp", "gif", "jpg", "jpeg", "png"]
        for x in imagecmdlist:
            if self.msglist[0] == x:
                print("self.msglist[0] was found in imagecmdlist: [" + self.msglist[0] + "]")
                isimagecmd = "True"
                specificfilesearch = "nonspecific"
                break
        else:
            for x in filetypelist:
                if self.msglist[0] == x:
                    print("self.msglist[0] was found in filetypelist: [" + self.msglist[0] + "]")
                    isimagecmd = "True"
                    specificfilesearch = self.msglist[0]
                    break
            else:
                print("self.msglist[0] was not image command, isimagecmd to False, specificfilesearch to blank")
                isimagecmd = "False"
                specificfilesearch = ""
        return(isimagecmd + "|" + specificfilesearch)


    def parseforsearch(self):
        print("starting parseforsearch with keyword: [" + self.msglist[0] + "]")
        searchcmdlist = ["bing", "google", "search"]


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



            




# def speed(self, intentkeyword):
#     if intentkeyword == "speed":
#         if getintentresultsplit[1] == "me":
#             if getintentresultlist[2].split(" ")[2] == "up":
#                 return("https://youtu.be/dCuCpVPkWDY")
#             if getintentresultlist[3].split(" ")[2] == "down":
#                 return("https://youtu.be/iALO4L166WU")



