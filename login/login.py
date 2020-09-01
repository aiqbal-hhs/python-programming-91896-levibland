# Login program

username = "bruh"
password = "cena"
ticker = True
uticker = True
pticker = True

for i in range(3):
    while ticker:
        if uticker == True:
            uinput = input("Username: ")
            if uinput.lower().strip() != ("bruh"):
                print("Incorrect username.\n")
                break
            else:
                print("Username correct!")
                uticker = False
                break
        
        pinput = input("Password: ")
        if pticker == True: 
            if pinput.lower().strip() != ("cena"):
                print("Incorrect password")
                break
            else:
                print(f"Login detail correct for username: {uinput}.\n")
                pticker = False
                break
