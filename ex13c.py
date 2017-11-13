# Study Drill #3

from sys import argv

script, first = argv

arg_2 = input("Oops, I forgot what was your second argument again? ")

if arg_2 == argv[1]:
    print(f"Ah yes that's right! It was {argv[1]}")
else:
    print(f"Hmm are you sure? I thought it was {argv[1]}...")
