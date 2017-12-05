'''
Code for exercise 16 study drill 2
Use the read() to read the file you create with
the ex16.py script.
'''

from sys import argv

script, filename = argv

print("To read the file hit RETURN or else use CTRL-C to exit.")
input("> ")

target = open(filename, 'r')

print("Here are the contents of your file: ")
print(target.read())

print("Now closing file...")
target.close()
