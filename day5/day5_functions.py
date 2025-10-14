def check_age(age):
    if age >= 18:
        return "You are an adult"
    else:
        return "You are a minor"
    
message = check_age(12)
print(message)