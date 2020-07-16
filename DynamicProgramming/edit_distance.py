# Uses python3
def edit_distance(s, t):
    #write your code here
    m=len(s)
    n=len(t)
    arr=[[0 for i in range(n+1)]for i in range(m+1)]
    for i in range (m+1):
        for j in range(n+1):
            if i==0:
                arr[i][j]=j
            elif j==0:
                arr[i][j]=i
            elif s[i-1] == t[j-1]: 
                arr[i][j] = arr[i-1][j-1] 
            else: 
                arr[i][j] = 1 + min(arr[i][j-1],         
                                   arr[i-1][j],         
                                   arr[i-1][j-1])    
  
    return arr[m][n]


print(edit_distance(input(), input()))
