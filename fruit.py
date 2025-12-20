class fruit():
    def __init__(self,col):
        self.colour=col
    def display(self):
        print(self.colour)

apple=fruit("red")

apple.display()