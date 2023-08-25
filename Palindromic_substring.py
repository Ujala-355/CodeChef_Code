for _ in range(int(input())):
    n=input()
    s=input()
    c=1
    for i in range(len(n)):
        for j in range(len(s)):
            if n[i]==s[j]:
                c=0
                break
    if c==0:
        print("Yes")
    else:
        print("No")
    
