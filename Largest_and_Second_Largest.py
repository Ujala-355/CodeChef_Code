for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m1=0
    m2=0
    for j in l:
        if j>m1:
            m1=j
    for k in l:
        if k>m2 and k<m1:
            m2=k
    print(m2)
