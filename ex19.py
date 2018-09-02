def total_cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You will need {cheese_count} blocks of cheese!")
    print(f"You will need {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket!\n")

def get_cheese_and_crackers(num_of_guests):
    # created a dictionary to handle multiple return values
    d = dict()
    d['blocks_of_cheese'] = num_of_guests * 2
    d['boxes_of_crackers'] = num_of_guests

    return d

def guests():
    num_guests =  int(input("Enter the number of guests: "))

    return num_guests

print("You're throwing a party each guest will need 1 box of crackers and 2 blocks of cheese.")
num_guests = guests()
cheese_crackers = get_cheese_and_crackers(num_guests)
total_cheese_and_crackers(cheese_crackers['blocks_of_cheese'], cheese_crackers['boxes_of_crackers'])
