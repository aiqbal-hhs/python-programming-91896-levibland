def getFizzBuzz(mults, *args):
	for i in range(*args):
		output = ''
		for mult in mults:
			if i % mult == 0:
				output += mults[mult]
		if output == '':
			output = i
		print(output)

mults = {3: 'Fizz', 5: 'Buzz'}
getFizzBuzz(mults, 1, 101) 
