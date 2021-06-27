import hashlib

jhon_encoded = "jhon".encode()
hash = hashlib.sha256(jhon_encoded)

print(f'jhon hashed: {hash.hexdigest()}')
