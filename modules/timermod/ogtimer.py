class ogtimer:
    def __init__(self, durationortime):
        self.durationortime = durationortime
    
    def ogparse(self):
        print("starting ogparse")
        durationortime = self.durationortime
        dortnocolon = durationortime.replace(":", "")
        if ":" in durationortime and dortnocolon.isdigit():
            time = durationortime
            print("colon in durationortime and isdigit")
            if len(time) > 5 or len(time) < 4:
                print("time is > 5 char or less than 4, returning invalid")
                return('inv')
            else:
                print("time looks valid, pass to timeparse for validation")
                return('wastime|' + time)
        elif ":" in durationortime and not dortnocolon.isdigit():
            print("user input was invalid (colon for durationortime but not digit without): [" + durationortime +"]")
            return('inv')
        elif durationortime.isdigit():
            duration = durationortime
            print("value for ogparse looks like duration")
            return('wasduration|' + duration)
        else:
            print("input didn't match any ogparse param, invalid or shit is broken: [" + durationortime + "]")
            return('inv')


ogtimerinit = ogtimer('7:00')
dortcheck = ogtimerinit.ogparse()
print(dortcheck)

