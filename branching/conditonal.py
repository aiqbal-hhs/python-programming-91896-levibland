upper = str(input("String: "))
lower = str(input("String: "))
number = int(input("Integer: "))

if upper.lower() == lower.lower():
    print("Identical")
if number == upper:
    print("Identical")
else:
    print("Type difference")
