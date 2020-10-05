from modules.renardusers import renardusers

class renardtodo: 

    def __init__(self, userid, username, todotext: str = "placeholder", getlist: bool = False, markcomplete: bool = False, taskint: int = 0):
        self.userid = userid
        self.username = username
        self.todotext = todotext
        self.getlist = getlist
        self.markcomplete = markcomplete
        self.taskint = taskint
        self.todoinit = renardusers(userid, "todo", param=todotext, username=username, serverid="uni", piperemoveint=taskint)
    

    def todomain(self):
        if self.getlist:
            return(self.gettodolist())
        elif self.markcomplete:
            return(self.todomarkcomplete())
        else:
            return(self.todoaddendum())


    def gettodolist(self):
        todoappendint = self.todoinit
        try:
            liststr = todoappendint.userread()
            print("liststr: " + str(liststr))
            if liststr[0] is None or liststr[0] == '':
                print("got [0] none case")
                stroutput = "hmm... are you sure you have a list? just use \".todo new task text here\" to start on one"
            else:
                listlist = liststr[0].split("|")
                listoutput = []
                for count,taskstr in enumerate(listlist,1):
                    listoutput.append(str(count) + ". " + taskstr)
                del(listoutput[-1])
                stroutput = ("```" + "\n".join(listoutput) + "```")
        except:
            stroutput = "hmm... are you sure you have a list? just use \".todo new task text here\" to start on one"
        return(stroutput)


    def todoaddendum(self):
        todoappendinit = self.todoinit
        try:
            todoappendinit.userappend()
            print("made here append")
            newtodo = self.gettodolist()
            appendresult = ("New task appended! Your new list: " + newtodo)
        except:
            appendresult = "omg error ask jordna to fix wtf"
        return(appendresult)


    def todomarkcomplete(self):
        print("we did call markcomplete")
        todoappendint = self.todoinit
        try:
            todoappendint.userpiperemove()
            newtodo = self.gettodolist()
            if newtodo.startswith("hmm"):
                markcompleteresult = ("Task complete! Woaw you have nothing left to do :)")
            else:
                markcompleteresult = ("Task complete! Your new list: " + newtodo)
        except:
            markcompleteresult = ("some kinda problemon occur, maybe you no have so many tasks... hmmm... lemonade")
        return(markcompleteresult)