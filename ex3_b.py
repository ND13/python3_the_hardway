# This is study drill number 3 for exercise 3
# "Find something you need to calculate and write a new .py file that does it."
# I've chosen to calculate the first problem from Project Euler

sum = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        sum = sum + num
print(sum)
