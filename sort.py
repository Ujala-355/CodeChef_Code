'''l=list(map(int,input().split()))
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]<l[j]:
            a=l[i]
            l[i]=l[j]
            l[j]=a
        j+=1
    i+=1
print(l)'''

for _  in range(int(input())):
    a=list(map(int,input().split()))
    n=len(a)
    string_loop_position=0
    while string_loop_position<=n-2:
        i=string_loop_position
        min=i
        while i<=n-1:
            if a[i]<a[min]:
                min=i
            i+=1 
        temp=a[string_loop_position]
        a[string_loop_position]=a[min]
        a[min]=temp
        string_loop_position+=1
    print(a)
            
