
def choices():
    print("Please choose what you would like to do.")
    user_choice = int(input("For Sigining Up Type 1 and For Logging in Type 2: "))
    if user_choice == 1:
       return signin()
    elif user_choice == 2:
       return login()
    else:
       raise TypeError

def signin():
    print("Please Provide your basic details to sign up")
    name = str(input("Username: "))
    password = str(input("Password: "))
    f = open("Assignment.py",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +name + " " + password
    f.write(info)

def login():
    print("Please Provide your basic details to login in")
    Usr_name = str(input("Username: "))
    password = str(input("Password: "))
    f = open("Assignment.py",'r')
    info = f.read()
    info = info.split()
    if Usr_name in info:
        index = info.index(Usr_name) + 1
        usr_password = info[index]
        if usr_password == "ishaqRDJ66":
            return "Welcome Back, " + Usr_name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."

print(choices())
