for i in range(int(input())):
   s=input()
   l=s.split("/")
   print(l)
   l[0]=int(l[0])
   l[1]=int(l[1])
   if l[0]>12:
       print("DD/MM/YYYY")
   elif l[1]>12:
       print('MM/DD/YYYY')
   elif l[0]<=12  and l[1]<=12:
       print("BOTH")
