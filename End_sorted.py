for _ in range(int(input())):
    x=int(input())
    l=list(map(int, input().split()))
    i1,ix1=0,0
    for i in range(x):
        if l[i]==1:
            i1 = i
        if l[i]==x:
            ix1=i
    if i1>ix1:
        print(i1+x-ix1-2)
    else:
        
        print(i1+x-ix1-1)
