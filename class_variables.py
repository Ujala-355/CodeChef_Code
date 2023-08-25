class Employee:
    increment=1.5
    no_of_emp=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_emp+=1 
    def increase(self):
        self.salary=int(self.salary*self.increment)
 ujala=Employee("ujala","saini",4000)
 neeraj=Employee("neeraj","das",4000)
 ujala.increase()
 print(ujala.fname)
