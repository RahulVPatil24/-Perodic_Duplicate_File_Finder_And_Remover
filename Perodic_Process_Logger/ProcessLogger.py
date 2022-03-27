from multiprocessing.dummy import Process
import psutil
from sys import *
import schedule
import time
import Check_Connection
import File_Logger

def ProcessLogger():
    
    listProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            #pinfo['vms'] = proc.memory_full_info().vms/(1024 * 1024)

            listProcess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    File_Logger.File_Logger(listProcess)

def main():

    print("Python Automation")

    print("Process Monitiring Tool With Memory Usage")

    if Check_Connection.Check_Connection() == True:

        schedule.every(1).minutes.do(ProcessLogger)

        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Check your connection\n")

if __name__ == "__main__":
    main()