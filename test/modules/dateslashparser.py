from datetime import datetime


nowmonth = str(datetime.now().month)
nowdate = str(datetime.now().day)


class dateslashparser:
    def __init__(self, dateslashparse):
        self.dateslashparse = dateslashparse
    

    def checkdatewithmonth(self, month, date):
        print("starting checkdatewithmonth")
        if (month == "04" or
            month == "06" or
            month == "09" or
            month == "11"):
            print("month was a 30 month")
            if int(date) == 31:
                print("date was 31 for a 30 day month, returning invalid")
                return("date inv 31")
        if month == "02":
            print("month was feb")
            if int(date) > 29:
                print("date was over 29 for February, returning invalid before checking leap year")
                return("date inv too many feb")
        else:
            return("valid")
    

    def checkleapyear(self, year):
        print("starting checkleapyear")
        if (int(year) % 4) != 0 and (int(year) % 400) != 0:
            print("user used 29 for February non-leap year, returning false")
            return False
        else:
            return True
    

    def getyearwithslashes(self, month, date):
        print("starting getyearwithslashes")
        workingdate = self.dateslashparse
        if len(workingdate.split("/")) > 2:
            print("user provided some value where the year goes...")
            possibleyear = workingdate.split("/")[2]
            print("initial received year: " + possibleyear)
            if len(possibleyear) == 1 or len(possibleyear) == 3 or len(possibleyear) >= 5 or not possibleyear.isdigit():
                print("year was 1 digit, or was 3 digits, or was 5 or more digits, or was not actually numbers, returning invalid")
                return("year inv")
            if len(possibleyear) == 2:
                print("year was two digits, attempting to append two more")
                year = "20" + possibleyear
                print("fixed year: " + year)
            if len(possibleyear) == 4:
                print("year was 4 digits, leaving it be at user's risk...")
                year = possibleyear        
        # Determining year if user did not provide one 
        if len(workingdate.split("/")) < 3:
            print("user did not provide a year")
            print("removing 0 from beginning of month for math comparison... (if applicable)")
            if month == "10":
                print("month was October, keeping the zero and doing nothing")
            if month != "10":
                print("month was not October, replacing any zeros that might exist")
                mathmonth = month.replace("0", "")
                print("mathmonth: " + mathmonth)
            if int(mathmonth) < int(nowmonth):
                print("month in timer was less than current month, timer defaulting to next year")
                year = (datetime.now().year + 1)
                print("year: " + str(year))
            if int(mathmonth) > int(nowmonth):
                print("month in timer was greater than current month, timer defaulting to this year")
                year = datetime.now().year
                print("year: " + str(year))
            if mathmonth == nowmonth:
                print("month in timer is THIS month :O ... we have to check the date... checking for zeroes first... starting date value: " + date)
                if date == "10" or date == "20" or date == "30":
                    print("date was 10 or 20 or 30... removing no zeroes, date unchanged")
                if date != "10" and date != "20" and date != "30":
                    print("date was not 10 or 20 or 30, removing any zeroes")
                    date = date.replace("0", "")
                if int(nowdate) >= int(date):
                    print("user provided date was before or equal to today, default year to next year")
                    year = (datetime.now().year + 1)
                if int(nowdate) < int(date):
                    print("user provided date was after today, default year to this year")
                    year = str(datetime.now().year)
                print("year: " + year)
        return(year)


    def getmonthwithslashes(self):
        print("starting getmonthwithslashes")
        workingdate = self.dateslashparse
        month = workingdate.split("/")[0]
        print("initial received month: " + month)
        if not month.isdigit() or len(month) > 2:
            print("user used slashes but not a month number, or the month number was more than two digits, returning invalid")
            return("month inv")
        if month.isdigit(): 
            print("Month is digit")
            if not month.startswith("0"):
                if int(month) > 12:
                    print("Month was greater than 12, sending error message to channel")
                    return("month inv")
                if len(month) == 1:
                    print("Month is one digit: " + month)
                    month = "0" + month
                    print("Appending 0 to month: " + month)
                else:
                    print("month was found valid... remaining unchanged: " + month)
        print("nowmonth found to be: " + nowmonth)
        return(month)

    def getdatewithslashes(self):
        print("starting getdatewithslashes")
        workingdate = self.dateslashparse
        print("this is our working date: [" + workingdate + "]")
        date = workingdate.split("/")[1]
        print("initial received date: " + date)
        if not date.isdigit() or len(date) > 2 or date == "00" or date == "0":
            print("date was too many digits or wasn't numbers or was zero... returning invalid")
            return("date inv")
        if date.isdigit():
            print("date was numbers :)")
            if not date.startswith("0"):
                print("date did not start with zero")
                if int(date) > 31: 
                    print("date was over 31, returning invalid")
                    return("date inv")
                if len(date) == 1:
                    print("date was one digit, adding 0 to the beginning")
                    date = "0" + date
                    print("new date with 0: " + date)
                print("now reached the furthest point we can on ensuring date is valid without checking the month.")
                print("end of get date with slashes output: " + date)
        month = self.getmonthwithslashes()
        if month == "month inv":
            return("month inv")
        else:
            checkdate = self.checkdatewithmonth(month, date)
            if checkdate == "date inv 31":
                return("date inv 31")
            if checkdate == "date inv too many feb":
                return("date inv too many feb")
            else:
                print("getmonthwithslashes and checkdatewithmonth passed... starting getyearwithslashes")
                year = self.getyearwithslashes(month, date)
                if year == "year inv":
                    return("year inv")
                else:
                    print("year was valid")
                    if month == "02" and date == "29":
                        print("user provided feb 29, checking for leapyear")
                        leapyear = self.checkleapyear(year)
                        if leapyear == False:
                            return("inv leap")
        return(str(year) + "-" + month + "-" + date)

                    
            
# dateparseinit = dateslashparser("2/29")
# usabledateparse = dateparseinit.getdatewithslashes()
# print(usabledateparse)






