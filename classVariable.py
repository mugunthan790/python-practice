class phone():
    chargerType="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"price: {self.price}")
        print(f"charger Type: {self.chargerType}")    
apple=phone("i phone 17","1,00,000")
apple.display()
        
        