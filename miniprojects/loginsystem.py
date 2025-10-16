username = "immsteve"
password = "123456"

attempts = 0

while True:
        attempts += 1
        print("Welcome to THE USUAL LOGIN SYSTEM :)")

        actionuser = input("Enter your username: ")
        actionpass = input("Enter your password: ")

        success1 = actionuser == username
        success2 = actionpass == password

        if success1:
            if success2:
                print("Logged In successfully!")
                break
            else:
                print("Incorrect Password!")
        else:
            print("User not found!")
        
        if attempts == 3:
             print("3 Wrong Tries")
             break
        else:
             continue