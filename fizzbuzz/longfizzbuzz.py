# An easily alterable version of fizzbuzz
def FizzBuzz(mults, *args):	# The *args parameter is for setting the amount of times to loop through the fizzbuzz code
				# The mults parameter is for specifying the numbers that will result in Fizz or Buzz
	for i in range(*args):
		output = ''
		for mult in mults:
			if i % mult == 0:  # Check if the if i is divisible by the numbers in the mults dictionary
				output += mults[mult]
		if output == '':   # If i is not divisible by the number specified in mults, set the output string to i
			output = i
		print(output)	# Print the result

mults = {3: 'Fizz', 5: 'Buzz'}	# Assign 3 to Fizz and 5 to Buzz
FizzBuzz(mults, 1, 101)  # Call FizzBuzz function passing the mults dictionary, and the parameters for the range function
