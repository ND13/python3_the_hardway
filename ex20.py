from sys import argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

def main():
    script, input_file = argv

    current_file = open(input_file)

    print("First let's pring the whole file:\n")
    print_all(current_file)

    print("Now let's rewind, kind of like a tape.")
    rewind(current_file)

    print("Let's print three lines: ")

    # Did this in a loop instead of separate function calls
    current_line = 0
    for i in range(3):
        current_line += 1
        print_a_line(current_line, current_file)

    current_file.close()

if __name__ == '__main__':
    main()
