import mysql.connector
from pyasn1.type.univ import Boolean
from modules.sqlheader import host as h, user as u, passwd as p

mydb = mysql.connector.connect(
host=h,
user=u,
passwd=p,
)



# mydb = mysql.connector.connect(
# host='3.144.163.74',
# user='dbuser',
# passwd='e4miqtng')    

mycursor = mydb.cursor()

def daydoneset(dayint):
    print("daydoneset called from daydone")
    sql = "UPDATE renarddb.daypersistent SET done = CASE WHEN day = " + str(dayint) + " THEN 1 ELSE 0 END"
    dbexecute(sql, True)

def daydonecheck(dayint):
    print("daydonecheck called from donedaydonedaydoneday")
    sql = ("SELECT day FROM renarddb.daypersistent WHERE done = 1")
    dbexecute(sql)
    for x in mycursor:
        print("dayint that is done read result: [" + str(x) + "]")
        daytuple = x
    print("dayresult: [" + str(daytuple[0]) + "]")
    if dayint == daytuple[0]:
        print("returning True for daydonecheck")
        return True
    else:
        print("returning false for daydonecheck")
        return False

def dbexecute(sql, commit: Boolean = False):
    mycursor.execute(sql)
    if commit:
        mydb.commit()




