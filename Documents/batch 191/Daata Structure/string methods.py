#String Methods:

str1 = 'Welcome Everyone'
print(len(str1))
print(str1[2:8])
print(str1.upper())
print(str1.lower())
print(str1.replace("Welcome","ThankYou"))
print(str1[::-1])  # to reverse

for i in str1:
    if(i=="e" or i=="o"): 
        continue
    print(i,end="")
