def check_age(age):
    if age < 18:
        raise Exception("not valid")
    else:
        return("valid")
        
print(check_age(25))