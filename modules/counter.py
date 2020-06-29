from modules.renardusers import renardusers

class counter:

    def __init__(self, countfield, userid, count):
        self.countfield = countfield
        self.userid = userid
        self.count = count
    
    def intwrite(self):
        for i in range(self.count):
            dbinit = renardusers(self.userid, self.countfield)
            dbinit.userintwrite()
    
