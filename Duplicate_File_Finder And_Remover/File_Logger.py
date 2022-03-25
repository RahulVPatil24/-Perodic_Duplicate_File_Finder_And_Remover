import os
from datetime import datetime
from Send_Mail import *
from sys import *

def File_Logger(data, flag,FolderName = 'duplicate.logs'):

    CurrentDate = datetime.now().strftime("%d_%m_%Y-%I_%M")+".txt"

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    if flag == True:
        File_Path = os.path.join(FolderName,CurrentDate)
        print(File_Path)

        fd = open(File_Path,"w")

        for element in data:
            fd.write("%s\n"%element)

        fd.close()

    else:
        File_Path = os.path.join(FolderName,'No-Duplicates'+CurrentDate)
        print(File_Path)

        fd = open(File_Path,"w")

        for element in data:
            fd.write("%s\n"%element)
    
        fd.close()

    Send_Mail(File_Path)