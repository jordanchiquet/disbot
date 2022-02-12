import csv
import os
import os.path
import mysql.connector

class renardusers:
    
    def __init__(self, userid, field, param : str = None, username: str = None, serverid = None, piperemoveint: int = 0):
        print("users initiated")
        self.userid = str(userid)
        self.field = field
        self.param = param
        self.username = username
        self.piperemoveint = piperemoveint
        if serverid is None:
            print("serverid was None, moving on")
        elif serverid == 688494181727207478:
            print("renard users called from endowed server")
            self.servername = "endowed"
        elif serverid == 237397384676507651:
            print("renard users called from renmemorial server")
            self.servername = "renmemorial"
        elif serverid == 838594342812647426:
            print("renard users called from mindfreax")
            self.servername = "mindfreax"
        elif serverid == "uni":
            print("renard users called for universal table")
            self.servername = "universal"
        else:
            print("something wrong with serverid in users module chief")
        self.mydb = mysql.connector.connect(
        host='3.144.163.74',
        user='dbuser',
        passwd='e4miqtng')     
    
    def userinit(self):
        mycursor = self.mydb.cursor()    
        sql = "SELECT * FROM renarddb." + self.servername + "users WHERE userid LIKE \"" + self.userid + "\""
        mycursor.execute(sql)
        for x in mycursor:
            return(x)
    
    def userexists(self):
        if self.userinit() == "None":
            return False
        else:
            return True

    def userreg(self):
        if self.userexists() == False:
            print("user passed userexists redundancy test... registering user")
            mycursor = self.mydb.cursor()
            sql = "INSERT INTO renarddb." + self.servername + "users (user) VALUES (%s)"
            val = [self.userid]
            mycursor.execute(sql, val)
            self.mydb.commit()
            print("user " + self.userid + " registered.")
            return("user " + self.userid + " registered.")
        else:
            print("user failed userexists redundancy test... either user is already registered or something is broken.")
            return("user " + self.userid + " was not registered, either because the user is already registered or because something is broken.")


    def userread(self):
        print("userread function was reached with parameters: USER: [" + str(self.userid) + "] FIELD: [" + self.field + "]")
        mycursor = self.mydb.cursor()
        sql = "SELECT (" + self.field + ") FROM renarddb." + self.servername + "users WHERE user LIKE (%s)"
        val = [self.userid]
        mycursor.execute(sql, val)
        for x in mycursor:
            print("read result: [" + str(x) + "]")
            return(x)
    
    def getwordcount(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT username, wordcount FROM renarddb." + self.servername + "users WHERE " + self.field + " > 0"
        mycursor.execute(sql)
        wordcountresults = []
        for x in mycursor:
            print(x)
            wordcountresults.append(x)
        return(wordcountresults)

    def getgraphdata(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT username, " + self.field + " FROM renarddb." + self.servername + "users WHERE " + self.field + " > 0"
        mycursor.execute(sql)
        graphresults = []
        for x in mycursor:
            print(x)
            graphresults.append(x)
        return(graphresults)

  
    def userwrite(self): 
        print("starting userwrite for server " + self.servername + " for field " + self.field + " with value " + self.param + " where user like " + str(self.userid))
        mycursor = self.mydb.cursor()
        print("self.username: [" + self.username + "]")
        sql = "INSERT INTO renarddb." + self.servername + "users(user," + self.field + ",username) VALUES (" + str(self.userid) + ",\"" + self.param + "\",\"" + self.username + "\") ON DUPLICATE KEY UPDATE " + self.field + " = \"" + self.param + "\", username = \"" + self.username + "\";"
        print("WRITESQL: [" + sql + "]")
        mycursor.execute(sql)
        self.mydb.commit()
        print("write successful")
        return("write successful")

    
    def userappend(self):
        print("starting userappend for server " + self.servername + " for field " + self.field + " with value " + self.param + " where user like " + str(self.userid))
        mycursor = self.mydb.cursor()
        sql = "UPDATE renarddb." + self.servername + "users " "SET " + self.field + "=CONCAT(ifnull(" + self.field + ", \"\"), \'" + self.param + "|\') WHERE user LIKE \'" + str(self.userid) + "\';"
        # UPDATE renarddb.universalusers SET todo=CONCAT(ifnull(todo, ''), 'my first task|') WHERE user LIKE '191688156427321344';
        print("WRITESQL: [" + sql + "]")
        mycursor.execute(sql)
        self.mydb.commit()
        print("write successful")
        return("write successful")
    
    def userpiperemove(self):
        print("starting userpiperemove for server " + self.servername + " for field " + self.field + " where user like " + str(self.userid))
        getpipes = self.userread()
        pipelist = getpipes[0].split("|")
        print("pipelist: " + str(pipelist))
        del(pipelist[self.piperemoveint])
        newpipestr = "|".join(pipelist)
        sql = "INSERT INTO renarddb." + self.servername + "users(user," + self.field + ",username) VALUES (" + str(self.userid) + ",\"" + newpipestr + "\",\"" + self.username + "\") ON DUPLICATE KEY UPDATE " + self.field + " = \"" + newpipestr + "\", username = \"" + self.username + "\";"
        print("WRITESQL: [" + sql + "]")
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        self.mydb.commit()


    
    def userintwrite(self):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO renarddb." + self.servername + "users(user," + self.field + ",username) VALUES (" + str(self.userid) + ",1,\"" + self.username + "\") ON DUPLICATE KEY UPDATE " + self.field + " = " + self.field + "+1, username = \"" + self.username + "\";"
        mycursor.execute(sql)
        self.mydb.commit()

    def sqltest(self, user):
        mydb = mysql.connector.connect(
        host='3.144.163.74',
        user='dbuser',
        passwd='e4miqtng')
        mycursor = mydb.cursor()
        sql = "SELECT * FROM renarddb.quotes WHERE user LIKE \"" + user + "\""
        mycursor.execute(sql)
        for x in mycursor:
            return(x)