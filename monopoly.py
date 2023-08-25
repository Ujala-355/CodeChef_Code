for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=max(a,b,c,d)
    y=(a+b+c+d)-x
    if x>y:
        print('YES')
    else:
        print('NO')
