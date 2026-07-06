username = input("Enter username:")
password = input("Enter password:")
role = input("Enter your role:")

correctUsername = "techskillhub.dev"
correctPassword = "123@pipl"

if(username == correctUsername and password == correctPassword):
    print("Login successfully.")
    print("Welcome to The TechSkillHub.~")
    if(role == "admin"):
        print("Welcome Admin")
    else:
        print("Welcome user.!")
else:
    print("Error:Incorrect username and password.!")
