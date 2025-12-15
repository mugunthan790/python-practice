def add():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("ADDITION =", a + b)

def sub():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("SUBTRACTION =", a - b)

def mul():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("MULTIPLICATION =", a * b)

def div():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("DIVISION =", a / b)

ope = input("Enter operation (add / sub / mul / div): ")

if ope == "add":
    add()
elif ope == "sub":
    sub()
elif ope == "mul":
    mul()
elif ope == "div":
    div()
else:
    print("Invalid operation")

    
