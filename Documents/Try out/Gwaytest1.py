#Input:a3b4c5 and Expected output:A9B16C25 Note: Your code should be dynamic

input_str=input("Enter the input:")
characters=""
numbers=""
for x in input_str:
    if x.isalpha():
        characters+=x
    elif x.isdigit():
        numbers+=x

output_str=""
for i in range(len(characters)):
    x=characters[i].upper()
    y=int(numbers[i])**2
    output_str+=f"{x}{y}"

print(output_str)
