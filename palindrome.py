i = int(input("Enter a number:"))
orig = i
rev = 0 
while i > 0:
    rev = rev * 10 +i % 10
    i //= 10
if rev == orig:
    print("palindrome number")
else:
    print("Not an palindrome number")