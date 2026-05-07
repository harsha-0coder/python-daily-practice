"""
your aregiven two non-empty lists representing two non-negative integers. the digits are stored in reverse order
add the two numbe and return sum , also the output list in reverse
Ex:-- given, l1 = [1,2,3]
             l2 =[4,5,6]
             output = [5,7,9] and sum = 975
             explaination = 321 + 654 =975
"""

l1 = [1,2,3]
l2 = [4,5,6]
l1.reverse()
l2.reverse()
num1 = int(''.join(map(str,l1)))
num2 = int(''.join(map(str,l2)))
sum1 = num1 + num2
out =[]
for i in str(sum1):
    out.append(int(i))

out.reverse()
print(sum1)
print(out)
