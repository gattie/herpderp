def fizzbuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)

def is_multiple(value, multiple):
    return (value % multiple) == 0

if __name__ == '__main__':
    import sys
    try:
        my_val = int(sys.argv[1])
        print(fizzbuzz(my_val), end=" ")
    except ValueError:
        print("Provided value is not an integer")
