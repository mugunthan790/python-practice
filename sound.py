class animal():
    def sound(self):
        print("Amimal sound")
        
class dog(animal):
    def sound(self):
        print("dog sound")
        
class bird(animal):
    def sound(self):
        print("bird sound")
        
crow=bird()
crow.sound()
