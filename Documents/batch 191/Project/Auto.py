import time
mode=input("Enter the mode:Auto or manual: ")
if(mode=="auto"):
    while True:
        #North direction
        print("North direction:->->->->")
        print("North: Green light")
        print("East-West-South: Red light")
        time.sleep(10)
        print("North: Yellow light")
        print("East: Yellow light")
        print("West-South: Red light")
        time.sleep(5)
        
        #East direction
        print("East direction:->->->->")
        print("East: Green light")
        print("North-West-South: Red light")
        time.sleep(10)
        print("East: Yellow light")
        print("South: Yellow light")
        print("North-West: Red light")

        #South direction:
        print("South direction:->->->->")
        print("South: Green light")
        print("North-East-West: Red light")
        time.sleep(10)
        print("South: Yellow light")
        print("West: Yellow light")
        print("North-East: Red light")
        time.sleep(5)

        #West direction
        print("West direction:->->->->")
        print("West: Green light")
        print("North-East-South: Red light")
        time.sleep(10)
        print("West: Yellow light")
        print("North: Yellow light")
        print("East-South: Red light")
        time.sleep(5)
