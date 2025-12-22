class teacher():
    def __init__(self,name,reg):
        self.tname=name
        self.regno=reg
    def dis(self):
        print(f"Name of the teacher is : {self.tname}")
        print(f"Name of the teacher is : {self.regno}")
print()       
t1=teacher("kavitha","24it29")
t1.dis()
print()
t2=teacher("jainthi","24it69")
t2.dis()
    