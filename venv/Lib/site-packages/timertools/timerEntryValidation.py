from datetime import date, datetime, timedelta
import time

from modules.randomhelpers import getFirstAlphaIndex, removefirstindex, getSpaceList, getCSTOffsetTime


datetimeExample = "2022-07-03 14:09:25.584001"

currentYear = (date.today() - timedelta(hours=5)).year
currentMonth = (date.today() - timedelta(hours=5)).month
currentDate = (date.today()  - timedelta(hours=5)).day

class timeEntryValidation:


    def __init__(self, timeEntryInput: str):
        print("timeEntryValidation initiation started")
        self.errorOutput = "error; with input: [" + timeEntryInput + "]; "
        print("errorOutput start: [" + self.errorOutput + "]")
        self.passOutput = "pass; with input: [" + timeEntryInput + "]; "
        self.secondsAppend = ":00.000000"
        self.timeEntryInput = timeEntryInput
        self.currentYear = (date.today() - timedelta(hours=5)).year
        self.currentMonth = (date.today() - timedelta(hours=5)).month
        self.currentDate = (date.today()  - timedelta(hours=5)).day
        self.currentDateFull = (datetime.now() - timedelta(hours=5)).date()
        print("self.currentDateFull: [" + str(self.currentDateFull) + "]")
        self.nowTime = (datetime.now() - timedelta(hours=5)).time()
        print("self.nowTime: [" + str(self.nowTime) + "]")
        print("timeEntryValidation initiation complete")


    def inputParserMain(self):
        entryList = (self.timeEntryInput).split(" ")
        if len(entryList) < 2:
            formatReturn = "fail", "no input after .timer", ""
        else:
            self.entryList = removefirstindex(entryList)
            if entryList[0].isdigit():
                print("starting durationFormatHandler")
                formatReturn = self.durationFormatHandler(entryList)
            elif "/" in entryList[0] or "-" in entryList[0]:
                print("/ or - in entryList[0]; inputParserMain")
                formatReturn = self.slashDateStartHandler(entryList)
            elif ":" in entryList[0]:
                print(": in entryList[0]; inputParserMain")
                formatReturn = self.colonStartHandler(entryList)
            elif (entryList[0])[:3] in str(self.monthList):
                print("[:3] of entryList[0] in monthList; inputParserMain")
                formatReturn = self.dateEngFormatStartHandler(entryList)
            else: 
                print("no useable timer parameters...; inputParserMain")
                formatReturn = "fail", "no usable input", ""
        if formatReturn[0] == "fail": 
            mainParserOutput = "fail", formatReturn[1]
        else:
            mainParserOutput = self.zeroPrepender(formatReturn[1] + self.secondsAppend), formatReturn[2]
        #TODO: if noHour:noMinute at the end, run default check
        print("timerEntryValidation inputParserMain output: [" + 
        str(mainParserOutput) + "]")
        return(mainParserOutput)
    

    def zeroPrepender(self, input):
        print("starting zeroPrepender with input: [" + input + "]")
        fullExpirySpaceList = getSpaceList(input)
        dateList = (fullExpirySpaceList[0]).split("-")
        for index, item in enumerate(dateList):
            if len(item) == 1:
                item = "0" + item
                dateList[index] = item
        outHourMin = fullExpirySpaceList[1]
        if len(outHourMin) == 14:
            outHourMin = "0" + outHourMin
        zeroPrependerOutput = "-".join(dateList) + " " + outHourMin
        print("ending zeroPrepender with output: [" + str(zeroPrependerOutput) + "]")
        return(zeroPrependerOutput)


    def dateEngFormatStartHandler(self, inputList : list):
        print("dateEngFormatStartHandler started")
        dateHandled = self.dateEnglishFormatValidator(inputList)
        print("dateHandled: [" + str(dateHandled) + "]; dateEngFormatStartHandler")
        expiryDate = (dateHandled[0]).replace("noDate", "01")
        print("expiryDate: [" + expiryDate + "]; dateEngFormatStartHandler")
        inputRemainderList = inputList[dateHandled[1]:]
        print("inputRemainderList: [" + str(inputRemainderList) + "]; date"
        "EngFormatStartHandler")
        noteSlice = 0
        expiryHourMin = "noHour:noMinute"
        if len(inputRemainderList) > 0:
            if ":" in inputRemainderList[0]:
                positionTwoTimeOutput = self.colonAndMeridiemHandler(inputRemainderList)
                if positionTwoTimeOutput[0] != "noHour":
                    expiryHourMin = positionTwoTimeOutput[0] + ":" + positionTwoTimeOutput[1]
                    print("noteslice: [" + str(positionTwoTimeOutput[2]) + "]")
                    noteSlice = positionTwoTimeOutput[2]
        expiryTime = expiryDate + " " + expiryHourMin
        timerNote = self.getTimerNote("slice", inputRemainderList, noteSlice)
        print("expiryTime: [" + expiryTime + "], with timerNote: [" + timerNote +
        "]; dateEngFormatStartHandler")
        return("pass", expiryTime, timerNote)


    def colonStartHandler(self, inputList : list):
        timeOutput = self.colonAndMeridiemHandler(inputList)
        if timeOutput[0] == "noHour":
            colonStartOutput = "fail", "error invalid hour; colonStartHandler", ""
        else:
            print("reached outer else in colonStartHandler")
            expiryDateFull = "noDate"
            timeStr = timeOutput[0] + ":" + timeOutput[1]
            noteSliceAddend = 0
            print("noteSliceAddend: [" + str(noteSliceAddend) + "]; colonStartHandler")
            timerNote = ""
            if len(inputList) > 1: 
                print("inputList longer than 1 in colonStartHandler; proceeding to grab date")
                inputRemainderList = inputList[timeOutput[2]:]
                print("proceeding with inputRemainderList: [" + str(inputRemainderList) + "]; colonStartHandler")
                if len(inputRemainderList) > 0:
                    positionTwo = inputRemainderList[0]
                    if "-" in positionTwo or "/" in positionTwo:
                        print("- or / in positionTwo: [" + positionTwo + "]; colonStartHandler")
                        slashDateCheck = self.dateSlashValidator(positionTwo)
                        if "error" not in slashDateCheck:
                            expiryDateFull = slashDateCheck
                            noteSliceAddend = 1
                    elif (positionTwo[:3]).lower() in str(self.monthList):
                        print("month text found for positionTwo: [" + positionTwo + "]; colonStartHandler")
                        positionTwoMonthChecked = self.dateEnglishFormatValidator(inputRemainderList)
                        if "noDate" not in positionTwoMonthChecked[0]:
                            print("did get date from dateEnglishFormatValidator; colonStartHandler")
                            expiryDateFull = positionTwoMonthChecked[0]
                            noteSliceAddend = positionTwoMonthChecked[1]
                timerNote = self.getTimerNote("slice", inputRemainderList, noteSliceAddend)
            if expiryDateFull == "noDate":
                print("expiryDateFull noDate at end of colonStartHandler")
                expiryDateFull = self.getDateFromTime(timeStr)
            expiryTime = expiryDateFull + " " + timeStr
            print("ending colonStartHandler with expiryTime: [" + expiryTime + "]"
            " and timerNote: [" + timerNote + "]")
            colonStartOutput = ("pass", expiryTime, timerNote)
        print("colonStartOutput returning: [" + str(colonStartOutput) + "]")
        return(colonStartOutput)


    def getTimerNote(self, sliceOrSplit: str, input, delimiterOrIndex):
        print("debug line donkey nuts")
        print ("getTimerNote called with input: [" + str(input) + "] and delimiterOrIndex: [" + str(delimiterOrIndex) + "]")
        print("debug line shit eater 9")
        if sliceOrSplit == "split":
            timerNote = str((input.split(delimiterOrIndex)[1])[1:])
        elif sliceOrSplit == "slice":
            timerNote = " ".join(input[delimiterOrIndex:])
        else:
            timerNote = "invalid parameter in getTimerNote for sliceOrSplit"
        print("getTimerNote returning: [" + timerNote + "]")
        return(timerNote)


    def dateOneination(input: str, changeDate: bool):
        print("starting dateOneination with input: [" + input + "]; changeDate: [" + str(changeDate) + "]")
        if changeDate:
            dateOneinated = input.replace("noDate", "01")
        else:
            dateOneinated = input
        return(dateOneinated)
        

    def getDateFromTime(self, input):
        print("started getDateFromTime with input: [" + input + "]")
        timerTime = (datetime.strptime(input,'%H:%M')).time()
        if timerTime < self.nowTime:
            print("timerTime found to have already expired today, getDateFromTime returning tomorrow")
            fullDateOut = self.currentDateFull + timedelta(days=1)
        else:
            print("timerTime given found to be in the future, getDateFromTime returning today")
            fullDateOut = self.currentDateFull
            print("debug line xxxtentacion")
        return(str(fullDateOut))
        

    def dateEnglishFormatValidator(self, inputList: list):
        print("dateEnglishFormat start")
        dateOut = "noDate"
        yearOut = "noYear"
        monthOut = self.monthTextValidator(inputList[0])
        noteSplitIndexAddend = 0
        if len(inputList) > 1:
            dateValidated = self.dateDigitValidator(inputList[1])
            if "error" not in dateValidated:
                dateOut = dateValidated
                noteSplitIndexAddend = 2
                if len(inputList) > 2:
                    print("about to send [2] from " + str(inputList) +" to yearValidated "
                    "in dateEnglishFormatValidator")
                    yearValidated = self.yearDigitValidator(inputList[2])
                    if "error" not in yearValidated:
                        print("yearOut in dateEnglishFormatValidator: [" + yearValidated + "]")
                        yearOut = yearValidated
                        noteSplitIndexAddend = 3
            else:
                yearValidated = self.yearDigitValidator(inputList[1])
                if "error" not in yearValidated:
                    print("yearOut in dateEnglishFormatValidator: [" + yearValidated + "]")
                    yearOut = yearValidated
                    noteSplitIndexAddend = 2
        if dateOut == "noDate":
            dateForYearGet = "01"
        else: 
            dateForYearGet = dateOut
        if (monthOut.isdigit()) and yearOut == "noYear":
            yearOut = self.getYearFromDate([monthOut, dateForYearGet])
        dateEnglishOutput = yearOut + "-" + monthOut + "-" + dateOut
        print("dateEnglishOutput: [" + dateEnglishOutput + "]")
        return(dateEnglishOutput, noteSplitIndexAddend)


    def colonAndMeridiemHandler(self, inputList: list):
        print("starting colonAndMeridiemHandler with inputList: [" + str(inputList) + "]")
        expiryHour, expiryMinute = "noHour", "noMinute"
        meridiemSpaceOut = self.meridiemSpaceHandler(inputList)
        colonCheck = self.colonParser(meridiemSpaceOut[0])
        if colonCheck[0] == True:
            expiryHour = self.meridiemAddition(int(colonCheck[1]), meridiemSpaceOut[1])
            expiryMinute = colonCheck[2]
        noteAddendum = meridiemSpaceOut[2]
        colonAndMeridiemHandlerOut = (expiryHour, expiryMinute, noteAddendum)
        print("colonAndMeridiemHandler returning: [" + str(colonAndMeridiemHandlerOut) + "]")
        return(colonAndMeridiemHandlerOut)


    def slashDateStartHandler(self, inputList : list):
        slashCheck = self.dateSlashValidator(inputList[0])
        print("exited dateSlashValidator in slashDateStartHandler with result: [" + slashCheck + "]")
        if "error" in slashCheck:
            slashDateStartOutput = "fail", slashCheck, ""
        else:
            print("arrived at outer else in slashDateStartHandler")
            expiryHourMin = "noHour:noMinute"
            noteSlice = 1
            if len(inputList) > 1:
                positionTwo = inputList[1]

                if ":" in positionTwo:
                    posTwoColonHandled = self.colonAndMeridiemHandler(inputList[1:])
                    if posTwoColonHandled[0] != "noHour":
                        expiryHourMin = posTwoColonHandled[0] + ":" + posTwoColonHandled[1]
                        noteSlice = 1 + posTwoColonHandled[2]
            expiryTime = slashCheck + " " + expiryHourMin
            timerNote = self.getTimerNote("slice", inputList, noteSlice)
            print("expiryTime from slashDateStartHandler: [" + expiryTime + "]")
            slashDateStartOutput = ["pass", expiryTime, timerNote]
        return(slashDateStartOutput)
                    
    
    def meridiemSpaceHandler(self, inputList):
        print("starting meridiemSpaceHandler")
        meridiemResultPositionOne = self.meridiemHandler(inputList[0])
        print("escaped meridiemHandler for position one in meridiemSpaceHandler with result: [" + str(meridiemResultPositionOne) + "]")
        keepInputForOut = False
        if meridiemResultPositionOne[0] == True:
            print("found meridiemResultPositionOne[0] as True")
            colonOutput = meridiemResultPositionOne[1]
            meridiemStr = meridiemResultPositionOne[2]
            noteSplitIndexAddend = 1
        elif meridiemResultPositionOne[0] == False and len(inputList) > 1:
            print("meridiemResultPositionOne[0] is False and length of input long enough to look for a meridiem after")
            meridiemResultPositionTwo = self.meridiemHandler(inputList[1])
            print("escaped meridiemHandler for position two in meridiemSpaceHandler with result: [" + str(meridiemResultPositionTwo) + "]")
            if meridiemResultPositionTwo[0] == True:
                colonOutput = inputList[0]
                meridiemStr = meridiemResultPositionTwo[2]
                noteSplitIndexAddend = 2
            else:
                keepInputForOut = True
        else:
            keepInputForOut = True
        if keepInputForOut == True:
            colonOutput = inputList[0]
            meridiemStr = ""
            noteSplitIndexAddend = 1
        meridiemSpaceHandlerOut = colonOutput, meridiemStr, noteSplitIndexAddend
        print("meridiemSpaceHandler returning: [" + str(meridiemSpaceHandlerOut) + "]")
        return(meridiemSpaceHandlerOut)


    def meridiemAddition(self, hourDigit : int, meridiemStr : str):
        print("starting meridiemAddition with hourDigit: [" + str(hourDigit) +
        "] and meridiemStr: [" + meridiemStr + "]")
        hourAddend = 0
        if ((meridiemStr == "pm" and hourDigit < 12) or
        (meridiemStr == "am" and hourDigit == 12)):
            hourAddend = 12
        hourSum = hourDigit + hourAddend
        if hourSum == 24:
            hourSum = 0
        if hourSum > 23:
            return(self.errorOutput + "hour greater than 23")
        else:
            return(str(hourSum))


    def meridiemHandler(self, input):
        print("starting meridiemHandler with input: [" + input + "]")
        try:
            alphaIndex = getFirstAlphaIndex(input)
            meridiemString = ((input[alphaIndex:]).replace(".", "")).lower()
            if meridiemString == "am" or meridiemString == "pm":
                meridiemOutput = True, input[:alphaIndex], meridiemString
            else: 
                meridiemOutput = False, "meridiemHandler: alpha not am/pm", ""
        except:
            meridiemOutput = False, "meridiemHandler: no alpha found", ""
        return meridiemOutput

       
    def durationFormatHandler(self, inputList : list):
        print("starting durationFormatHandler with inputList: [" + str(inputList) + "]")
        unitCheckOne = self.unitValidator(inputList[1])
        print("escaped unitCheckOne on durationFormatHandler")
        print(unitCheckOne)
        if not str(unitCheckOne).isdigit(): #checking for returned minute * factor based on the unit
            print("failed isdigit for durationFormatHandler for: [" + str(unitCheckOne) + "]")
            return("fail", "{TimerError-durationFormatHandler} " + unitCheckOne)
        else:  
            print("verified unit was correct and got valid digit: [" + str(unitCheckOne) + "]")
            timeDeltaAddend = int(inputList[0]) * unitCheckOne
            print("timeDeltaAddend: [" + str(timeDeltaAddend) + "]")
            inputStr = " ".join(inputList)
            noteAppend = (inputStr.split(inputList[1]))[1]
            print("processed til after noteAppend 0 in durationFormatHandler")
            if len(inputList) > 3:
                print("starting unitValidator for unitCheckTwo (durationFormatHandler)")
                unitCheckTwo = self.unitValidator(inputList[3])
                if inputList[2].isdigit() and str(unitCheckTwo).isdigit():
                    timeDeltaAddend = timeDeltaAddend + (int(inputList[2]) * unitCheckTwo)
                    noteAppend = ((inputStr.split(inputList[3]))[1])[1:]
        nowTime = getCSTOffsetTime()
        print("nowTime: [" + str(nowTime) + "]; durationFormatHandler")
        expiryTime = (nowTime + timedelta(minutes=timeDeltaAddend)).strftime("%Y-%m-%d %H:%M")
        return("pass", expiryTime, noteAppend)


    def colonParser(self, input):
        print("starting colonParser with input: [" + input + "]")
        usableOutput = False
        colonParserOutputTwo = ""
        if ":" not in input:
            colonParserOutputOne = self.errorOutput + "no colon sent to colonParser | "
        else:
            colonList = input.split(":")
            if len(colonList) > 2:
                colonParserOutputOne = self.errorOutput + "too many items in colonsplit | "
            else:
                colonHours = colonList[0]
                colonMinutes = colonList[1]
                if not colonHours.isdigit() or not colonMinutes.isdigit():
                    colonParserOutputOne = self.errorOutput + "non digit in hours or minutes place | "
                elif len(colonHours + colonMinutes) > 4 or len(colonHours + colonMinutes) < 3: 
                    colonParserOutputOne = self.errorOutput + "too many digits in colon time | "
                elif int(colonHours) > 23 or int(colonMinutes) > 59:
                    colonParserOutputOne = self.errorOutput + "hours or minutes int was too high (above 23 or above 59)"
                else:
                    usableOutput = True
                if usableOutput == True:
                    colonParserOutputOne = colonHours
                    colonParserOutputTwo = colonMinutes
        colonParserOutput = usableOutput, colonParserOutputOne, colonParserOutputTwo
        print("colonParserOutput: [" + str(colonParserOutput) + "]")
        return(colonParserOutput)


    def unitValidator(self, input):
        print("starting unitValidator for duration format")
        input = input.lower()
        if input.startswith("month"):
            unitOutput = self.errorOutput + "unit invalid - months differ in length and arent accepted right now, try a day amount or 4 weeks instead | "
        elif input.startswith("m"):
            unitOutput = 1
        elif input.startswith("h"):
            unitOutput = 60
        elif input.startswith("d"):
            unitOutput = 1440
        elif input.startswith("w"):
            unitOutput = 10080
        elif input.startswith("y"):
            unitOutput = 525600
        else:
            unitOutput = self.errorOutput + "unit invalid (not minute, hour, day, week, or year) | "
        print("unitValidator output: [" + str(unitOutput) + "] for unit [" + input + "]")
        return unitOutput


    def dateSlashValidator(self, input):
        slashOutput = ""
        isError = False
        if "/" in input:
            slashSplit = input.split("/")
        elif "-" in input:
            slashSplit = input.split("-")
        else:
            slashOutput = self.errorOutput + "no dash or hyphen fed to dateSlashValidator | "
        if slashSplit is not None:
            if len(slashSplit) < 2 or len(slashSplit) > 3:
                slashOutput = self.errorOutput + "date too short or too long | "
            else:
                monthValidated = self.monthDigitValidator(slashSplit[0])
                print("made out of monthDigitValidator in dateSlashValidator with result: [" + monthValidated + "]")
                if "error" in monthValidated:
                    slashOutput = slashOutput + monthValidated
                    isError = True
                dateValidated = self.dateDigitValidator(slashSplit[1])
                print("made out of dateDigitValidator in dateSlashValidator with result: [" + dateValidated + "]")
                if "error" in dateValidated:
                    slashOutput = self.errorOutput + dateValidated
                    isError = True
                if len(slashSplit) == 3: 
                    yearValidated = self.yearDigitValidator(slashSplit[2])
                    print("made out of yearDigitValidator in dateSlashValidator with result: [" + yearValidated + "]")
                    if "error" in yearValidated:
                        slashOutput = slashOutput + yearValidated
                        isError = True
                    elif len(yearValidated) == 2:
                        yearValidated = "20" + yearValidated
                if len(slashSplit) == 2 and not isError:
                    yearValidated = self.getYearFromDate(slashSplit)
        if slashOutput == "":
            slashOutput = yearValidated + "-" + monthValidated + "-" + dateValidated
        print("slashOutput: [" + slashOutput + "]")
        return slashOutput
    

    def getYearFromDate(self, inputList):
        print("getYearFromDate started")
        date = int(inputList[1])
        month = int(inputList[0])
        nextYear = currentYear + 1 #this probably will not work
        if currentMonth > month:
            getYearOutput = nextYear
        if currentMonth < month: 
            getYearOutput = currentYear
        if currentMonth == month:
            if currentDate < date:
                getYearOutput = currentYear
            else:
                getYearOutput = nextYear
        return(str(getYearOutput))


    def basicDigitValidator(self, fedFrom, input):
        input = str(input)
        print("starting basicDigitValidator from " + fedFrom + " with input [" + input + "]")
        basicDigitValidatorOutput = input
        if not input.isdigit():
            basicDigitValidatorOutput = self.errorOutput + "non-digit input | "
        else:
            if input == "0":
                basicDigitValidatorOutput = self.errorOutput + "input was '0' | "
            else:
                if "month" in fedFrom or "date" in fedFrom:
                    if len(input) > 2:
                        basicDigitValidatorOutput = self.errorOutput + "input longer than two characters for month or date | "
                elif "year" in fedFrom:
                    if len(input) < 2 or len(input) > 4:
                        basicDigitValidatorOutput = self.errorOutput + "input invalid length for year | "
        return(basicDigitValidatorOutput)


    def monthDigitValidator(self, input):
        input = str(input)
        print("starting monthDigitValidator with input: [" + input + "]")
        basicValidatorOutput = self.basicDigitValidator("monthDigitValidator", input)
        if "error" in basicValidatorOutput:
            monthDigitOutput = basicValidatorOutput
        else:
            errorOutput = "error: monthDigitValidator; input: [" + input + "] | "
            monthDigitOutput = input
            if not input.startswith("0"):
                if int(input) > 12:
                    monthDigitOutput = errorOutput + "month greater than 12 | "
            elif len(input) == 1:
                monthDigitOutput = "0" + input
        print(monthDigitOutput)
        return(monthDigitOutput)


    def dateDigitValidator(self, input):
        print("starting dateDigitValidator with input: [" + input + "]")
        for char in "rdthn":
            input = (str(input)).replace(char, "")
        basicValidatorOutput = self.basicDigitValidator("dateDigitValidator", input)
        if "error" in basicValidatorOutput:
            dateDigitOutput = basicValidatorOutput
        else:
            errorOutput = "error: dateDigitValidator; input: [" + input + "]; "
            dateDigitOutput = input
            if not input.startswith("0"):
                if int(input) > 31:
                    dateDigitOutput = errorOutput + "date greater than 31"
            elif len(input) == 1:
                dateDigitOutput = "0" + input
        print(dateDigitOutput)
        return(dateDigitOutput)
    

    def yearDigitValidator(self, input):
        input = str(input)
        print("starting yearDigitValidator with input: [" + input + "]")
        yearDigitOutput = input
        basicValidatorOutput = self.basicDigitValidator("yearDigitValidator", input)
        print("escaped basicValidatorOutput in yearDigitValidator with result: [" + basicValidatorOutput + "]")
        if "error" in basicValidatorOutput:
            yearDigitOutput = basicValidatorOutput
        else:
            print("reached outer else in yearDigitValidator")
            if len(input) == 2:
                print("verified input year is length 2: [" + input + "]")
                currentYear = (self.currentYear)
                print("currentYear: [" + str(currentYear) + "]; yearDigitValidator")
                currentYear = str(currentYear)[2:]
                print("was able to parse currentYear in yearDigitValidator")
                if int(input) < int(currentYear):
                    print("year given already happened, sir; yearDigitValidator")
                    yearDigitOutput = self.errorOutput + "that year is passed (2 digit); "
            elif len(input) == 4:
                print("verified year is 4 digits; yearDigitValidator")
                if int(input) < self.currentYear:
                    yearDigitOutput = self.errorOutput + "that year is passed (4 digit);"
        print("reached end of yearDigitValidator with yearDigitOutput: [" + yearDigitOutput + "]")
        return(yearDigitOutput)


    def isLeapYear(self, input: int):
        if (input % 400 == 0) or ((input % 100 != 0) and (input % 4 == 0)):
            leapYear = True
        else:
            leapYear = False
        return(leapYear)
    

    def febValidator(self, formattedDate):
        year = formattedDate.split("-")[0]
        month = formattedDate.split("-")[1]
        date = formattedDate.split("-")[2]
        if month == "02":
            if int(date) > 29:
                febValidatorOutput = self.errorOutput + "date greater than 29 given for February | "
            if int(date) <= 28:
                febValidatorOutput = self.passOutput + "28 or less for February | "
            else:
                if self.isLeapYear(year):
                    febValidatorOutput = self.passOutput + "29 given for leap year | "
                else:
                    febValidatorOutput = self.errorOutput + "29 given for non-leap year | "
        else:
            febValidatorOutput = self.passOutput + "month not February | "
        return(febValidatorOutput)


    def monthTextValidator(self, input):
        input = input.lower()
        if input.startswith("jan"):
            monthOutput = "01"
        elif input.startswith("feb"):
            monthOutput = "02"
        elif input.startswith("mar"):
            monthOutput = "03"
        elif input.startswith("apr"):
            monthOutput = "04"
        elif input.startswith("may"):
            monthOutput = "05"
        elif input.startswith("jun"):
            monthOutput = "06"  
        elif input.startswith("jul"):
            monthOutput = "07"
        elif input.startswith("aug"):
            monthOutput = "08"
        elif input.startswith("sep"):
            monthOutput = "09"
        elif input.startswith("oct"):
            monthOutput = "10"
        elif input.startswith("nov"):
            monthOutput = "11"
        elif input.startswith("dec"):
            monthOutput = "12"
        else:
            monthOutput = "invalid month" 
        return monthOutput
    
    monthList = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]