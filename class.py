class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoy the beach")

ramesh=goa()
suresh=goa()
ramesh.name="Ramesh"
suresh.name="Suresh"
ramesh.drink="yes"
suresh.drink="no"
print(ramesh.name)
print(F"Drink:{ramesh.drink}")
print(suresh.name)
print(f"Drink:{ramesh.drink}")
ramesh.party()
suresh.party()
ramesh.beach()
suresh.beach()

