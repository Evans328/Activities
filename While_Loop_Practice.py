nameList =["Fred", "Bob", "Tony", "John"]

success = False

while success == False:
    name = input ("Enter your name ")

    if name in nameList:
        print("Hi ", name, " Welcome back!")

        password = input("Password: ")
        if password == "savvycoder":
            print("Welcome in!")
            success = True
        else: 
            print("Try again stupid!")

    else:
        nameList.append(name)
        print("Nice to meet you! ", name)    
print(nameList)