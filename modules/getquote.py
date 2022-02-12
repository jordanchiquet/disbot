import mysql.connector
import random


def getquote(user: str = None, id: str = None):
    mydb = mysql.connector.connect(
    host='3.144.163.74',
    user='dbuser',
    passwd='e4miqtng')
    mycursor = mydb.cursor(buffered=True)
    if user is not None:
        sql = "SELECT * FROM renarddb.quotes WHERE user LIKE \"%" + user + "%\""
        mycursor.execute(sql)
        qlist = []
        # qtxt = "idk i can find it hold on wait hold on where the quote it was just here"
        for x in mycursor:
            print("qtxt: " + str(x))
            qlist.append(x)
        qunparse = random.choice(qlist)
        print("flag " + str(qunparse))
        qid = qunparse[0]
        name = qunparse[1]
        qtxt = qunparse[2]
        date = qunparse[3]
        return(str(qid) + "|" + name + "|" + qtxt + "|" + date)

