salary=int(input("Enter the salary amount:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age>=21):
    print("you are eligible")
    lone=int(input("Enter the loan amount :"))
    if(lone<=50000):
        print(f"you are eligible for loan {lone}")
    else:
        print(" the maximum loan amount is 50,000")
else:
    print("you are not eligible for loan !")