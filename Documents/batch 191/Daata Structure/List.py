#Data Structure:
#1.Build in DS
#2.Userdefined DS

#List[],Tuple(),Dictionary{},Set{}

#1.List[] (mutable)
list1=[]    #empty list creation
list1=[12,34,56,67.5,"hello",6,98,4.2,90,"hi"] #mixed datatype data
print(list1[1])
print(list1[1:4])  # 1 to 4
print(list1[:6])  # 0 to 6
print(list1[:])  #prints all data
print(type(list1))
list1[2]=34.7   # to change data of that index
list1.append("Welcome")  #to append data to list.
list1.insert(3,"thalapathy")  #to insert data at the index
x=list1.pop(0) #to remove the data.
print(x)
print(list1)
del list1[6]  #to delete the data.
print(list1)
for i in list1:
    print(i)

for j in range(0,10):
    list1.append(j)
print(list1)

