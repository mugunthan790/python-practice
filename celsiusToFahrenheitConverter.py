class temp():
    def getdata(self):
        self.s=int(input("Enter Celsius Tempracture:"))
    def cal(self):
        self.f=(self.s*9/5)+32
    def display(self):
        print(f"the fahrenhite of {self.s} celsius is : {self.f}")
find=temp()
find.getdata()
find.cal()
find.display()