class vehicle():
    def start(self):
        print("vehicle start")
        
class car(vehicle):
    def start(self):
        print("car start")
        
audi=car()
audi.start()