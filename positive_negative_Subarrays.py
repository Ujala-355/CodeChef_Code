for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    p=0
    q=0
    for j in range(1,n+1):
        if l[j-1]>0:
            p+=j 
        else:
            q+=j 
    print(abs(p-q))
