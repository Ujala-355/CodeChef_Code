d=int(input())
c=0
b=0
while d!=0:
    i=d%2
    b+=(i*10**c)
    d=(d//2)
    c+=1
print(b)
