# declare a new class called person
class Person:
    def __init__(self, age, fname, sname, job):
          self.age = age
          self.fname = fname
          self.sname = sname
          self.job = job
    
    def greet(greeting):
          # use fstring to print greeting
          print(f"{greeting}\n")
 

# declare a new instance of the Person() class called tyrone
tyrone = Person(40, "Tyrone", "Smith", "carpenter")

# print tyrones attributes
print(tyrone.age)
print(tyrone.fname)
print(tyrone.sname)
print(tyrone.job)

# intentionally spelt wrong
tyrone.greet("Hello jonh cena")
