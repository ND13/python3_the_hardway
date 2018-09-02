# *args here lets use a variable length for arguments passed to function
def print_two(*args):
    # unpacking arguments
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# different than print_two function this only accepts two arguments being passed to it
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# single argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# no arguments
def print_none():
    print("I got nothin'.")

print_two("Nick", "Davis")
print_two_again("Nick", "Davis")
print_one("First!")
print_none()
