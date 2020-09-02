def factorial(num):
    factorial = 1
    if num < 0:
        print("Factorials do not exist for negative numbers.\n")
    elif num == 0:
        print("0! is = 1")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.\n")
