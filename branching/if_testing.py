# testing if statements

inp = input()

if inp == "hello":
  print("Correct")
elif inp == "yello":
  print("yello")
else:
  print("Your an idiot")
  

inp = int(input())

if inp == 1:
  print("Correct")
elif inp == 2:
  print("2")
else:
  print("Your an idiot")
  

inp = int(input())

if inp >= 5 or inp <= 20:
  print("In bounds")
elif inp == 12:
  print("Corrct")
else:
  print("Your an idiot")
