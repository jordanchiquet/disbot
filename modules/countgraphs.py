import matplotlib.pyplot as plt
import numpy as np

from modules.sqlHandler import sqlMektanixDevilDog as mek

#x = user
class GraphMaker:

    def __init__(self, serverid: int, countCol: str):
        self.serverid = str(serverid)
        self.su = "serveriduserid"
        self.countCol = countCol + "count"
        self.queryField = "%" + self.serverid + "%"
        print("GraphMaker initialized")
    
    def main(self):
        if self.getStatLists():
            self.plotMaker()
            return(True)
        else:
            return(False)

    

    def getStatLists(self) -> bool:
        print("getStatList started")
        specificColStatDump = self.getSpecificColStat()
        wordCountStatDump = self.getWordStat()
        if specificColStatDump is None or wordCountStatDump is None:
            print("getStatLists got none for a stat dump")
            return False
        self.nameList, self.specCountList, self.wordCountList = [], [], []
        for item in specificColStatDump:
            if item[1] > 0:
                self.nameList.append(item[0])
                self.specCountList.append(item[1])
        for item in wordCountStatDump:
            if item[0] in self.nameList:
                self.wordCountList.append(item[1])
        #TODO test if this is pulling accurate numbers... mostly that its getting the right ones
        # for each user, and that the word count and specific count are for the same user
        print("self.nameList: [" + str(self.nameList) + "]\n"
        "self.specCountList: [" + str(self.specCountList) + "]\n"
        "self.wordCountList: [" + str(self.wordCountList) + "]")
        return True
    
    def getGraphArrays(self):
        print("getGraphArray started")
        self.bar_y = np.divide((self.specCountList) / (self.wordCountList))



    def getSpecificColStat(self):
        print("getSpecificColStats started")
        resultColumn = "username, " + self.countCol
        specificColStatDump = mek(purpose="read", table="userstats", resultColumn=resultColumn,
        queryColumn=self.su, queryField=self.queryField)
        print("specificColStatDump: [" + str(specificColStatDump) + "]")
        return(specificColStatDump)
    
    def getWordStat(self):
        print("getWordStat started")
        resultColumn = "username, wordcount"
        wordCountDump = mek(purpose="read", table="userstats", resultColumn=resultColumn,
        queryColumn=self.su, queryField=self.queryField)
        print("wordCountDump: [" + str(wordCountDump) + "]")
        return(wordCountDump)
    

    def plotMaker(self):
        print("plotMaker started")
        #TODO make the fig/ax_array self variables and access outside this function. 
        # one for bar, one for pie, one for helping and writing labels
        self.makeAxArrays()
        self.makeBarGraph()
        self.makePieChart()
        plt.show() 
    
    def makeAxArrays(self):
        print("makeAxArrays started")
        self.fig = plt.figure(constrained_layout=True)
        self.ax_array = (self.fig).subplots(1, 2, squeeze=False)

    def makeBarGraph(self):
        print("makeBarGraph started")
        barHeight = np.divide(self.specCountList, self.wordCountList)
        self.ax_array[0, 0].bar(x=self.nameList, height=barHeight)
        # self.ax_array[0, 0].xlabel("fucks given")
        # self.ax_array[0, 0].set_xticks(self.nameList, rotation=90)
        # self.ax_array[0, 0].xticks(rotation=90)
        # self.ax_array[0, 1].bar(x=self.nameList, height=barHeight)
        


    def makePieChart(self):
        print("makePieChart started")
        self.ax_array[0, 1].pie(self.specCountList, labels=self.nameList, shadow=True, startangle=90)
        self.ax_array[0, 1].axis('equal')


    def makeAutopct(self):
        print("buildRawPie started")



