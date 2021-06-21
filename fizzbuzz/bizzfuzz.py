  # A two line bizzfuzz program

for i in range(1, 101):
	# This is cancer
	print("Bizz"*(i%3<1)+(i%5<1)*"Fuzz" or i)
