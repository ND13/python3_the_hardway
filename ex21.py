def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def main():
    print("Let's do some math with just functions!")
    print("-------------------------------------------------------------------------")
    
    age = add(20, 7)
    height = subtract(74, 4)
    weight = multiply(85, 2)
    iq = divide(50, 2)

    print("-------------------------------------------------------------------------")
    print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

    print("-------------------------------------------------------------------------")
    print("Here is a puzzle")

    print("-------------------------------------------------------------------------")
    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

    print("That becomes: ", what, "can you do it by hand?")

if __name__ == '__main__':
    main()
