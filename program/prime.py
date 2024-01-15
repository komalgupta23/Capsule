#Write a program to check if a given number is prime or not using a while loop.
i = 2
num = int(input("Enter a number:"))
if num < 2:
    print("it is not prime number")
else:
    while  i < num:
        if num % i == 0:
            print("it is not prime number")
            break
        i += 1
    else:
     print("it is  prime number")