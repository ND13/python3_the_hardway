# pass filename as second argument to this program

# Importing argv from the sys module
from sys import argv
# arguments
script, filename = argv

# store the opened file in variable txt
txt = open(argv[1])
# print string, print reading of txt file
print(f"Here's your file {filename}")
print(txt.read())

# close file
txt.close()
