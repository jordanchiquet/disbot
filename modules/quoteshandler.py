

from modules.sqlHandler import sqlMektanixDevilDog as mek


def addQuote (user: str, quoteStr: str, timestamp, serverid: int, userid: int) -> bool:
    print("addQuote started")
    insertColumns = "(user, quote, timestamp, serverid, userid)"
    timestamp = str(timestamp) #test with and wihout str-ing this
    serverid, userid = str(serverid), str(userid)
    quoteStr = quoteStr.replace("\"", "'")
    user = user.split("#")[0]
    insertValues = (user, quoteStr, timestamp, serverid, userid)
    insertValues = str(insertValues)
    addQuoteOutSuccess = False, ""
    qDupeCheckOne = quoteDupeCheck(quoteStr)
    if not qDupeCheckOne[0]:
        mek(purpose="insert", table="quotes", insertColumn=insertColumns, insertData=insertValues)
        quoteId = quoteDupeCheck(quoteStr)[1]
        addQuoteOutSuccess = True
    else:
        quoteId = qDupeCheckOne[1]
        addQuoteOutSuccess = False
    addQuoteOut = (addQuoteOutSuccess, quoteId)
    print("addQuote returning: [" + str(addQuoteOut) + "]")
    return(addQuoteOut)

def quoteDupeCheck(quoteStr: str):
    print("quoteDupeCheck started")
    dupeResult = mek(purpose="read", table="quotes", resultColumn="id",
    queryColumn="quote", queryField=quoteStr)
    if dupeResult is None:
        dupe = False, ""
    else:
        dupe = True, dupeResult[0]
    print("quoteDupeCheck returning: [" + str(dupe) + "] for "
    "quote: [" + quoteStr + "]")
    return(dupe)

def getQuoteById(quoteId: str):
    print("getQuoteById started")
    resultColumns = "quote, user, timestamp"
    queryResult = mek(purpose="read", table="quotes", resultColumn=resultColumns,
    queryColumn="id", queryField=int(quoteId))
    print("getQuoteById returning: [" + str(queryResult) + "]")
    return(queryResult)

def getRandomQuote(serverId: int):
    print("getRandomQuote started")
    resultColumns = "quote, id, user, timestamp"
    queryResult = mek(purpose="random", table="quotes", resultColumn=resultColumns,
    queryColumn="serverid", queryField=serverId)
    print("getRandomQuote returning: [" + str(queryResult) + "]")
    return(queryResult)

def deleteQuote(isAdmin: bool, quoteId: str, userid: str):
    print("deleteQuote started")
    existsResult = checkExistenceAndUserById(quoteId)
    if not existsResult[0]:
        outMsg = "Could not find quote " + quoteId + "."
    else:
        if userid != existsResult[1] and not isAdmin:
            outMsg = "Only admins can delete other users' quotes."
        else:
            mek(purpose="deleterow", table="quotes", queryColumn="id",
            queryField=int(quoteId))
            outMsg = "Quote " + quoteId + " erased from the archive memory."
    print("deleteQuote returning: [" + outMsg + "]")
    return(outMsg)

def deleteQuoteByTime(timestamp: str):
    print("deleteQuoteByTime started")
    mek(purpose="deleterow", table="quotes", queryColumn="timestamp",
        queryField=timestamp)

def checkExistenceAndUserById(quoteId: str):
    print("checkExistenceById started")
    existsResult = mek(purpose="read", table="quotes", resultColumn="id, userid",
    queryColumn="id", queryField=int(quoteId))
    if existsResult is None:
        quoteExists = False, ""
    else:
        quoteExists = True, existsResult[1]
    print("checkExistenceById returning: [" + str(quoteExists) + "]")
    return(quoteExists)




