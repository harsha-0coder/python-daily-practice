"""
given an array of integers "nums" and an integer "target", return indices of the two numbers such 
that they add upto target
ex:-- 
Given nums =[ 2,7,11,15] and target = 9 
output:- [0,1] as 2 +7 = 9 
"""

num = [10,15,20,25,30]
target = 50

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] +num[j] == target:
            print([i,j])

        
        
   