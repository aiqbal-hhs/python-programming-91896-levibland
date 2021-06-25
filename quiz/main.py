import random
import qna
import sys

'''
    This file includes the logic for this math quiz.
'''

# @function quiz()
# @param qna this parameter is for passing the questions and answers
# @param params this parameter is for passing the parameters for the quiz
# @dev the quiz() function is the main quiz function that handles all the logic surrounding questions and answers
def quiz(qna, params):
    # @param params formatted as so: [quiz_length, difficulty, randomness]
    
    attempts = 1
    correct_answers = 0
    score = 0

    # randomize order of questions
    # randomness passed as 3rd item in the list returned by the setquizparams() function
    if params[2] == True:
        random.shuffle(qna)

    elif params[2] == False:
        pass

    else:
        error('\nSomething went wrong.\n')
        die()

    # main quiz loop
    for i in range(params[0]):
        print(f'{qna[i][0]}\n')
        guess = input('> ')
        while attempts <= params[1]:
            if guess.lower().strip() in qna[i][1]:
                print(f'\nYour answer, {guess}, is the correct answer.\n')
                attempts = params[1]
                correct_answers += 1
                score += 2
                break

            elif guess.lower().strip() == ("quit"):
                die()

            elif guess.lower().strip() not in qna[i][1]:
                print(f'\nYour answer, {guess}, is not the correct answer.\nTry again.\n')
                print(f'{qna[i][0]}\n')
                guess = input('> ')
                attempts += 1
                score += 0.1

            else:
                error('\nSomething went wrong.\n')
                die()

        attempts = 0

    # after exiting the loop, print how many questions they got correct
    print(f'\nYou have answered {correct_answers} questions correctly.\n')


# @function setquizparams()
# @dev the setquizparams() function allows the user to set the parameters of the quiz
# @return quiz_length this variable stores the number of questions in the quiz, it is set by the user, it cannot be <= 0 and > the total number of questions
# @return difficulty this variable stores the number of tries the user gets for each question, it is set by the user, it can not be > 1
# @return randomness this variable is used to determine whether the questions in the quiz should be randomized, it is set by the user, it can either be True or False
def setquizparams():

    # following variables are used in the process to check if the users inputs are an integer
    length_is_int = False
    difficulty_is_int = False
    
    print('\nSet the parameters for the quiz game.\n')
    print('\nSet the length of the quiz.\n')

    # user enters how many questions they want to answer
    quiz_length = input('> ')

    # allow the user to quit
    if quiz_length.lower().strip() == ("quit"):
        print("Quitting...\n")
        die()

    # check if quiz_length is an integer, if it is: continue, if not: try again
    while length_is_int != True:
        try:
            quiz_length = int(quiz_length)
            while quiz_length > len(qna.qna)or quiz_length <= 0:
                
                # check which error to throw
                if quiz_length > len(qna.qna):
                    error(f"\nValue entered is greater than the length of the quiz\nPlease enter a value less than or equal to {len(qna.qna)}")

                elif quiz_length <= 0:
                    error("\nValue entered for quiz_length is <= 0, please enter an integer > 0.\n")
                    
                quiz_length = input("> ")

                # allow the user to quit
                if quiz_length.lower().strip() == ("quit"):
                    print("Quitting...\n")
                    die()
                    
                quiz_length = int(quiz_length)

            # if no errors are thrown, exit the loop    
            length_is_int = True

        except ValueError:
            error('\nIncorrect value entered for quiz_length, please enter an integer\n')
            print('\nSet the length of the quiz\n')
            quiz_length = input('> ')
            
            # allow the user to quit
            if quiz_length.lower().strip() == ("quit"):
                print("Quitting...\n")
                die()

    print('\nSet the number of tries for each question you get\n')
    difficulty = input('> ')

    # allow user to quit
    if difficulty.lower().strip() == ("quit"):
        print("Quitting...\n")
        die()

    while difficulty_is_int != True:
        try:
            difficulty = int(difficulty)
            while difficulty <= 0:
                print("You can not have zero or negative tries for each question, please enter a positive integer.\n")
                difficulty = input("> ")

                # allow user to quit
                if difficulty.lower().strip() == ("quit"):
                    print("Quitting...\n")
                    die()
                    
                difficulty = int(difficulty)

            # if no errors are thrown, exit the loop
            difficulty_is_int = True

        except ValueError:
            error('\nIncorrect value entered for number of tries, please enter an integer\n')
            print('\nSet the number of tries for each question you get\n')
            difficulty = input('> ')
            
            # allow user to quit
            if difficulty.lower().strip() == ("quit"):
                print("Quitting...\n")
                die()

    print('\nDo you want your quiz to be randomized?\n')
    randomness = input('> ')

    # allow user to quit
    if randomness.lower().strip() == ("quit"):
        print("Quitting...\n")
        die()

    # while randomness is not a correct input, prompt user to enter a valid input
    while randomness.lower().strip() not in ['yes', 'y', 'n', 'no']:
        error('\nYour input for randomness is not valid, please answer \'yes\', \'y\', \'no\' or \'n\'\n')
        randomness = input('> ')
        
        # allow user to quit
        if randomness.lower().strip() == ("quit"):
            print("Quitting...\n")
            die()

    if randomness.lower().strip() == ('yes') or randomness.lower().strip() == ('y'):
        randomness = True

    elif randomness.lower().strip() == ('no') or randomness.lower().strip() == ('n'):
        randomness = False

    else:
        error('Something has gone horribly wrong.\n')
        die()


    print(f'\nYou have chosen the length of the quiz to be {quiz_length}.\n\nYou have chosen to have {difficulty} attempts at each question.\n')
    print('\nIf you want to quit during the quiz simply type \'quit\' and the game will automatically exit.\n')

    # return all the values in a list
    return [quiz_length, difficulty, randomness]

# @function die()
# @dev the die() function quits the game and throws an error 
def die():
    error("Exiting now.\n")
    sys.exit()

# @function error()
# @param message used for passing an error message to the error() function
# @dev the error() fucntion notifies the user of an error 
def error(message):
    print(message)

# @function greeter()
# @dev the greeter() function is the initial options screen if the quiz, a user may enter 'play', 'help', or 'quit', and the quiz script will react accordingly.
# @option 'play' the 'play' command allows players to start the quiz
# @option 'help' the 'help' command prints all of the commands available to the user
# @option 'quit' the 'quit' command quits the game, killing the program
def greeter():
    print('\nWelcome to Math quiz 2020 (c)\n')
    print('\nPlay\nHelp\nQuit\n')
    option = input('> ')

    # check if 'option' is a valid input
    if option.lower().strip() == ('play'):
        print('\nYou have chosen to play the math quiz.\n')
        quiz(qna.qna, setquizparams())

    elif option.lower().strip() == ('help'):
        print('\n commands: \'help\' for help, \'play\' to play, \'quit\' to quit.\n')

    elif option.lower().strip() == ('quit'):
        print('\nQuitting...\n')
        die()

    # while 'option' is not a valid input, prompt the user to enter a vlid command 
    while option not in ['play', 'help', 'quit']:
        print('\nNot a valid command, type "help" for help.\n')
        option = input('> ')

        if option.lower().strip() == ('play'):
            print('\nYou have chosen to play the math quiz.\n')
            quiz(qna.qna, setquizparams())

        elif option.lower().strip() == ('help'):
            print('\n commands: \'help\' for help, \'play\' to play, \'quit\' to quit.\n')

        elif option.lower().strip() == ('quit'):
            print('\nQuitting...\n')
            die()

# call the greeter() function which starts the quiz, after the quiz has finished call the die() function quitting the game
greeter()
die()
