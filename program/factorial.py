#Write a program to calculate the factorial of a number using a for loop.

num = int(input("Enter a number:"))
fact=1
for i in range(2,num+1):
    fact = fact*i
print(f"The factorial of {num} is {fact}")