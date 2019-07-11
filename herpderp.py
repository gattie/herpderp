def herpderp(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "HerpDerp"
        return "Herp"
    if is_multiple(value, 5):
        return "Derp"
    return str(value)

def is_multiple(value, multiple):
    return (value % multiple) == 0

if __name__ == '__main__':
    import sys
    try:
        my_val = int(sys.argv[1])
        for i in range(1, my_val):
            print(herpderp(i), end=" ")
    except ValueError:
        raise ValueError("Provided value is not an integer")
