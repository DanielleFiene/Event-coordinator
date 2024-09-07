# Function to read and process the guest list from a file
def read_guestlist(file_name):
    # Open the file with the given file name
    with open(file_name) as f:
        # Read all lines from the file and split them into a list
        entries = f.read().splitlines()

    # While there are still entries in the list
    while entries:
        # Remove the last line from the list and split it by commas
        line_data = entries.pop().split(',')
        # Extract the name and age from the line data
        name, age = line_data[0], int(line_data[1])
        # Add the name and age to the guests dictionary
        guests[name] = age
        # Yield the name and age for further processing
        entry = yield name, age
        # If an entry is sent to the generator, add it back to the list
        if entry is not None:
            entries.append(entry)

# Initialize an empty dictionary to hold guest information
guests = {}

# Print the header for the guest list
print('Guestlist:')
print('----------')

# Create a generator object for reading the guest list
guestlist = read_guestlist('guest_list.txt')

# Iterate over the first 10 items from the guest list generator
for i in range(10):
    print(next(guestlist))

# Send a new guest entry to the generator and print the result
print(guestlist.send("Jane,35"))

# Iterate over the remaining items from the guest list generator and print them
for guest in guestlist:
    print(guest)

print()

# Print the header for the drinking age list
print('Guests drinking age 21 and over list:')
print('-------------------------------------')

# Filter and list guests who are 21 or older
age_21_over = [x for x in guests if guests[x] >= 21]
print(age_21_over)

print()

# Print the header for the full seating list
print("Full seating list:")
print("------------------")

# Define a generator function for table 1
def table_1():
    table = 'Table number: ' + str(1)
    food = 'Chicken'
    # Generate seating for table 1
    for i in range(1, 6):
        seat = i
        yield table, food, seat

# Define a generator function for table 2
def table_2():
    table = 'Table number: ' + str(2)
    food = 'Steak'
    # Generate seating for table 2
    for i in range(1, 6):
        seat = i
        yield table, food, seat

# Define a generator function for table 3
def table_3():
    table = 'Table number: ' + str(3)
    food = 'Fish'
    # Generate seating for table 3
    for i in range(1, 6):
        seat = i
        yield table, food, seat

# Combine the generators for all tables
def combined_tables():
    yield from table_1()
    yield from table_2()
    yield from table_3()

# Create a generator object for combined tables
full_seating = combined_tables()

# Define a final function to pair guests with seating
def final(guests, full_seating):
    # Iterate over each guest
    for i in guests:
        # Get the next seating arrangement from the full seating generator
        seating = next(full_seating)
        # Yield a tuple of the guest and their seating arrangement
        yield (i, seating)

# Create a generator object for final guest seating
fin = final(guests, full_seating)

# Print the final guest seating arrangements
for i in fin:
    print(i)
