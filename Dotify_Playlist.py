for _ in range(int(input())):
    n,k,l=map(int,input().split())
    l1=[]
    for i in range(n):
        a,b=map(int,input().split())
        if b==l:
            l1.append(a)
    l1.sort()
    l1=l1[::-1]
    if len(l1)<k:
        print("-1")
    else:
        print(sum(l1[:k]))
        
