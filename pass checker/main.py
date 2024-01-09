import re
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return False
    return True


password = input("enter your password")

valid = validate_password(password)

if valid:
    print("valid pass")
else:
    print("req not true in pass")