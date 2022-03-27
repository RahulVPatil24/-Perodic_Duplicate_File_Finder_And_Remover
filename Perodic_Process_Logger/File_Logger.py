import os
from datetime import datetime
from Send_Mail import *
from sys import *
import Send_Mail

def File_Logger(data, FolderName = 'Process.logs'):

    current_date_time = datetime.now().strftime("%d_%m_%Y-%I_%M")+".txt"

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    File_Path = os.path.join(FolderName,current_date_time)
    print(File_Path)

    fd = open(File_Path,"w")

    for element in data:
        fd.write("%s\n"%element)
    
    fd.close()

    Send_Mail.Send_Mail(File_Path)