import random

class dice:
    def __init__(self, a, b: str = None):
        if b is None:
            self.rolltext = a
            self.adv = None
        else:
            self.rolltext = b
            self.adv = a


async def roll(self):
    rolltext = self.rolltext
    mult = int(rolltext[0])
    if "+" in rolltext:
        numsplit1 = rolltext.split("+")[0]
        numsplit2 = rolltext.split("+")[1]
        d = int(numsplit1[2:])
        print(numsplit2)
        print(d)
    if "+" not in rolltext:
        d = int(rolltext[2:])
        numsplit2 = 0
    min = 1
    max = d
    reslist = []
    for x in range(mult):
        res = random.randint(min, max)
        reslist.append(res)
        pass
    rollsum = sum(reslist)
    addsum = rollsum + int(numsplit2)
    reslist.clear()     
    if numsplit2 == 0:
        return(str(addsum) + " " + str(reslist))
    else:
        return(str(addsum) + " " + str(reslist) + " + " + numsplit2)


async def adv(self):
    if self.adv is None:
        return("error, advantage state was none")
    else:
        advstate = self.adv
    if advstate.startswith("adv"):
        rolla = self.roll()
        rollb = self.roll()
        print("a: [" + rolla + "]")
        print("b: [" + rollb + "]")


rollinit = dice("1d6", "adv")
rollinit.adv()