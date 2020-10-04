from modules.renardusers import renardusers

class renardtodo: 

    def __init__(self, userid, username, todotext, getlist: bool = False, markcomplete: bool = False):
        self.userid = userid
        self.username = username
        self.todotext = todotext
        self.markcomplete = markcomplete
        self.todoinit = renardusers(userid, "todo", )
    
    def todoaddendum(self):
        if self.markcomplete:
            print("addendum double check failed due to markcomplete being true")
            return("uh oh, Jordan's retarded! Tell him self.markcomplete was True when it should have been false!")
        else:
            todoappendinit = renardusers(self.userid, "todo", param = todotext, username = self.username, serverid = "uni")
            return ("New task appended! Use \".todo\" with no extra parameters to get your list!")
        
    def gettodolist(self):
        print("placeholder")
            