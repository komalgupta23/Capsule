#Write a program to calculate the sum of digits of a number using a for loop.
i = int(input("Enter a number:"))
sum = 0
for digit in str(i):
    sum += int(digit)

print("sum of digit is",sum)    
