

def get_change(m):
    l=m+1
    arr=[0]*(l+4)
    arr[1]=1
    arr[2]=2
    arr[3]=1
    arr[4]=1
    if(m<=4):
        return(arr[m])
    for i in range(5,l):
        arr[i]=min(arr[i-1],arr[i-3],arr[i-4])+1

    #write your code here
    return arr[i]


m = int(input())
print(get_change(m))
