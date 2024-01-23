#2.tuple(): (It is mutable - not editable)

a=12,  #(it is a tuple)
print(type(a))

tuple1=()  #empty tuple
tuple1=(34,67.8,23,"tuple",56,8.9,"hi",89)
print(tuple1[5])
print(tuple1[2:6])
print(tuple1[-2])  #from reverse
print(tuple1[:])

list2=list(tuple1) #type conversion
print(list2)

list2[3]=1800  #replace
list2.append("Python")
print(list2)

tuple1=tuple(list2)
print(tuple1)

b=13, 14, 15, "Program", 9.5,  #it is also a tuple
print(b)
