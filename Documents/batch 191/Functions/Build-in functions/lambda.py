i=eval(input("Enter the value1:"))
x=lambda a:a*2
print(x(i))  #i will be assigned to a.

j=eval(input("Enter the value2:"))
k=eval(input("Enter the value3:"))
l=eval(input("Enter the value4:"))
m=eval(input("Enter the value5:"))
y=lambda b,d,e,f:b+d*e-f+45
print(y(j,k,l,m))  #j,k,l,m will be assigned to b,d,e,f.

#1st value will be assigned to 1st variable, similarly next values assigned for consecutive variables.
