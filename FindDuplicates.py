import os
import hashfile
import DeleteFiles
from sys import *

def FindDuplicates(path):

    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for DirectoryName, SubDirectory, FileList in os.walk(path):

            print("Current folder is: "+DirectoryName)

            for subD in SubDirectory:
                print("Sub Folder of"+DirectoryName+"is: "+subD)

            for file in FileList:
                path = os.path.join(DirectoryName, file)
                File_Hash = hashfile.hashfile(path)

                if File_Hash in dups:
                    dups[File_Hash].append(path)
                else:
                    dups[File_Hash] = [path]
                
        DeleteFiles.DeleteFiles(dups)
    else:
        print("Invalid Path")