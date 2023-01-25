
from modules.sqlHandler import sqlMektanixDevilDog as Mektanix




def defaultRead(userid: str):
    print("defaultRead in timerSQL started")
    return(Mektanix(purpose="read", table="userdata", 
    resultColumn="timerdefault", queryColumn="userid", queryField=userid))

def defaultWrite(userid: str, inputData: str):
    print("defaultWrite in timerSQL started")
    return(Mektanix("update", "userdata", "timerdefault", "userid", userid, insertData = inputData))

def timerWrite(inputDataTuple: tuple):
    """
    write timer to SQL
    :param tuple inputDataTuple: userid, timer's expiry, timernote in that order
    """
    print("timerWrite in timerSQL started")
    # return(Mektanix(purpose="insert", table="timers", ))
    return(Mektanix(purpose="insert", table="timers", 
    insertColumn = ("(userid, notifychannel, expiry, note)"), 
    insertData = str(inputDataTuple)))

def timerRead():
    print("timerRead in timerSQL started")
    return(Mektanix(purpose="getall", table="timers"))

def expiryRemove(id: int):
    print("expiryRemove in timerSQL started")
    return(Mektanix(purpose="deleterow", table="timers",
    queryColumn="idtimers", queryField=id))

def getTimerId(expiryTime: str):
    print("getTimerId in timerSQL started")
    return(Mektanix(purpose="read", table="timers", resultColumn="idtimers",
    queryColumn="expiry", queryField=expiryTime))

def addNotifyUsers(id: int, userid: str):
    print("addNotify in timerSQL started")
    return(Mektanix(purpose="append", table="timers", resultColumn="userid",
    queryColumn="idtimers", queryField=id, insertData="|" + userid))

def getNotifyUsers(id: int):
    print("getNotifyUsers in timerSQL started")
    return(Mektanix(purpose="read", table="timers", resultColumn="userid",
    queryColumn="idtimers", queryField=id))

def removeNotifyUser(timerid: int, userid: str):
    print("string check " + userid)
    currentNotifys = getNotifyUsers(timerid)
    print(currentNotifys)
    afterNotifys = currentNotifys[0].replace("|" + userid, "")
    (Mektanix(purpose="update", table="timers", queryColumn="idtimers",
    queryField=timerid, resultColumn="userid", insertData=f'"{afterNotifys}"'))
    return(timerid)
    # updateSql = ("INSERT INTO " + table + "(" + queryColumn + "," + 
    # resultColumn + ") VALUES (\"" + queryField + "\",\"" + insertData +
    # "\") ON DUPLICATE KEY UPDATE " + resultColumn + " = \"" + insertData + "\"")