def fizzbuzz(value):
    if (value % 3) == 0:
        return "Fizz"
    if value == 5:
        return "Buzz"
    return str(value)