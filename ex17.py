from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}")

in_data = open(from_file).read()
out_file = open(to_file, 'w')
out_file.write(in_data)

print(f"Copying file completed: {to_file} size: {len(in_data)}")

out_file.close()
