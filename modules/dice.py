import random
from random import randrange

class dice:
    def __init__(self, a: str = None, b: str = None):
        if b is None:
            self.rolltext = a.lower()
            self.adv = None
        else:
            if a[0].isdigit():
                self.rolltext = (a.replace(",", "")).lower()
                self.adv = b
            else:
                self.rolltext = (b.replace(",","")).lower()
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
        addsub = True
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
            strmodifier = "+"
        elif "-" in rolltext:
            numsplit1 = rolltext.split("d")[1]
            d = numsplit1.split("-")[0]
            modifier = numsplit1.split("-")[1]
            strmodifier = "-"
            addsub = False
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
        if addsub:
            addsum = rollsum + int(modifier)
        else: 
            addsum = rollsum - int(modifier)
        if modifier == 0:
            if len(reslist) == 1:
                dice_out = (str(addsum))
            else:
                dice_out = (str(addsum) + " " + str(reslist) + "|" + d)
            return(dice_out)
        else:
            modaddendum =(" " + strmodifier + " *" + modifier + "*")
            resliststr = str(reslist).replace("]", "")
            returnstr = ("**" + str(addsum) + "**  " + resliststr + modaddendum + "]")
            return(returnstr + "|" + d)


    def roller(self):
        advresult = self.advcheck()
        if advresult == "noadv":
            diceout = self.roll().split("|")
            return(self.roll().split("|")[0])
        val1 = (self.roll().split(" ")[0])
        val2 = (self.roll().split(" ")[0])
        if advresult == "adv":
            d = self.roll().split("|")[1]
            if val1 == d:
                return(val1 + " - rolled with advantage. (First roll: " + val1 + "! Did not initiate second roll.)")
            if int(val1) > int(val2):
                return(val1 + " - rolled with advantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
            else:
                return(val2 + " - rolled with advantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
        if advresult == "dis":
            if val1 == "1":
                return("1 - rolled with disadvantage. (First roll: 1! Did not initiate second roll.)")
            if int(val1) < int(val2):
                return(val1 + " - rolled with disadvantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
            else:
                return(val2 + " - rolled with disadvantage. (First roll: " + val1 + ", Second Roll: " + val2 + ")")
        else:
            return("That's now how I roll brother...")

    def abilityroller(self):
        print("made it abilityrorller")
        self.rolltext = "24d6" 
        resultsplit1 = list(((self.roll()).split("[")[1]).split("]")[0])
        resultsplit1pruned = [int(y) for y in[item.replace("1", str(random.randrange(2,6))) for item in [x for x in resultsplit1 if x.isdigit()]]]
        print("successfully got list")
        print(resultsplit1)
        print(resultsplit1pruned)
        print([resultsplit1pruned[0:4]])
        abil1 = resultsplit1pruned[0:4]
        abil2 = resultsplit1pruned[4:8]
        abil3 = resultsplit1pruned[8:12]
        abil4 = resultsplit1pruned[12:16]
        abil5 = resultsplit1pruned[16:20]
        abil6 = resultsplit1pruned[20:24]
        abil1.remove(min(abil1)); abil2.remove(min(abil2)); abil3.remove(min(abil3)); abil4.remove(min(abil4)); abil5.remove(min(abil5)); abil6.remove(min(abil6))
        abil1final = str(sum(abil1)) + ", "
        abil2final = str(sum(abil2)) + ", "
        abil3final = str(sum(abil3)) + ", "
        abil4final = str(sum(abil4)) + ", "
        abil5final = str(sum(abil5)) + ", "
        abil6final = str(sum(abil6))
        return(abil1final + abil2final + abil3final + abil4final + abil5final + abil6final)
        