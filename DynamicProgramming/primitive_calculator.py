def new(n):
        arr=[0]*(n+1)
        arr[0]=0
        if n==1:
            print("0")
            print("1")
            return 0
        elif(n==2 or n==3):
            print(1)
            print("1 ",n)
            return 0
        else:
            arr[1]=0
            arr[2]=1
            arr[3]=1
            l=[]
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(0)
            for i in range(4,n+1):
                if(i%2==0 and i%3!=0):
                    if(min(arr[int(i/2)],arr[i-1])==arr[int(i/2)]):
                        abc=int(i/2)
                    else:
                        abc=i-1
                    arr[i]=1+arr[abc]
                elif(i%3==0 and i%2!=0):
                    if(arr[int(i/3)]>arr[i-1]):
                        abc=i-1
                    else:
                        abc=int(i/3)
                    arr[i]=1+arr[abc]
                elif(i%2==0 and i%3==0):
                    if(min(arr[int(i/3)],arr[i-1],arr[int(i/2)])==arr[int(i/3)]):
                        abc=int(i/3)
                    elif(min(arr[int(i/3)],arr[i-1],arr[int(i/2)])==arr[int(i/2)]):
                        abc=int(i/2)
                    else:
                        abc=i-1
    
                    arr[i]=1+arr[abc]
                else:
                    abc=i-1
                    arr[i]=1+arr[i-1]
                l.append(abc)
        s=len(l)-1
        q=[]
        q.append(n)
        while(l[s]!=0):
            q.append(l[s])
            s=l[s]
        q.append(1)
        q.sort()
        print(arr[n])
        for i in q:
            print(i,end=" ")
        return 0

    
   
n = int(input())
res=new(n)
