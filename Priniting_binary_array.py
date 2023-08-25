for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    s=" "
    for j in l:
        if j==0:
            s=s+" "+"1"
        elif j==1:
            s=s+" "+"0"
        else:
            s=s+" "+str(j)
    print(s)
            
