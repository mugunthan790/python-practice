class calculator():
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def operation(self):
        oper=input("Enter the operation:")
        if oper=="add":
            print("Addition:",self.a+self.b )
        elif oper=="sub":
            print("subtraction:",self.a-self.b)
        elif oper=="mul":
            print("multiplication:",self.a*self.b)
        elif oper=="div":
            print("division:",self.a/self.b)
        else:
            print("invalid option !")
        
print()
fun=calculator(10,20)
fun.operation()
print()
fun2=calculator(2,10)
fun2.operation()
