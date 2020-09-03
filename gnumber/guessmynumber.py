# Guess my number program
ANSWER = 12356874   # Change value of ANSWER to change the answer to the guess my number challenge
tries = 3

while tries > 0:
    uin = int(input("What is the number?\n"))   # uin stands for user input
    if uin == ANSWER:
        print(f"Your answer, {uin}, is the correct answer.\n") # NOTE TO READERS: f"{uin}" is the same as "{}".format(uin), fstrings are a more modern way of
                                                               # formatting print statements and strings in general.
        tries = 0
    else:
        print(f"Your answer, {uin}, is not the corrrect answer.\n")
        tries -= 1
        print(f"You have {tries} tries left.\n")
