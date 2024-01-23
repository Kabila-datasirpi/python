import time
n=eval(input("enter the value:"))
while(n<=100):
    print(n)
    n+=n
    time.sleep(1)
print("Here, the series of numbers")
