for i in range(int(input())):
    s=input()
    c=0
    maxvowels=0
    for j in (s):
        if j in "aeiou":
            c+=1
            maxvowels=max(maxvowels,c)
        else: 
            c=0
    if maxvowels>2:
        print("Happy")
    else:
        print("Sad")
