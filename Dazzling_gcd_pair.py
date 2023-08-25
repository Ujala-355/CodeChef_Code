for i in range(int(input())):
    a,b=map(int,input().split())
    if a%2==0 and a+2<=b:
        print(a,a+2)
    elif a+3<=b:
        if a%3==0:
            print(a,a+3)
        else:
            print(a+1,a+3)
    else:
        print(-1)
        
