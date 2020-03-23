from modules.googleimageapi import imageget
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
            print("doparsegohere")
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
        if msgspacesplit[0] == "hey" or msgspacesplit[0] == "hello" or msgspacesplit[0] == "hi" or msgspacesplit[0] == "hola":
            print("msgspacesplit[0] was hey or hello or hi or hola, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0].startswith("comput") or msgspacesplit[0].startswith("compadre") or msgspacesplit[0].startswith("machine") or msgspacesplit[0].startswith("renard"):
            print("msgspacesplit[0] startwith variation of computer or renard name, deleting msgpacesplit [0]")
            msgspacesplit = removefirstindex(msgspacesplit)
        if msgspacesplit[0] == "load" or msgspacesplit[0] == "give":
            print("msgspacesplit[0] was load or give, deleting msgpacesplit [0]")
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
        if msgspacesplit[0] == "a" or msgspacesplit[0] == "an":
            print("msgspacesplit[0] was a or an, deleting msgspacesplit[0]")
            msgspacesplit = removefirstindex(msgspacesplit)

        if len(msgspacesplit) < 1:
            return("inv")             
        else:
            return(nocmdimagesearch + "|" + " ".join(msgspacesplit))


    def definitionexecute(self, defintioncommandsplitpoint):
        definitionqueryorig = self.msgcontent.split(defintioncommandsplitpoint)[1]
        definitionquerylist = definitionqueryorig.split(" ")
        definitionquerylist = listemptystring(definitionquerylist)
        if defintioncommandsplitpoint.startswith("what") or \
        defintioncommandsplitpoint.startswith("waht") or \
        defintioncommandsplitpoint == "wat" or \
        defintioncommandsplitpoint == "wats":
            print("splitpoint was what... checking for is")
            if definitionquerylist[0] == "if":
                print("if parse")
            if definitionquerylist[0] == "is":
                print("definitionquerylist[0] is is, deleting from defintionquerylist[0]")
                definitionquerylist = removefirstindex(definitionquerylist)
        if definitionquerylist[0] == "a" or definitionquerylist[0] == "an":
            print("definitionquerylist[0] is a or an, deleting from definitionquerlist[0]")
            definitionquerylist = removefirstindex(definitionquerylist)
        definitionquery = " ".join(definitionquerylist)
        print("starting definition get with query: [" + definitionquery + "]")
        return(getdefinition(definitionquery))


    def doexecute(self, dosplitpoint):
        
    def imageexecute(self, imagecommandsplitpoint, filetype, genericsearch: bool = False):
        imgqueryorig = self.msgcontent.split(" ")
        imgquerylist = imgqueryorig[imagecommandsplitpoint:]
        print("starting imgquerylist: [" + str(imgquerylist) + "]")
        imgquerylist = listemptystring(imgquerylist)
        if genericsearch == False:
            if imgquerylist[0] == "of" or imgquerylist[0] == "from":
            #do something special for "from" later... search specific site or location
                print("imgquerylist[0] was of or from, deleting imgquerylist[0]")
                imgquerylist = removefirstindex(imgquerylist)
        if imgquerylist[0] == "a" or imgquerylist == "an":
            print("imgquerylist[0] was a or an, deleting imgquerylist[0]")
            imgquerylist = removefirstindex(imgquerylist)
        if len(imgquerylist) < 1:
            return("inv")
        else:
            imgquery = " ".join(imgquerylist)
            print("starting imageget with query: [" + imgquery + "]")
            return(imageget(imgquery, filetype))


    def parsefordefinition(self, pfdkeyword):
        if pfdkeyword == "def" or \
        pfdkeyword == "define" or \
        pfdkeyword == "definition" or \
        pfdkeyword.startswith("what") or \
        pfdkeyword.startswith("waht") or \
        pfdkeyword == "wat" or \
        pfdkeyword == "wats":
            print("pfdkeyword was def or define or defintion or started with what, returning True")
            return True
        else:
            return False
    

    def parseforimage(self, pfikeyword):
        print("starting parseforimage")
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


