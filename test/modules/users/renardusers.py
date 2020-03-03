import csv
import os
import os.path
import mysql.connector

class renardusers:
    
    def __init__(self, userid, field, param : str = None):
        self.userid = userid
        self.field = field
        self.param = param
    
    def userinit(self):
        mydb = mysql.connector.connect(
        host='18.216.39.250',
        user='dbuser',
        passwd='e4miqtng')
        mycursor = mydb.cursor()    
        sql = "SELECT * FROM renarddb.users WHERE userid LIKE \"" + self.userid + "\""
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
            mydb = mysql.connector.connect(
            host='18.216.39.250',
            user='dbuser',
            passwd='e4miqtng')
            mycursor = mydb.cursor()
            sql = "INSERT INTO renarddb.users (user) VALUES (%s)"
            val = [self.userid]
            mycursor.execute(sql, val)
            mydb.commit()
            print("user " + self.userid + " registered.")
            return("user " + self.userid + " registered.")
        else:
            print("user failed userexists redundancy test... either user is already registered or something is broken.")
            return("user " + self.userid + " was not registered, either because the user is already registered or because something is broken.")

# UPDATE `renarddb`.`users` SET `name` = 'sfsf' WHERE (`id` = '1');

    def userread(self):
        if self.userexists() == True:
            mydb = mysql.connector.connect(
            host='18.216.39.250',
            user='dbuser',
            passwd='e4miqtng')
            mycursor = mydb.cursor()
            sql = "SELECT (%s) FROM renarddb.users WHERE userid LIKE (%s)"
            val = [self.field, self.userid]
            mycursor.execute(sql, val)
            for x in mycursor:
                return(x)
        else: 
            print("user failed user exists redundancy check")
            return("not registered")
    
    def userwrite(self):
        mydb = mysql.connector.connect(
        host='18.216.39.250',
        user='dbuser',
        passwd='e4miqtng')          
        mycursor = mydb.cursor()
        sql = "INSERT INTO renarddb.users(user,%s) VALUES (%s,%s) ON DUPLICATE KEY UPDATE %s = %s"
        val = [self.field, self.userid, self.param, self.field, self.param]
        mycursor.execute(sql, val) 
        mydb.commit()
        print("write successful")
        return("write successful")


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


    
testinit = renardusers(1,"fart")
quicktest = testinit.sqltest("dog")
print(quicktest)