def fizzbuzz(value):
    if is_multiple(value, 3):
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)

def is_multiple(value, multiple):
    return (value % multiple) == 0