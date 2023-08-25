for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    max=0
    while i<len(l):
        if l[i]>l[max]:
            max=i
        i+=1
    if max==0:
        secondmax=1
    else:
        secondmax=0
    j=0
    while j<len(l):
        if l[j]>l[secondmax] and j!=max:
            secondmax=j
        j+=1
    print(l[secondmax])
    
