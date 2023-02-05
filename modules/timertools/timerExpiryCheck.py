from modules.timertools.timerSQL import timerRead, expiryRemove
from datetime import datetime, timedelta

from modules.randomhelpers import getCSTOffsetTime

def expiryCheck():
    print("starting expiryCheck")
    results = timerRead()
    output = ["noshow"]
    if results is not None:
        for result in results:
            resultDate = datetime.strptime(result[2], "%Y-%m-%d %H:%M:%S.%f")
            if resultDate <= getCSTOffsetTime():
                print("time " + result[2] + " expired")
                expiryRemove(result[0])
                print("debug line weasel man 99")
                output = ["showtime", result[4], notifyFormatGetter(result[1]), 
                result[2], result[3]]
                print("exiting expiryCheck with output: ["
                + str(output) + "]")
                return(output)
        return(output)
    else:
        return(output)
    

def notifyFormatGetter(userids: str):
    if "|" in userids:
        useridList = userids.split("|")
        for index, item in enumerate(useridList):
            item = "<@!" + item +">"
            useridList[index] = item
        notifyFormatGot = (("; ".join(useridList)) + " ")
    else:
        notifyFormatGot = "<@!" + userids +"> "
    print("notifyFormatGetter returning: [" + notifyFormatGot + "]")
    return(notifyFormatGot)
