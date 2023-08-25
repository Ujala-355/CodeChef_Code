for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l1 = [0]*n
    i=0
    while i<n:
        l1[i]=l[n-i-1]
        i+=1
    print(l1)
