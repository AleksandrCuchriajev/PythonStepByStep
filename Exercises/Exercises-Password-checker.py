username = input("What is your username? : ").capitalize()
password = input("What is your password? : ")
password_length = len(password)
secret_password = "*" * password_length
print(f"Hi {username}, your password {secret_password} has {password_length} characters.")