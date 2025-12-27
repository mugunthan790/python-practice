class person():
    def __init__(self,name):
        self.name=name
        
class student(person):
    def __init__(self,name,mark):
        super().__init__(name)
        self.grade=mark
    def display(self):
        print(f"Name:{self.name}")
        print(f"Grade:{self.grade}")
        
ram=student("jone",10)
ram.display()