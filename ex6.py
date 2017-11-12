
# int variable and formatted string variable
types_of_people = 10
x = f"there are {types_of_people} types of people."

# three string variables, 1 of them formatted
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print x and y string variables
print(x)
print(y)

# print them again with y in single quotes
print(f"I said: {x}")
print(f"I also said: '{y}'")

# hilarious is boolean variable joke_evaluation is string with {} for formatting
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# print joke_evaluation with formatting
print(joke_evaluation.format(hilarious))

# w and e string variables
w = "this is the left side of ..."
e = "a string with a right side."

# print w and e
print(w + e)

# strings with strings inside on are lines 9, 16, 17
# lines 4 and 21 are formatted but their int and boolean values
# the + in line 31 chains the two strings together making it longer
