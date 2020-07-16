#Uses python3

import sys

def lcs2(a, b, c):
    #write your code here
    
    
    n=len(a)
    m=len(b)  
    o=len(c)  
    L=[[[0 for x in range(m+1)] for y in range(n+1)] for z in range(o+1)]
    
    for i in range(o+1):
        for j in range(n+1):
            for k in range(m+1):
                if i==0 or j==0 or k==0:
                    L[i][j][k]=0
                elif(c[i-1]==a[j-1] and c[i-1]==b[k-1]):
                    L[i][j][k]=1+L[i-1][j-1][k-1]
                else:
                    L[i][j][k]=max(max(L[i][j-1][k],L[i-1][j][k]),L[i][j][k-1])
    print(L[o][n][m])


n=int(input())
a=list(input().split())
m=int(input())
b=list(input().split())
o=int(input())
c=list(input().split())
lcs2(a,b,c)
