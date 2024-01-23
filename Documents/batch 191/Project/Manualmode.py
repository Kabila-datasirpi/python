mode=input("Enter the mode:Auto or manual: ")
if(mode=="manual"):
    while True:
        direction = input("Enter traffic light direction (North, South, East, West): ")
        light = input("Enter traffic light color: ")
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
                print("east: Green signal and Wait")
                print("west-south: Red signal and Stop")
                
            else:
                print("Invalid input")
                
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
