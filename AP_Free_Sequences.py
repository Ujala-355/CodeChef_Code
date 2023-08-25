for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                if l[k]-l[j]==l[j]-l[i]:
                    c=1
                    break
                    
    if c==1:
        print("NO")
    else:
        print("YES")
            
