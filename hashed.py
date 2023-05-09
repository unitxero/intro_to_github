password = str(input("Enter Password: "))

hashed_id = hashlib.sha512(password.encode()).hexdigest()

print(hashed_id)
