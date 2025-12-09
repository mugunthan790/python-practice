a = int(input("A: "))
b = int(input("B: "))
opp = input("Enter the operation (add,sub,mul,div): ")

if opp == "add":
    print(a + b)
elif opp == "sub":
    print(a - b)
elif opp == "mul":
    print(a * b)
elif opp == "div":
    print(f"{a/b:.2f}")
else:
    print("Invalid option")