#Write a program to find the largest element in an array using a for loop.
arr = (45, 32, 54, 23, 43,76 )
max_element = arr[0]
for num in arr:
    if num > max_element:
        max_element = num
print("Largest element in the array:", max_element)
        
    