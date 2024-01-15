#Write a program to print the Fibonacci series up to a given limit using a for loop.
num = int(input("Enter a number:"))
x = 0
y = 1
z = 0
while z <= num:
    print(z)
    x = y
    y = z
    z = x + y
    #print(z)

    
    