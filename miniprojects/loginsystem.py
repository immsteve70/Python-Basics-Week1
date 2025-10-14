username = "immsteve"
password = "123456"

while True:
    print("Welcome to THE USUAL LOGIN SYSTEM :)")

    actionuser = input("Enter your username: ")
    actionpass = input("Enter your password: ")

    if actionuser == username:
        if actionpass == password:
            print("Logged In successfully!")
        else:
            print("Incorrect Password!")
    else:
        print("User not found!")
    
