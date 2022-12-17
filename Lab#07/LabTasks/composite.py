from abc import ABC, abstractmethod 
 
class BaseDepartment(ABC):     
    @abstractmethod     
    def __init__(self, num_of_employees):         
        pass 
 
    @abstractmethod     
    def print_department(self):         
        pass 
 
class Accounting(BaseDepartment):     
    def __init__(self, num_of_employees):         
        self.num_of_employees = num_of_employees 
 
    def print_department(self):         
        print(f"Accounting employees: {self.num_of_employees}") 
 
class Development(BaseDepartment):     
    def __init__(self, num_of_employees):         
        self.num_of_employees = num_of_employees 
 
    def print_department(self):         
        print(f"Development employees: {self.num_of_employees}")  
 
class Management(BaseDepartment):     
    def __init__(self, num_of_employees):         
        self.num_of_employees = num_of_employees         
        self.childs = [] 
 
    def print_department(self):         
        print(f"Management base employees: {self.num_of_employees}")         
        total_emp_count = self.num_of_employees         
        for child in self.childs:             
            total_emp_count += child.num_of_employees             
            child.print_department()         
            print(f'Total employees: {total_emp_count}') 
 
    def add_child_dept(self, dept):         
        self.childs.append(dept) 
    def delete_child_dept(self,dept):
        self.child.pop(dept)
#  
acc_dept = Accounting(200) 
dev_dept = Development(500) 
 
management_dept = Management(50) 
management_dept.add_child_dept(acc_dept) 
management_dept.add_child_dept(dev_dept) 
 
# print dept
management_dept.print_department() 
