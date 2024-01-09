import hashlib
def hashedpass(password):
    password_bytes = password.encode('utf-8')
    password_hash = hashlib.sha256(password_bytes)
    return password_hash.hexdigest()

password = input("input your password")
hashed = hashedpass(password)
print(hashed)