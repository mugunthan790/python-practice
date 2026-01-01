class si():
    def getdata(self):
        self.pa=int(input("Enter the Principal Amount:"))
        self.ri=int(input("Enter the Rate of intrest:"))
        self.t=int(input("Enter the Time period:"))
        
    def process(self):
        self.simpleintrest=self.pa*self.ri*self.t/100
        print(f"Simple Intrest= {self.simpleintrest}")
        
cal=si()
cal.getdata()
cal.process()