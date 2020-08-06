from modules.renardusers import renardusers
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getgraph(column, serverid, rawcount: bool = False):
    usersinit = renardusers(1, column, serverid=serverid)
    totalcountinit = renardusers(1, "wordcount", serverid=serverid)
    graphdatarawcolumn = usersinit.getgraphdata()
    if rawcount:
        finaldata = graphdatarawcolumn
    if not rawcount:
        graphdatarawmsgcount = totalcountinit.getgraphdata()
        print(graphdatarawmsgcount)
        columnmembervalues = []
        columnnumvalues = []
        msgcountnumvalues = []
        print("fail 1")
        for x in graphdatarawcolumn:
            columnmembervalues.append(x[0])
            columnnumvalues.append(x[1])
        for x in graphdatarawmsgcount:
            msgcountnumvalues.append(x[1])
        print("failing here")
        ratiovalues = list(np.array(columnnumvalues) / np.array(msgcountnumvalues))
        finaldata = createtuple(columnmembervalues, ratiovalues)
    # print(graphdataraw
    # column)
    columns = ("", column)
    graphdata = pd.DataFrame.from_records(finaldata, columns = columns)
    graphdata.plot(x = "", y = column, kind = "bar")
    plt.tight_layout()
    plt.savefig('graph.png')
    # return(graphdata)


def createtuple(list1, list2):
    graphtuple = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return(graphtuple)
