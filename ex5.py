name = 'Ronin'
age = 26 # not a lie
height = 70 # inches
weight = 168 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# converting pounds and inches to kilograms and centimeters
height_cm = round(float(height) * 2.54)
weight_kg = round(float(weight) / 2.20)

# printing an empty line to separate sections
print("")

print(f"Let's talk about {name} but this time using kilograms and centimeters.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
