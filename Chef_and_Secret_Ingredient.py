for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if i>=b:
            c=1
            break
    if c==0:
        print("NO")
    else:
        print("YES")
        
