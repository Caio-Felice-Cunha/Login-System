from controller import ControllerLogin, ControllerRegister

while True:
    print("========== [MENU] ==========")
    decision =      int(input('Type 1 to register\n'
                          'Type 2 to Login\n'
                          'Type 3 to exit\n'))
    
    if decision == 1:
        name = input("Type your name: ")
        email = input("Type your email: ")
        password = input("Type your password: ")
        
        result = ControllerRegister.register(name, email, password)

        if result == 2:
            print("Name size is not valid")

        elif result == 3:
            print("Email size is bigger than 200 characteres")

        elif result == 4:
            print("Password size not valid")

        elif result == 5:
            print("Email already registered")

        elif result == 6:
            print("System internal error")

        elif result == 1: 
            print("Successfully registered")
    
    elif decision == 2:

        email = input("Type your email: ")
        password = input("Type your password: ")

        result = ControllerLogin.login(email, password)

        if not result:
            print("Email or password incorrect")

        else:
            print(result)

    else:
        break