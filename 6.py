"""
Given a signed 32 bit integer "x" with its digits reversed. if reversing "x" causes the value 
to go outside the signed 32 bit integer range, then return 0.
ex:-- x = 123
output:- 321 
"""

x = int(input("Enter the number\n"))
sign = -1 if x < 0 else 1
x = abs(x)
reverse = 0
while x > 0:
    remainder = x % 10
    reverse = reverse * 10 + remainder
    x //= 10  
reverse =reverse * sign
if -2**32 < x < (2**32 -1) and -2**32 < reverse < (2**32 -1):
    print(f"reverse: {reverse}")

else:
    print(0)






