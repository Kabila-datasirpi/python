import time
while(True):
    try:
        x=eval(input("Enter x: "))
        y=eval(input("Enter y: "))
        c=x/y
        print(c)
        
    except NameError:          #if variable is not declared
        print("Variable not defined")
        
    except TypeError:          #if datatype differs 
        print("Please enter valid data")
        
    except ZeroDivisionError:  #if zero used for division
        print("Zero value is not divisible")
        
    except:
        print("Some error occured")
    else:
        print("Runs Successfully...")
        try:
            d=input("Enter d: ")
            print(d)
            
        except TypeError:
            print("Error occured")
            
        else:
            print("2nd logic working....")

    finally:
        print("Error occurs or not, but it will get printed")
    time.sleep(3)
