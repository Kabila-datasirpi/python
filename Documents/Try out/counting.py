str1=input("Enter the input:")
str2={}
lower=str1.lower()
for letter in lower:
    if letter.isalpha():
        str2[letter]=str2.get(letter,0)+1
for letter, count in str2.items():
    print(f"{letter}->{count}")
    
