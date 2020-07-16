# Uses python3
import sys

def optimal_weight(W, w,n):
    # write your code here
    w.sort()
    arr=[[0 for j in range (W+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                arr[i][j]=0
            elif j<w[i-1]:
                arr[i][j]=arr[i-1][j]
            else:
                arr[i][j]=max(arr[i-1][j],w[i-1]+arr[i-1][j-w[i-1]])
    print(arr[i][j])
        


W2=list(map(int, input().split()))
W=W2[0]
n=W2[1]
w = list(map(int, input().split()))
optimal_weight(W, w,n)
