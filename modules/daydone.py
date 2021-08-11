import mysql.connector
# from modules.sqlheader import host as h, user as u, passwd as p

# mydb = mysql.connector.connect(
# host=h,
# user=u,
# passwd=p,
# )



mydb = mysql.connector.connect(
host='18.216.39.250',
user='dbuser',
passwd='e4miqtng')    

mycursor = mydb.cursor()

def daydoneset(dayint):
    print("daydoneset called from daydone")
    sql = "UPDATE renarddb.daypersistent SET done = CASE WHEN day = " + str(dayint) + " THEN 1 ELSE 0 END"
    dbexecute(sql)

def daydonecheck(dayint):
    print("daydonecheck called from donedaydonedaydoneday")
    sql = ("SELECT day FROM renarddb.daypersistent WHERE done = 1")
    dbexecute(sql)
    for x in mycursor:
        print("dayint that is done read result: [" + str(x) + "]")
        day = x
    if dayint == int(day):
        return True
    else:
        return False

def dbexecute(sql):
    mycursor.execute(sql)
    mydb.commit()




