#3.Dictionary{}:  - Key-value pairs  (it is immutable)

dict1={}  #empty dictionary
dict1={"Name":"Ramesh","Age":30,"Gender":"Male"}

dict1["Name"]="Ahamed"  #change value for key
dict1["Height"]=170   #add new key & values

print(dict1)
print(dict1.keys())    #to print all keys
print(dict1.values())  #to print all values
del dict1["Height"]   #to delete a value
print(dict1)

for key,values in dict1.items():  #to print all keys and values
    print(key)
    print(values)

list1=list(dict1.values()) #type conversion either keys or values
print(list1)
