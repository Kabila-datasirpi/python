'''TRAFFIC LIGHT LOGIC WITH 4 DIRECTIONS USING PYTHON:
   Project done by : SUBAIR AHAMED S B.E(CSE)
                     Batch-no:191(Python)'''


#Automatic traffic ligjht logic for four directions:
import time
mode=input("Enter the mode:'auto or manual': ")
if(mode=="auto"):
    while True:
        #North direction
        print("North direction:->->->->")
        print("North: Green light")
        print("East-West-South: Red light")
        time.sleep(10)
        print("")
        print("North: Yellow light")
        print("East: Yellow light")
        print("West-South: Red light")
        time.sleep(5)
        print("")
        
        #East direction
        print("East direction:->->->->")
        print("East: Green light")
        print("North-West-South: Red light")
        time.sleep(10)
        print("")
        print("East: Yellow light")
        print("South: Yellow light")
        print("North-West: Red light")
        time.sleep(5)
        print("")

        #South direction:
        print("South direction:->->->->")
        print("South: Green light")
        print("North-East-West: Red light")
        time.sleep(10)
        print("")
        print("South: Yellow light")
        print("West: Yellow light")
        print("North-East: Red light")
        time.sleep(5)
        print("")

        #West direction
        print("West direction:->->->->")
        print("West: Green light")
        print("North-East-South: Red light")
        time.sleep(10)
        print("")
        print("West: Yellow light")
        print("North: Yellow light")
        print("East-South: Red light")
        time.sleep(5)
        print("")

    
#Manual traffic light logic for four directions:
elif(mode=="manual"):
    while True:
        print("")
        direction = input("Enter traffic light direction (North, South, East, West): ")
        light = input("Enter traffic light color: ")
        print("")
        #North direction:
        if(direction=="north"):
            
            if(light=="green"):
                print("north: Green signal and Go")
                print("east-west-south: Red signal and Stop")
                
            elif(light=="yellow"):
                print("north: Yellow signal and Wait")
                print("east: Yellow signal and Wait")
                print("west-south: Red signal and Stop")
                
            elif(light=="red"):
                print("north: Red signal and Stop")
                print("east: Green signal and Go")
                print("west-south: Red signal and Stop")
                
            else:
                print("Invalid input")

        #East direction:        
        elif(direction=="east"):
            
            if(light=="green"):
                print("east: Green signal and Go")
                print("north-west-south: Red signal and Stop")
                
            elif(light=="yellow"):
                print("east: Yellow signal and Wait")
                print("south: Yellow signal and Wait")
                print("north-west: Red signal and Stop")
                
            elif(light=="red"):
                print("east: Red signal and Stop")
                print("south: Green signal and Wait")
                print("north-west: Red signal and Stop")
                
            else:
                print("Invalid input")

        #South direction:
        elif(direction=="south"):
            
            if(light=="green"):
                print("south: Green signal and Go")
                print("north-east-west: Red signal and Stop")
                
            elif(light=="yellow"):
                print("south: Yellow signal and Wait")
                print("west: Yellow signal and Wait")
                print("north-east: Red signal and Stop")
                
            elif(light=="red"):
                print("south: Red signal and Stop")
                print("west: Green signal and Wait")
                print("north-east: Red signal and Stop")
                
            else:
                print("Invalid input")

        #West direction:
        elif(direction=="west"):
            
            if(light=="green"):
                print("west: Green signal and Go")
                print("north-east-south: Red signal and Stop")
                
            elif(light=="yellow"):
                print("west: Yellow signal and Wait")
                print("north: Yellow signal and Wait")
                print("east-south: Red signal and Stop")
                
            elif(light=="red"):
                print("west: Red signal and Stop")
                print("north: Green signal and Wait")
                print("east-south: Red signal and Stop")
                
            else:
                print("Invalid input")

        else:
            print("Invalid input")

else:
    print("Invalid input")
    



