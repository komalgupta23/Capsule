i = int(input("Enter a number:"))
d = i
rev = 0 
while i > 0:
    rev = rev * 10 + i % 10
    i //= 10
print(f"Reverse of {d} is {rev}.")

