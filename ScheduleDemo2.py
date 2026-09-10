import datetime
import schedule
import time


def Display():
    print("jay ganesh...", datetime.datetime.now())

def main():
    print("Automation print startrd")    
    
    schedule.every(1).minute.do(Display)
    
    #issue


if __name__=="__main__":
    main()