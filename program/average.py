#Write a program to calculate the average of a list of numbers using a for loop.
list = (12, 34, 54, 43, 21)
sum=0
avg = 0
for i in list:
    sum = sum + i
    avg = sum/len(list) 
print(f"The average of list is {avg}")    