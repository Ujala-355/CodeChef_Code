for _ in range(int(input())):
    b=int(input())
    if b>0 and b<=10:
        print("Lower Double")
    elif b>=10 and b<=15:
        print("Lower Single")
    elif b>15 and b<=25:
        print("Upper Double")
    else:
        print("Upper Single")
            
