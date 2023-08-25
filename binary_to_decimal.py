binary=int(input())
b=0
decimal=0
while binary!=0:
    i=binary%10
    decimal+=(i*2**b)
    binary=(binary//10)
    b+=1
print(decimal)
