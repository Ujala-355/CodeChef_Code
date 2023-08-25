for _ in range(int(input())):
    n=int(input())
    S=c1=c2=c3=c4=c5=c6=c7=c8=0
    for i in range(n):
        x,y=map(int,input().split())
        if x==1:
            if y>c1:
                c1=y
        if x==2:
            if y>c2:
                c2=y
        if x==3:
            if y>c3:
                c3=y 
        if x==4:
            if y>c4:
                c4=y 
        if x==5:
            if y>c5:
                c5=y 
        if x==6:
            if y>c6:
                c6=y
        if x==7:
            if y>c7:
                c7=y 
        if x==8:
            if y>c8: 
                c8=y 
    s=c1+c2+c3+c4+c5+c6+c7+c8  
    print(s)
                
                
                
        
            
            
            
            
            
            
            
    
