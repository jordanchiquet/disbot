from modules.renardusers import renardusers
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getgraph(column):
    usersinit = renardusers(1, column)
    graphdataraw = usersinit.getgraphdata()
    print(graphdataraw)
    columns = ("", column)
    graphdata = pd.DataFrame.from_records(graphdataraw, columns = columns)
    graphdata.plot(x = "", y = column, kind = "bar")
    plt.tight_layout()
    plt.savefig('graph.png')
    # return(graphdata)

