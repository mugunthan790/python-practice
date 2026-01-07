try:
 class pnf():
    def getdata(self):
        self.num=int(input("Enter the number:"))
        
    def process(self):
        if self.num>0:
            print(f"{self.num} is Positive Number")
        elif self.num==0:
            print(f"{self.num} is Zero")
        else:
            print(f"{self.num} is Negetive Number")
            
 find=pnf()
 find.getdata()
 find.process()
except Exception as e:
    print(f"invalid option {e}")
finally:
    print("exit")