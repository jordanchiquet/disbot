import csv
import os
import os.path
import mysql.connector

class renardusers:
    
    def __init__(self, userid, field, param : str = None, username: str = None, serverid: int = None):
        print("users initiated")
        self.userid = userid
        self.field = field
        self.param = param
        self.username = username
        if serverid is None:
            print("serverid was None, moving on")
        elif serverid == 688494181727207478:
            print("renard users called from endowed server")
            self.servername = "endowed"
        elif serverid == 237397384676507651:
            print("renard users called from renmemorial server")
            self.servername = "renmemorial"
        else:
            print("something wrong with serverid in users module chief")
        self.mydb = mysql.connector.connect(
        host='18.216.39.250',
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
            mydb.commit()
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
    

    def getgraphdata(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT username, " + self.field + " FROM renarddb." + self.servername + "users"
        mycursor.execute(sql)
        graphresults = []
        for x in mycursor:
            print(x)
            graphresults.append(x)
        return(graphresults)

  
    def userwrite(self): 
        mycursor = self.mydb.cursor()
        print("self.username: [" + self.username + "]")
        sql = "INSERT INTO renarddb." + self.servername + "users(user," + self.field + ",username) VALUES (" + str(self.userid) + ",\"" + self.param + "\",\"" + self.username + "\") ON DUPLICATE KEY UPDATE " + self.field + " = \"" + self.param + "\", username = \"" + self.username + "\";"
        mycursor.execute(sql)
        self.mydb.commit()
        print("write successful")
        return("write successful")
    
    def userintwrite(self):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO renarddb." + self.servername + "users(user," + self.field + ",username) VALUES (" + str(self.userid) + ",1,\"" + self.username + "\") ON DUPLICATE KEY UPDATE " + self.field + " = " + self.field + "+1, username = \"" + self.username + "\";"
        mycursor.execute(sql)
        self.mydb.commit()

    def sqltest(self, user):
        mydb = mysql.connector.connect(
        host='18.216.39.250',
        user='dbuser',
        passwd='e4miqtng')
        mycursor = mydb.cursor()
        sql = "SELECT * FROM renarddb.quotes WHERE user LIKE \"" + user + "\""
        mycursor.execute(sql)
        for x in mycursor:
            return(x)