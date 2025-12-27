class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
class manager(employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.departmet=dep
    def display(self):
         print(f"name:{self.name}")
         print(f"Salary:{self.salary}")
         print(f"Department:{self.departmet}")
        
ram=manager("ram","20,000","packing")
ram.display()

        
        