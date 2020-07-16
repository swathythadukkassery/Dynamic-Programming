#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    
    
    n=len(a)
    m=len(b)    
    L=[[0 for x in range(m+1)] for y in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                L[i][j]=0
            elif(a[i-1]==b[j-1]):
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i][j-1],L[i-1][j])
    print(L[n][m])


n=int(input())
a=list(input().split())
m=int(input())
b=list(input().split())
lcs2(a,b)
