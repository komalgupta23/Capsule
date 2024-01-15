#Write a program to print the multiplication table of numbers from 1 to 5 using a for loop.
for i in range(1,6):
    print("\nMULTIPLICATION OF",i)
    for num in range(1,11):
        tab = i * num
        print(f"{i} x {num} = {tab}" )