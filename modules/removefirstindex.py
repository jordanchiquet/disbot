def removefirstindex(thelist):
    print("list before removing first index: [" + str(thelist) + "]")
    del thelist[0]
    print("list after removing the first index: [" + str(thelist) + "]")
    return(thelist)