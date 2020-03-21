import random

class dice:
    def __init__(self, a, b: str = None):
        if b is None:
            self.rolltext = a
            self.adv = None
        else:
            if a[0].isdigit():
                self.rolltext = a
                self.adv = b
            else:
                self.rolltext = b
                self.adv = a


    def advcheck(self):
        advstate = self.adv
        if advstate is None:
            return("noadv")
        else:
            if advstate.startswith("adv"):
                return("adv")
            if advstate.startswith("dis"):
                return("dis")
            else:
                return("inv")
    

    def roll(self):
        rolltext = self.rolltext
        mult = rolltext.split("d")[0]
        if mult.isdigit():
            print("number of dice passed digit check")
            mult = int(mult)
        else:
            print("number of dice did not pass digit check")
            return("That's not how I roll brother...")
        if "+" in rolltext:
            numsplit1 = rolltext.split("d")[1]
            d = numsplit1.split("+")[0]
            modifier = numsplit1.split("+")[1]
        else:
            d = rolltext.split("d")[1]
            modifier = 0
        min = 1
        max = int(d)
        reslist = []
        for x in range(mult):
            res = random.randint(min, max)
            reslist.append(res)
            pass
        rollsum = sum(reslist)
        addsum = rollsum + int(modifier)
        if modifier == 0:
            return(str(addsum) + " " + str(reslist))
        else:
            return(str(addsum) + " " + str(reslist) + " + " + modifier)


    def roller(self):
        advresult = self.advcheck()
        if advresult == "noadv":
            return(self.roll())
        val1 = self.roll().split(" ")[0]
        val2 = self.roll().split(" ")[0]
        if advresult == "adv":
            if int(val1) > int(val2):
                return(val1 + " - rolled with advantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
            else:
                return(val2 + " - rolled with advantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
        if advresult == "dis":
            if int(val1) < int(val2):
                return(val1 + " - rolled with disadvantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
            else:
                return(val2 + " - rolled with disadvantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
        else:
            return("That's now how I roll brother...")




rollinit = dice("1d6+1", "dis")
print(rollinit.roller())