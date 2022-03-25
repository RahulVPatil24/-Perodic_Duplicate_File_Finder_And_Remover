import schedule
from sys import *
import time
import schedule
from FindDuplicates import *
import Check_Connection

def main():

        print("-----Duplicate File Remover Automation Script-----")

        print("Application name: "+argv[0])

        if(len(argv) != 2):
            print("ERROR: Invalid number of arguments")
            exit()
        
        if(argv[1] == "-h") or (argv[1] == "-H"):
            print("This script is used to traverse specific directory and delete duplicate files")
            exit()

        if(argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage: ApplicationName AbsolutePath_of_Directory")
            exit()

        conection = Check_Connection.Check_Connection()
        
        if conection == True:
            try:
                print("Scheduler starts......")

                startTime = time.time() 
            
                schedule.every(1).minutes.do(FindDuplicates, argv[1])

                endtime = time.time()

                print('Took %s seconds to evaluate.'%(endtime - startTime))

                while True:
                    schedule.run_pending()
                    time.sleep(1)

            except ValueError:
                print("ERROR: Invalid datatype of input")
            except Exception as E:
                print("ERROR: Invalid input",E)
            
        else:
            print("check your connection....")
            exit()

if __name__ == "__main__":
    main()