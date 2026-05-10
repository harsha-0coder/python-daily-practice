"""
given a string s , return the longest palindromic substring in s 
ex:--"babad"
o/p:-- bab
"""

S = "babad"
A = []
B = []
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        A.append(S[i:j])

for l in A:
    if l[:] == l[::-1]:
        B.append(l)
 
print(max(B, key=len))






