import hashlib

name = input("Your name: ")

encoded = name.encode()

digest = hashlib.sha256(encoded)

print(f"Here is your name passed through the sha256 hash function: {digest.hexdigest()}")
