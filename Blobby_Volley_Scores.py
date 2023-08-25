for _ in range(int(input())):
    n=int(input())
    u=input()
    x=0
    y=0
    s="A"
    for i in range(n):
        if u[i]==s[0]:
            if s=="A":
                x+=1
            else:
                y+=1 
        else:
            if s=="A":
                s="B"
            else:
                s="A"
    print(x,y)
    
