for _ in range(int(input())):
    g=int(input())
    if g%2!=0:
        print(-1)
    else:
        for i in range(g,0,-1):
            if i==1:
                print(i)
            else:
                print(i,end=" ")
