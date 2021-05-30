
def validate_age(age : int):
    if age < 0:
        raise ValueError("Age can not be less than 0")
