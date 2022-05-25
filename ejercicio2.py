#Create a program than request password a user and after confirm it

password = str(input("Please into your password: "))
confirm_password =str(input("Please confirm your password: "))

if (password == confirm_password):
    print("Verification is Sucessfully")
else:
    print("Sorry, your passwords isn't equals")