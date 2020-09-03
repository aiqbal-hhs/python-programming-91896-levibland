# a script that prints fibonacci numbers up to the limit set by the limit parameter
def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

limit = int(input("Choose limit: "))
for i in fibonacci(limit):
  print(i)
