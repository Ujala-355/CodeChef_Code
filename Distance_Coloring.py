for _ in range(int(input())):
    n,k=map(int,input().split())
    a=1
    for i in range(n):
        a=(a*k)%(10**9+7)
        if k>1:
            k=k-1
    print(a)
