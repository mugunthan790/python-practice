class a():
    def __init__(self):
        print("class A")
    
        
class b(a):
    def __init__(self):
        super().__init__()
        print("class B")
        
class c(b,a):
    def __init__(self):
        super().__init__()
        print("class C")
        
obj1=c()
    