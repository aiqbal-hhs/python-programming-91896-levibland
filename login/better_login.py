# TODO: implement account creation

import hashlib

# Username and password combinations
# stored as sha256 hash for added security
login_details = {
  "Jhon": "507f8ded27f5b96fa908bd9bba10996849b4d189c235b117df15c3e73624623e",
}

# List of all usernames in existence
usernames = ['Jhon']

def title_screen():
  print('##############################################')
  print('############   Choose an action   ############')
  print('##############################################')
  print('Login\n')
  print('Create Account\n')

  selection = input('> ')
  formatted = selection.lower().strip()

  if formatted == ("login"):
    login()
  elif formatted == ("create account"):
    create_account()
  else:
    print("Error: Invalid selection (01)\n")
    exit(1)

def login():
  global usernames
  global login_details

  print("Username:")
  username = input("> ")

  print('Password:')
  password = input("> ")

  while username not in usernames:
    print("Error: Invalid username (02)\n")
    print("Username:")
    username = input("> ")

    print("Password:")
    password = input("> ")

  encoded = password.encode()
  digest = hashlib.sha256(encoded)

  if digest.hexdigest() == login_details[username]:
    print("Logged in, press any key to exit.")
    wait = input("> ")
    exit(0)
  else:
    print("Error: Password incorrect (03)")
  
title_screen()
