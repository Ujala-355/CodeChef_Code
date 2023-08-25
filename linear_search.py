for _ in range(int(input())):
    s=int(input())
    l=list(map(int,input().split()))
    n=int(input())
    t=0
    i=0
    while i<s:
        if l[i]==n:
            t=1
        i+=1
    if t>=1:
        print("YES")
    else:
        print("NO")
            
