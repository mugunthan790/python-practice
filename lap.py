class laptop():
    def __init__(self):
        self.ram=""
        self.process=""
    def display(self):
        print(f"Ram={self.ram}")
        print(f"Processer={self.process}")
        
hp=laptop()
hp.ram="16gb"
hp.process="i5"

dell=laptop()
dell.ram="16gb"
dell.process="i7"

hp.display()
print()
dell.display()
    