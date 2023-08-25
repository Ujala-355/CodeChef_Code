for _ in range(int(input())):
    x,y=map(int,input().split())
    a=str(x*y)
    l=list(a)
    c=0
    c1=0
    for i in l:
       c+=1 
    if c==5:
        print("YES")
    else:
        print("NO")
