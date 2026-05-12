"""
Given an integer x, return true if x is palindrome and false otherwise
ex:-- 121 
output:-- true
explaination:- 121 reads as 121 from left to right and from right to left
"""

x = 1331
if x > 0:
    sign =1
else:
    sign = -1
y = abs(x)
reverse = 0
while y >0:
    remainder = y%10
    reverse = reverse*10 + remainder
    y = y//10

if x == reverse :
    print("True")

else:
    print("False") 
