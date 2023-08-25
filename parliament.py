for i in range(int(input())):
    n,x=map(int,input().split())
    if (n-x)<=x:
        print('YES')
    else:
        print('NO')
