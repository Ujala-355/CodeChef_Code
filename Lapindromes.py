for i in range(int(input())):
    s=input()
    d=len(s)
    str1=''
    str2=''
    if d%2==0:
        str1=s[:d//2]
        str2=s[d//2:]
    else:
        str1=s[:d//2]
        str2=s[d//2+1:]
    l1=list(str1)
    l2=list(str2)
    l1.sort()
    l2.sort()
    if l1==l2:
        print('YES')
    else:
        print('NO')
