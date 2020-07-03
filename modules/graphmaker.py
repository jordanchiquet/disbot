from modules.renardusers import renardusers
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getgraph(column):
    usersinit = renardusers(1, column)
    graphdataraw = usersinit.getgraphdata()
    print(graphdataraw)
    columns = ("user", "fucks given")
    graphdata = pd.DataFrame.from_records(graphdataraw, columns = columns)
    graphdata.plot(x = "user", y = "fucks given", kind = "bar")
    plt.savefig('graph.png')
    # return(graphdata)

