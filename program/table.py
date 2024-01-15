#Write a program to print the multiplication table of a given number using a while loop.

num = int(input("Enter a number for its table:"))
i = 1
while i<=10:
    tab = num*i
    print(f"{num} x {i} = {tab}")
    i+=1
