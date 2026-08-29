import sys
import os

def DirectoryScanner(DirectoryPath):
    print("Files from the directory are :")
    
    fobj = open("MarvellousLog.txt","w")
    fobj.write("Marvellous Automation Script\n")
    
    fobj.write("Files from the directory are :\n")
    
    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        for fname in  FileName:
            fobj.write(fname+"\n")
            
    fobj.close()

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this auromation script is usse to travel the directory")
            print("for better usage please check --u flag")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please execute the script as")
            print("Python FileName.py DirectoryuName")
            print("Directory NAme should be absolute path of the directory")
        else:
            DirectoryScanner(sys.argv[1])
           
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
   
    print(Border)
    print(" thank you for using MArvellous Automation Script")
    print(Border)

if __name__=="__main__":
    main()