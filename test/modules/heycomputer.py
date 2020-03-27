from modules.googleimageapi import imageget
from modules.googleapi import googleget
from modules.definitionwebscrape import getdefinition
from modules.listemptystring import listemptystring
from modules.removefirstindex import removefirstindex


class heycomputer:
    def __init__(self, msgcontent):
        self.msgcontent = msgcontent.replace(".","")
    

    def heycomputerexecute(self):
        print("starting defineintent from heycomputer flow")
        getintentresult = self.getintenttext()
        if getintentresult == "inv":
            print("getintentresult was inv, returning inv")
            return("inv")
            #come back to this
        getintentresultlist = getintentresult.split("|")
        nocmdimagesearch = getintentresultlist[0]
        print("nocmdimagesearch: [" + nocmdimagesearch + "]")
        intentkeyword = getintentresultlist[1].split(" ")[0]
        msglist = self.msgcontent.split(" ")
        intentindex = msglist.index(intentkeyword)
        print("intentkeyword: [" + intentkeyword + "]")
        parseforimageresult = self.parseforimage(intentkeyword)
        if parseforimageresult.split("|")[0] == "True":
            print("command is for image.")
            imagefiletype = parseforimageresult.split("|")[1]
            imageresult = self.imageexecute(intentindex, imagefiletype)
            return(imageresult)
        print("escaped")
        parsefordefinitionresult = self.parsefordefinition(intentkeyword)
        if parsefordefinitionresult == True:
            print("command is for defintion")
            definitionresult = self.definitionexecute(intentkeyword)
            return("~" + definitionresult)
        if intentkeyword == "do":
            doresult = self.doexecute(intentkeyword)
            return(doresult)
        else:
            if nocmdimagesearch == "True":
                imageresult = self.imageexecute(intentindex, "nonspecific", True)
                return(imageresult)
            else:
                #add other conditions
                imageresult = self.imageexecute(intentindex, "nonspecific", True)
                return(imageresult)

        # parsefordefinitionresult


    def getintenttext(self):
        print("starting getintenttext")
        msg = (self.msgcontent).lower()
        msgspacesplit = msg.split(" ")
        nocmdimagesearch = "False"
        if msgspacesplit[0] == "ay" or msgspacesplit[0] == "ayo":
            print("msgspacesplit[0] was ay or ayo, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "hey" or msgspacesplit[0] == "hello" or msgspacesplit[0] == "hi" or msgspacesplit[0] == "hola" or msgspacesplit[0] == "yo":
            print("msgspacesplit[0] was hey or hello or hi or hola, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0].startswith("comput") or msgspacesplit[0].startswith("compadre") or msgspacesplit[0].startswith("machine") or msgspacesplit[0].startswith("renard"):
            print("msgspacesplit[0] startwith variation of computer or renard name, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "go":
            print("msgspacesplit[0] was go, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "ahead":
            print("msgspacesplit[0] was ahead, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "and":
            print("msgspacesplit[0] was and, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "download":
            print("msgspacesplit[0] was download, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "load" or msgspacesplit[0] == "give" or msgspacesplit[0] == "look" or msgspacesplit[0] == "pull":
            print("msgspacesplit[0] was load or give, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "to":
            print("msgspacesplit[0] was to, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "show" or msgspacesplit[0] == "let":
            print("msgspacesplit[0] was show, deleting msgpacesplit [0] and declaring nocmdimagesearch boolean as true")
            nocmdimagesearch = "True"
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == ("to") or msgspacesplit[0] == "too":
            print("msgspacesplit[0] was to or too, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)                 
        if msgspacesplit[0] == "me" or msgspacesplit[0] == "us" or msgspacesplit[0] == "we" or msgspacesplit[0] == "i":
            print("msgspacesplit[0] was me or us or we or i, deleting msgspacesplit[0]")
            msgspacesplit = removefirstindex(msgspacesplit)
            if msgspacesplit[0] == "see":
                print("msgspacesplit[0] was see, deleting msgspacesplit[0]")
                msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "up":
            print("msgspacesplit[0] was up, deleting msgspacesplit[0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "the":
            print("msgspacesplit[0] was the, deleting msgspacesplit[0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "a" or msgspacesplit[0] == "an":
            print("msgspacesplit[0] was a or an, deleting msgspacesplit[0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if len(msgspacesplit) < 1:
            return("inv")            
        else:
            return(nocmdimagesearch + "|" + " ".join(msgspacesplit))


    def definitionexecute(self, definitioncommandsplitpoint):
        definitionqueryorig = self.msgcontent.split(definitioncommandsplitpoint)[1]
        definitionquerylist = definitionqueryorig.split(" ")
        definitionquerylist = listemptystring(definitionquerylist)
        if definitioncommandsplitpoint.startswith("what") or \
        definitioncommandsplitpoint.startswith("waht") or \
        definitioncommandsplitpoint == "wat" or \
        definitioncommandsplitpoint == "wats":
            print("splitpoint was what... checking for is")
            if definitionquerylist[0] == "if":
                print("if parse")
            if definitionquerylist[0] == "is":
                print("definitionquerylist[0] is is, deleting from defintionquerylist[0]")
                definitionquerylist = removefirstindex(definitionquerylist)
        # if definitioncommandsplitpoint == "look":
        #     print("definitionquerylist[0] is look, deleting from defintionquerylist[0]")
        #     definitionquerylist = removefirstindex(definitionquerylist)
        #     if definitioncommandsplitpoint == "up":
        #         print("definitionquerylist[0] is up, deleting from defintionquerylist[0]")
        #         definitionquerylist = removefirstindex(definitionquerylist)
        if definitionquerylist[0] == "of":
            print("definitionquerylist[0] is of")
            definitionquerylist = removefirstindex(definitionquerylist)
        if definitionquerylist[0] == "a" or definitionquerylist[0] == "an":
            print("definitionquerylist[0] is a or an, deleting from definitionquerlist[0]")
            definitionquerylist = removefirstindex(definitionquerylist)
        finalentryindex = len(definitionquerylist) - 1
        if definitionquerylist[finalentryindex] == "me":
            print("finalentryindex was me... checking for \"for\"")
            penultimateentryindex = finalentryindex - 1
            if definitionquerylist[penultimateentryindex] == "for":
                print("penultimate index was for and last index was me. deleting both.")
                del definitionquerylist[penultimateentryindex]
                del definitionquerylist[penultimateentryindex]
                print("new definitionquerylist after deletion: [" + str(definitionquerylist) + "]")
        definitionquery = " ".join(definitionquerylist)
        print("starting definition get with query: [" + definitionquery + "]")
        return(getdefinition(definitionquery))


    def doexecute(self, dosplitpoint):
        msglist = self.msgcontent.split(" ")
        doqueryorig = self.msgcontent.split(dosplitpoint)[1]
        doquerylist = doqueryorig.split(" ")
        doquerylist = listemptystring(doquerylist)
        if doquerylist[0] == "a" or doqueryorig[0] == "an":
            print("doquerylist[0] was a or an, deleting first index]")
            doquerylist = removefirstindex(doquerylist)
        parseforimageresult = self.parseforimage(doquerylist[0])
        if parseforimageresult.split("|")[0] == "True":
            print("doquerylist[0] was image or filetype, setting imagesplit as doquerylist[0]")
            if doquerylist[0] == "search":
                print("doquerylist[0] was search, deleting first index]")
                doquerylist = removefirstindex(doquerylist)
            if doquerylist[0] == "for" or doquerylist[0] == "of":
                print("doquerylist[0] was search, deleting first index]")
                doquerylist = removefirstindex(doquerylist)
            imagefiletype = parseforimageresult.split("|")[1]
            imgquerystart = doquerylist[0]
            imgqueryindex = msglist.index(imgquerystart)
            imageresult = self.imageexecute(imgqueryindex, imagefiletype)
            return(imageresult)
        if doquerylist[0] == "search":
            print('generic search execute')
            doqueryindex = msglist.index(doquerylist[0])
            dosearchresult = self.searchexecute(doqueryindex)
            print("dosearchresult: [" + dosearchresult + "]")
            return(dosearchresult)
    
        
    def imageexecute(self, imagecommandsplitpoint, filetype, genericsearch: bool = False):
        imgqueryorig = self.msgcontent.split(" ")
        imgquerylist = imgqueryorig[imagecommandsplitpoint:]
        print("starting imgquerylist: [" + str(imgquerylist) + "]")
        imgquerylist = listemptystring(imgquerylist)    
        for x in imagecmdlistfull:
            if imgquerylist[0] == x:
                print("imgquerylist[0] in imagecmdlist, removing")
                imgquerylist = removefirstindex(imgquerylist)
                continue
        for x in searchcmdlistfull:
            if imgquerylist[0] == x:
                print("imgquerylist[0] in searchcmdlist, removing")
                imgquerylist = removefirstindex(imgquerylist)
                continue    
        if imgquerylist[0] == "of" or imgquerylist[0] == "from" or imgquerylist[0] == "for":
        #do something special for "from" later... search specific site or location
            print("imgquerylist[0] was of or from or for, deleting imgquerylist[0]")
            imgquerylist = removefirstindex(imgquerylist)
        if imgquerylist[0] == "a" or imgquerylist == "an":
            print("imgquerylist[0] was a or an, deleting imgquerylist[0]")
            imgquerylist = removefirstindex(imgquerylist)
        finalentryindex = len(imgquerylist) - 1
        if imgquerylist[finalentryindex] == "me":
            print("finalentryindex was me... checking for \"for\"")
            penultimateentryindex = finalentryindex - 1
            if imgquerylist[penultimateentryindex] == "for":
                print("penultimate index was for and last index was me. deleting both.")
                del imgquerylist[penultimateentryindex]
                del imgquerylist[penultimateentryindex]
                print("new definitionquerylist after deletion: [" + str(imgquerylist) + "]")
        if len(imgquerylist) < 1:
            return("inv")
        else:
            imgquery = " ".join(imgquerylist)
            print("starting imageget with query: [" + imgquery + "]")
            return(imageget(imgquery, filetype))
    

    def searchexecute(self, searchsplitpoint):
        print("starting searchexecute")
        searchqueryorig = self.msgcontent.split(" ")
        searchquerylist = searchqueryorig[searchsplitpoint:]
        print("starting searchquerylist: [" + str(searchquerylist) + "]")
        searchquerylist = listemptystring(searchquerylist)
        for x in searchcmdlistfull:
            if searchquerylist[0] == x:
                print("searchquerylist[0] in searchcmdlist, removing")
                searchquerylist = removefirstindex(searchquerylist)
                continue
        print("escaped searchexecute searcmd loop")
        if searchquerylist[0] == "up":
            print("searchquerylist[0] was up, deleting searchquerylist[0]")
            searchquerylist = removefirstindex(searchquerylist)
        if searchquerylist[0] == "a" or searchquerylist[0] == "an":
            print("searchquerylist[0] was a or an, deleting searchquerylist[0]")
            searchquerylist = removefirstindex(searchquerylist)
        if searchquerylist[0] == "for" or searchquerylist[0] == "of":
            print("searchquerylist[0] was for or of, deleting searchquerylist[0]")
            searchquerylist = removefirstindex(searchquerylist)
        msglist = self.msgcontent.split(" ")
        transitiontoimage = self.parseforimage(searchquerylist[0])
        print("transition to image sanity: [" + transitiontoimage + "]")
        print("made it out of image check after searchexecute")
        searchqueryindex = msglist.index(searchquerylist[0])
        print("searchqueryindex: [" + str(searchqueryindex) + "]")
        print("that index is: [" + msglist[searchqueryindex] + "]")
        if transitiontoimage.split("|")[0] == "True":
            print("generic search is for an image! transitioning to image search")
            imgfiletype = transitiontoimage[1]
            imgfromsearchres = self.imageexecute(searchqueryindex, imgfiletype)
            return(imgfromsearchres)
        else:
            print("not an image search after searchexecute :)")
        finalentryindex = len(searchquerylist) - 1
        if searchquerylist[finalentryindex] == "me":
            print("finalentryindex was me... checking for \"for\"")
            penultimateentryindex = finalentryindex - 1
            if searchquerylist[penultimateentryindex] == "for":
                print("penultimate index was for and last index was me. deleting both.")
                del searchquerylist[penultimateentryindex]
                del searchquerylist[penultimateentryindex]
                print("new searchquerylist after deletion: [" + str(searchquerylist) + "]")
        if len(searchquerylist) < 1:
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


    def parsefordefinition(self, pfdkeyword):
        if pfdkeyword == "def" or \
        pfdkeyword == "define" or \
        pfdkeyword == "definition" or \
        pfdkeyword.startswith("what") or \
        pfdkeyword.startswith("waht") or \
        pfdkeyword == "wat" or \
        pfdkeyword == "wats":
            print("pfdkeyword was def or define or defintion or started with what or was look, returning True")
            return True
        else:
            return False
    

    def parseforimage(self, pfikeyword):
        print("starting parseforimage")
        print("pfikeyword: [" + pfikeyword + "]")
        if pfikeyword == "img" or pfikeyword == "image" or pfikeyword =="photo" or pfikeyword == "photograph" or pfikeyword == "pic" or pfikeyword == "picture" or pfikeyword == "snapshot":
            print("pfikeyword was img or image or photo or photograph or pic or picture or snapsho, setting isimage cmd to True, specificfilesearch to nonspecific")
            isimagecmd = "True"
            specificfilesearch = "nonspecific"
        elif pfikeyword == "bmp" or pfikeyword == "gif" or pfikeyword == "jpeg" or pfikeyword == "jpg" or pfikeyword == "png":
            print("pfikeyword was an image filetype, setting isimagecmd to True, specificfilesearch to pfikeyword")
            isimagecmd = "True"
            specificfilesearch = pfikeyword
            print("specificfilesearch: [" + specificfilesearch + "]")
        else:
            print("pfikeyword was not image command, isimagecmd to False, specificfilesearch to blank")
            isimagecmd = "False"
            specificfilesearch = ""
        return(isimagecmd + "|" + specificfilesearch)


imagecmdlistfull = ["img", "image", "photo", "photograph", "pic", "picture", "snaphot", "bmp", "gif", "jpg", "jpeg", "png"]
searchcmdlistfull = ["bing", "google", "g", "ggl", "gogle", "duckduckgo", "search", "look"]