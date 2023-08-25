
for i in range(int(input())):
    x=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c1=0
    for j in range(1,x):
        if a[j]>a[c1]:
            c1=j 
        elif a[j]==a[c1] and b[j]>b[c1]:
            c1=j 
    print(c1+1)

