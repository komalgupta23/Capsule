#Write a program to find the smallest element in an array using a while loop.
array = (45, 32, 54, 23, 43,76 )
min = array[0]
for a in array:
    if a < min:
        min = a
print(min)