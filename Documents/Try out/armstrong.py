num=int(input("Enter the number:"))
m=str(num)
l=len(m)
count=0
for i in m:
    count+=int(i)**l
if(num==count):
    print(num,"is a armstrong")
else:
    print(num,"is not a armstrong")
    
