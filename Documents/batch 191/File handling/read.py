file=open("Python_class.txt","r")
#print(file.read())     #--> reads and show all the content

#print(file.readline()) #--> reads and show 1st line

#print(file.readlines()) #--> reads and show all data in a list

##list1=file.readlines()  #--> reads and show data as seperate lines
##count=1
##for i in list1:
##    print("Line no-",count,i)
##    count+=1

list1=file.readlines()   #--> reads and show the lines needed
print(list1[1:9])
