import mysql.connector #mysql-connector-python
import modules.sqlheader as sqlheader
# import sqlheader as sqlheader




def sqlMektanixDevilDog(purpose: str, table: str, resultColumn: str = None, queryColumn: str = None, 
queryField: any = None, insertColumn: any = None, insertData: any = None, intOp: str = None):
    """
    SQL master function
    :param str purpose: read, update, or insert
    :param str table: table to use
    :param str resultColumn: column we want a result for in \"read\" or want to replace in \"update\"
    :param str queryColumn: column to search for query in, to return corresponding field in resultColumn
    :param str queryField: query text that queryColumn will be pinged for
    :param any insertColumn: string or tuple, columns to insert insertData
    :param any insertData: string or tuple, data we are writing 
    """
    print("sqlMektanixDevilDog started - the Red One Lives")
    dbOpen = mysql.connector.connect(
        host = sqlheader.host,
        user = sqlheader.user,
        passwd = sqlheader.passwd,
        get_warnings = True
        )
    dbCursor = dbOpen.cursor()
    table = "renarddb." + table
    if queryField is not None and purpose != "increment":
        queryField = sqlStrValidator(queryField)
    if purpose == "append":
        mekResult = (fieldAppend(dbOpen, dbCursor, table, resultColumn, queryColumn, queryField, insertData)) #tbd
    elif purpose == "deleterow":
        mekResult = (deleteRow(dbOpen, dbCursor, table, queryColumn, queryField))
    elif purpose == "getall":
        mekResult = (tableGetAll(dbCursor, table))
    elif purpose == "increment":
        mekResult = (intValueIncrementer(dbOpen, dbCursor, table, resultColumn, queryColumn, queryField, intOp, insertData))
    elif purpose == "insert":
        print("purpose insert in sqlHandler")
        mekResult = (tableInsert(dbOpen, dbCursor, table, insertColumn, insertData))
    elif purpose == "random":
        print("purpose random in sqlHandler")
        mekResult = (getRandomRow(dbCursor, table, resultColumn, queryColumn, queryField))
    elif purpose == "read":
        print("purpose read (as read) in sqlHandler")
        mekResult = (tableRead(dbCursor, table, resultColumn, queryColumn, queryField))
    elif purpose == "update":
        print("purpose update in sqlHandler")
        mekResult = (tableUpdate(dbOpen, dbCursor, table, resultColumn, queryColumn, queryField, insertData))



    else:
        mekResult = ("invalid param for purpose (argument[0]) to sqlMektanixDevilDog")
    return(mekResult)

    
def tableRead(dbCursor, table: str, resultColumn: str, queryColumn: str, queryField: str):
    print("tableRead started in Mektanix")
    readSQL = ("SELECT " + resultColumn + " FROM " +
    table + " WHERE " + queryColumn + " LIKE " + queryField )
    print("tableRead readSQL: [" + readSQL + "]")
    dbCursor.execute(readSQL)
    result = None
    resultList = []
    resultCnt = 0
    for result in dbCursor:
        resultCnt += 1
        print(str(resultCnt) + " Mektanix Devil Dog tableRead result: [" + str(result) + "]")
        resultList.append(result)
    resultOut = result
    if len(resultList) > 1:
        resultOut = resultList
    dbCursor.close()
    print("tableRead result: [" + str(resultOut) + "]")
    return(resultOut)


def tableGetAll(dbCursor, table: str):
    print("starting tableGetAll in Mektanix")
    getAllSQL = ("SELECT * FROM " + table)
    print("getAllSQL: [" + getAllSQL + "]")
    dbCursor.execute(getAllSQL)
    result = None
    tableGetAllOutput = []
    for result in dbCursor:
        tableGetAllOutput.append(result)
    if result is None:
        print("no results in tableGetAll for table: [" + table + "]")
        tableGetAllOutput = None
    print("tableGetAll returning: {" + str(tableGetAllOutput) + "}")
    return(tableGetAllOutput)

