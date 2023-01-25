import os.path, fnmatch
import random

#TODO: picgrabber master function?

def picTriggerMain(msgContent: str, serverid: int):
    print("starting picTriggerMain")
    picTriggerResult = False, ""
    folderCheck = trigMasterGeneral(folderTriggerList, msgContent, serverid)
    if folderCheck[0]:
        picTriggerResult = folderCheck
    else:
        oneOffCheck = trigMasterGeneral(oneOffTriggerList, msgContent)
        if oneOffCheck[0]:
            picTriggerResult = oneOffCheck
        else:
            soloCheck = trigMasterGeneral(soloTriggerList, msgContent)
            if soloCheck[0]:
                picTriggerResult = soloCheck
    print("picTriggerMain returning: [" + str(picTriggerResult) + "]")
    return(picTriggerResult)

def thisBitchTrigger(msgContent: str):
    print("thisBitchTriggerStarted")
    msgSanitized = msgContent.replace(",", "")
    if msgSanitized.endswith("this bitch"):
        fileFolder = ("/home/ubuntu/disbot/picfolder/bitchfolder")
        fileIntStr = folderWalker(fileFolder)
        fileName = "bitchfile" + fileIntStr
        fileName = getFileName(fileName, fileFolder)
        return(True, fileName)
    return(False, "")


def trigMasterGeneral(triggerList: list, msgContent: str, serverid: int = 1):

    print("listChecker started")
    if serverid in exceptTriggerListDict:
        for value in exceptTriggerListDict[serverid]:
            triggerList.remove(value)
    for item in triggerList:
        if item in msgContent:
            print(item + " in msgContent")
            if triggerList == soloTriggerList:
                if item != msgContent:
                    return(False, "")
            itemSanitized = item.replace(" ", "")            
            fileFolder = getFileFolder(triggerList, itemSanitized)
            if triggerList == folderTriggerList:
                fileIntStr = folderWalker(fileFolder)
                itemSanitized = itemSanitized + fileIntStr
            fileName = getFileName(itemSanitized, fileFolder)
            return(True, fileName)
    return(False, "")



def folderWalker(fileFolder: str):
    print("folderWalker started")
    print("fileFolder: [" + fileFolder + "]")
    path, dir, files = os.walk(fileFolder).__next__()
    fileMin = 1
    fileMax = len(files)
    outFile = random.randint(fileMin, fileMax) 
    print("folderWalker returning: [" + str(outFile) + "]")
    return(str(outFile))

def getFileName(fileName: str, fileFolder: str):
    print("getFileName started with fileName :[" + fileName + "]; fileFolder:[" + fileFolder + "]")
    fileName = fileName + "*"
    for root, dirs, files in os.walk(fileFolder):
        for name in files:
            if fnmatch.fnmatch(name, fileName):
                print("getFileName found file for fileName: [" + fileName + "]")
                getFileNameOut = (os.path.join(root, name))
                print("getFileName returning: [" + getFileNameOut + "]")
                return(getFileNameOut)

def getFileFolder(triggerListInUse: list, folderPrefix: str):
    print("starting getFileFolder")
    # folder = "D:/renard/disbot/picfolder/" + folderPrefix + "folder/"
    if triggerListInUse ==  folderTriggerList:
        folder = "/home/ubuntu/disbot/picfolder/" + folderPrefix + "folder"
    else:
        folder = "/home/ubuntu/disbot/picfolder/oneofffolder"
    return(folder)

folderTriggerList = [
    "bye bye",
    "your sign",
    "i see what you mean",
    "gang",
    "thanks obama",
    "vibe check"
]

oneOffTriggerList = [
    "actually,",
    "give me a hand",
    "promotion",
    "same sex",
    "stop right there",
    "yay",
    "you comin"
]

soloTriggerList = [
    "computer terminate",
    "no"
]

exceptTriggerListDict = {
    1049786065260642354: "gang"
}

    
# getFileName("byebye2*", "D:/renard/disbot/picfolder/byebyefolder")
