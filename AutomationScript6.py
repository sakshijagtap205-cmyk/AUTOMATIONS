import sys

def main():
    Border = "-"*40
    print(Border)
    print("MArvellous Automation Script")
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
            DirectoryName = sys.argv[1]
            print("DirectoryName is :",DirectoryName)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
   
    print(Border)
    print(" thank you for using MArvellous Automation Script")
    print(Border)

if __name__=="__main__":
    main()