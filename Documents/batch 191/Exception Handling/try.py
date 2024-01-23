import time
while(True):
    try:
        x=20
        y=0
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
    time.sleep(2)
