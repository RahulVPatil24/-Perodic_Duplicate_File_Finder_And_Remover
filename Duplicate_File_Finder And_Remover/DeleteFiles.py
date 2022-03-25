import os
from File_Logger import *
from sys import *

def DeleteFiles(dict):

    results = list(filter(lambda x: len(x) > 1, dict.values()))
    
    iCnt = 0
    lst = []
    flag = False

    if len(results)>0:
        for result in results:
            for subresult in result:
                iCnt += 1
                if iCnt > 1:
                    lst.append(subresult)
                    os.remove(subresult)
            iCnt = 0
        flag = True
    else:
        print("No duplicate files found")
    
    File_Logger(lst,flag)
