num = int(input("Enter a number: "))
sum = 0
m = str(num)
n = len(m) #len() retunrs the number of characters in a string.
for i in m:
    sum += int(i) ** n
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
