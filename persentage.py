per=int(input("enter the persentage:"))
if(per>=70 and per<=100):
    print("you are eligible")
    name=input("Enter your name:")
    department=input("enter your department:")
    print(f"your name is : {name}")
    print(f"your department is : {department}")
else:
    print("you are not eligible !")
    