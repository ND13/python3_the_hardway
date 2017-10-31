# This is study drill number 3 for exercise 3
# "Find something you need to calculate and write a new .py file that does it."
# I've chosen to calculate the first problem from Project Euler

# This loops through all values from 1-1000 and gets the sum of all numbers
# that are evenly divided by 3 or 5. A good start but there is definitely
# more efficient ways to do this, maybe I will come back in the future.
sum = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        sum = sum + num
print(sum)
