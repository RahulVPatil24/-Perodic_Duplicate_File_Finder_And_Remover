import sys
import subprocess
import schedule
import time
import File_Logger

def ProcessList(path):
    l = []
    li = []
    with open(path)as fp:
        for line in fp:
           l.append('"'+line+'"')

        for str in l:
            subprocess.Popen(str,shell=True)
            li.append('"'+str+'"')

    File_Logger.File_Logger(li)

def main():

    print("-----Process Launcher-----")

    print("Application Name: "+sys.argv[0])

    if(len(sys.argv)!= 2):
        print("ERROR: Invalid number of arguments")
        exit()

    if(sys.argv[1] == 'h') or (sys.argv[1] == 'H'):
        print("This script is used to open URL which are written in one file")
        exit()

    if(sys.argv[1] == "-u") or (sys.argv[1] == '-U'):
        print("usage: ApplicationName Name_Of_File")
        exit()

    try:
        
        schedule.every().days.at("01:40").do(ProcessList,sys.argv[1])
        
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:

        print("ERROR: Invalid datatype pf input")

    except Exception as E:

        print("ERROR: Invalid input",E)

if __name__ == "__main__":
    main()