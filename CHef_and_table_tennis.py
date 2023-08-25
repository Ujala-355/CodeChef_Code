for i in range(int(input())):
    s=input()
    l=list(s)
    c1=0
    c2=0
    for j in l:
        if j=="1":
            c1+=1
        else:
            c2+=1
    if c1>=c2:
        print("WIN")
    else:
        print("LOSE")
