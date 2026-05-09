"""
Given two sorted arrays num1 and num2 of size m and n respectively return the medain of the two sorted array
ex:-- num1 = [1,3]
num2 = [2]
output:- 2 
explanation:-- merged array = [1,2,3] and median = 2 
"""

num1 = [1,3]
num2 = [2,4]
num1.extend(num2)
num1.sort()

n = len(num1)

if n % 2 != 0:
    median = num1[n//2]

else:
    median = (num1[n//2 - 1] + num1[n//2]) / 2


print(median)
