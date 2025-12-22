class fruit():
    def __init__(self,colour):
        self.colour=colour
    def display(self):
        print(self.colour)

apple=fruit("red")

apple.display()