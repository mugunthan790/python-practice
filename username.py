name="vijay"
password="1234"
username=input("Enter the User name:")
u_password=input("Enter the Password:")
def valid():
   if(name==username and password==u_password):
     return True
   else:
       return False
a=valid()
print(a)
