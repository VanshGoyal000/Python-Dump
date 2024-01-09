import random 
import string

def generate_password(lenght):
    all_characters= string.ascii_letters + string.digits + string.punctuation
    password =''
    for i in range(lenght):
        password += random.choice(all_characters)
    return password

lenght = int(input("lenght of password"))
password = generate_password(lenght)
print(password)