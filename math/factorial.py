# factorial() finds the factorial fo a number given by the user
def factorial(num):
    factorial = 1
    # if a negative number is passed to the function
    if num < 0:
        print("Factorials do not exist for negative numbers.\n")
    # if 0  is apssed to the function
    elif num == 0:
        print("0! is = 1")
    # if anything other than 0 or a negative number is passed to the function
    else:
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.\n")

# call the factorial() function, passing 3 as an argument
factorial(3)
