for _ in range(int(input())):
    a,b,c,d,e,f=list(map(int,input().split()))
    x=(a+b+c+d+e)
    y=x*f 
    if y<=120:
        print("No")
        
    else:
        print("Yes")
            
        
