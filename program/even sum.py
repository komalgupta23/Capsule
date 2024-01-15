#Write a program to find the sum of all even numbers between 1 and 100 using a for loop.
sum=0
for i in range(1,101):
    if i % 2 == 0:
        sum = sum + i
print("The sum of even is",sum)
        
    