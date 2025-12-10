a=int(input("Enter english mark:"))
b=int(input("Enter tamil mark:"))
c=int(input("Enter maths mark:"))
d=int(input("Enter science mark:"))
e=int(input("Enter social science:"))
add=a+b+c+d+e
avg=add/5
print(f"Total marks={add}")
print(f"Average={avg}")
if(avg<35):
    print("ADDITIONAL CLASS IS REQUIRED !")
else:
    print("GOOD")