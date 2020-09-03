# Guess my number program
ANSWER = 12356874
tries = 3

while tries > 0:
    uin = int(input("What is the number?\n"))
    if uin == ANSWER:
        print(f"Your answer, {uin}, is the correct answer.\n")
        tries = 0
    else:
        print(f"Your answer, {uin}, is not the corrrect answer.\n")
        tries -= 1
        print(f"You have {tries} tries left.\n")
