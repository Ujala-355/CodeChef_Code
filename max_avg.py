for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    sum=0
    c=0
    max=0
    i=0
    l1=[0]*n
    index=0
    while i<n:
        sum+=l[i]
        c+=1
        x=sum/c
        print(x)
        if x>max:
            max=x
            index=i 
        i+=1
    print("max",max,index)
       
   
