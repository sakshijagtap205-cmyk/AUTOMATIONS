import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous"):
    Border = "-"*40
    
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ", "_")    #replace is inbuilt function
    LogFileName = LogFileName.replace(":","_")
    
    print("Log File gets created with Name:", LogFileName)
    
    fobj = open(LogFileName,"w")
    
    fobj.write(Border+"\n")
    
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Border+"\n\n")
    
    fobj.write("Files from the directory are :\n\n")
    fobj.write(Border+"\n")
    
    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        for fname in  FileName:
            fobj.write(fname+"\n")
            
            fobj.write(Border+"\n")
            fobj.write("Log files get createde at :"+timestamp)
            fobj.write("\n"+Border+"\n")
            
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
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                
           
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
   
    print(Border)
    print(" thank you for using MArvellous Automation Script")
    print(Border)

if __name__=="__main__":
    main()