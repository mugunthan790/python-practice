class granpa():
    def phone(self):
        print("granpa's phone")
        
class dad(granpa):
    def money(self):
        print("dad's money")
        
class son(dad):
    def laptop(self):
        print("son's laptop")
        
mani=son()
mani.laptop()
mani.money()
mani.phone()


