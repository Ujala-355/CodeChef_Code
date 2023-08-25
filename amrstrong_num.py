'''for _ in range(int(input())):
    n=int(input())
    s=str(n)
    n_len=len(s)
    sum=0
    t=n
    while t>0:
        d=t%10
        sum+=d**n_len
        t//=10
    if n==sum:
        print("Armstrong number",sum)
    else:
        print("not Armstrong number",sum)'''

for _ in range(int(input())):
    n=int(input())
    t1=n
    i=0
    while t1>0:
        t1=t1//10
        i+=1
    t2=n
    sum=0
    while t2>0:
        d=t2%10
        sum+=d**i
        t2=t2//10
    if n==sum:
       print("Armstrong number",sum)
    else:
       print("not Armstrong number",sum)
   
    