def tableUpdate(db, dbCursor, table: str, resultColumn: str, queryColumn: str, queryField: str, insertData: str):
    print("starting Mektanix tableUpdate")
    if "," in resultColumn:
        updateColStr = ', '.join([f'{item} = VALUES({item})' for item in resultColumn.split(',')])
    else:
        updateColStr = f'{resultColumn} = VALUES({resultColumn})'

    updateSql = (f'INSERT INTO {table} ({queryColumn},{resultColumn}) VALUES ({queryField}, {insertData}) ' +
    f'ON DUPLICATE KEY UPDATE {updateColStr}')
    # updateSql = ("INSERT INTO " + table + "(" + queryColumn + "," + 
    # resultColumn + ") VALUES (\"" + queryField + "\",\"" + insertData +
    # "\") ON DUPLICATE KEY UPDATE " + resultColumn + " = \"" + insertData + "\"")
    print(f"updateSql: [{updateSql}]")
    sqlExecute(True, updateSql, dbCursor, db)

def fieldAppend(db, dbCursor, table: str, resultColumn: str, queryColumn: str, queryField, appendData):
    print("starting Mektanix fieldAppend")
    appendSQL = ("INSERT INTO " + table + "(" + queryColumn + "," + 
    resultColumn + ") VALUES (" + queryField + ",\"" + appendData +
    "\") ON DUPLICATE KEY UPDATE " + resultColumn + " = CONCAT(IFNULL(" + resultColumn + 
    ", \"\"), VALUES (" + resultColumn + "))")
    print("appendSQL: [" + appendSQL + "]")
    sqlExecute(True, appendSQL, dbCursor, db)

def deleteRow(db, dbCursor, table, queryColumn, queryField):
    print("starting Mektanix deleteRow)")
    deleteRowSQL = ("DELETE FROM " + table + " WHERE " + queryColumn + "=" + queryField)
    print("deleteRowSQL: [" + deleteRowSQL + "]")
    sqlExecute(True, deleteRowSQL, dbCursor, db)

def tableInsert(db, dbCursor: object, table: str, insertColumn, insertData):
    print("starting Mektanix tableInsert")
    insertSql = ("INSERT IGNORE INTO " + table + " " + (str(insertColumn)).replace("\"","") + " VALUES " + str(insertData))
    print("insertSql: [" + insertSql + "]")
    result = sqlExecute(True, insertSql, dbCursor, db)
    return(result)

def intValueIncrementer(db, dbCursor, table: str, resultColumn: str, queryColumn: str, queryField, operation: str, amount: int):
    print("starting Mektanix intValueIncrementer")
    amountIn = str(amount)
    incrementSql = ("INSERT INTO " + table + " (" + queryColumn + ", " + resultColumn + ") VALUES (\"" +
    queryField + "\","  + amountIn + ") ON DUPLICATE KEY UPDATE " + resultColumn + 
    " = " + resultColumn + " " + operation + " " + amountIn)
    print("incrementSql: [" + incrementSql + "]")
    sqlExecute(True, incrementSql, dbCursor, db)

def getRandomRow(dbCursor, table: str,  resultColumn: str, queryColumn: str = None, queryField: any = None):
    print("starting Mektanix getRandomRow")
    if queryColumn is None or queryField is None:
        whereClause = "\n"
    else:
        whereClause = " WHERE " + queryColumn + " LIKE " + queryField + "\n"
    randomSql = ("SELECT " + resultColumn + " FROM " + table + "" + whereClause + "ORDER BY RAND()\nLIMIT 1") 
    print("randomSql: [" + randomSql + "]")
    dbCursor.execute(randomSql)
    result = None
    for result in dbCursor:
        print("Mektanix Devil Dog getRandomRow result: [" + str(result) + "] query on next line")
        if result is None:
            print("result was None in getRandomRow")
        return(result)



def sqlStrValidator(input):
    print("starting Mektanix sqlStrValidator with input: [" + str(input) + "]")
    if type(input) is int:
        sqlStrValidatorOut = str(input)
    elif not input.isdigit():
        sqlStrValidatorOut = "\"" + input + "\""
    else:
        sqlStrValidatorOut = input
    print("exiting Mektanix sqlStrValidator with: [" + sqlStrValidatorOut + "]")
    return(sqlStrValidatorOut)

def sqlExecute(commit: bool, sqlStr: str, dbCursor, db = None):
    dbCursor.execute(sqlStr)
    if commit:
        db.commit()
    print(f'dbCursor.fetchall: {dbCursor.fetchall()}')
    print(f'dbCursor.fetcwarnings: {dbCursor.fetchwarnings()}')
    return(dbCursor)




#INSERT INTO `renarddb`.`timers` (`userid`, `expiry`, `note`) VALUES (\"testu\", \"teste\", \"testn\");


