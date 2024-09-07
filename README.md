# Guest List and Seating Arrangement Script

## Overview

This script is designed to manage a guest list from a file and organize seating arrangements for an event. It reads a list of guests from a file, processes their information, and assigns them to tables based on predefined seating arrangements. The script also filters guests based on their age and outputs a list of those who are 21 and older.

## Learning Goals

1. **File Handling in Python:**
   - Learn how to read from and process files using Python.
   - Understand how to handle file data line by line.

2. **Generators and Yield:**
   - Understand the use of generators to handle streaming data.
   - Learn how to use the `yield` keyword to produce values lazily and handle dynamic input.

3. **Data Structures:**
   - Practice working with dictionaries to store and manage data.
   - Learn to filter and manipulate lists based on conditions.

4. **Custom Iterators:**
   - Create custom iterators for managing complex data flows.
   - Combine multiple generators to produce a unified result.

5. **Dynamic Data Handling:**
   - Learn to dynamically modify a list and handle real-time data updates.

## Features

- **Read Guest List:** Read guest data from a file, which includes names and ages.
- **Add New Guests:** Allow adding new guests to the list dynamically.
- **Filter by Age:** Generate a list of guests who are 21 years old or older.
- **Seating Arrangements:** Assign guests to tables with predefined food options.

## Requirements

- Python 3.x

## Setup

1. **Prepare the Guest List File:**

   Create a file named `guest_list.txt` in the same directory as the script. The file should contain guest information in the following format:

   ```
   Name1,Age1
   Name2,Age2
   ...
   ```

   Example content:

   ```
   Alice,30
   Bob,22
   Charlie,19
   ```

2. **Script Usage:**

   Ensure you have Python 3 installed. Run the script using the command:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of the Python script file.

## How It Works

1. **Reading the Guest List:**

   The `read_guestlist` function reads the guest list from the `guest_list.txt` file. It processes each line, extracting names and ages, and stores this information in the `guests` dictionary. The function is a generator that allows dynamic updates to the guest list.

2. **Adding New Guests:**

   The script demonstrates how to add a new guest by sending a new entry to the generator.

3. **Filtering by Age:**

   After processing the initial list, the script generates and prints a list of guests who are 21 years old or older.

4. **Seating Arrangements:**

   - **Table Generators:** Three separate generator functions (`table1`, `table2`, and `table3`) provide seating arrangements for different tables with different food options.
   - **Combined Tables:** The `combinedtables` function combines the seating arrangements from all tables into a single generator.
   - **Final Assignment:** The `final` function pairs each guest with a seating arrangement, which is then printed.

## Example Output

```plaintext
Guestlist:
----------
Alice 30
Bob 22
Charlie 19
Jane 35

Guests drinking age 21 and over list:
------------------------
['Alice', 'Bob', 'Jane']

Full seating list:
-----------------
('Alice', ('Table number: 1', 'Chicken', 1))
('Bob', ('Table number: 1', 'Chicken', 2))
...
```

## Notes

- The script assumes the guest list file is correctly formatted and present in the same directory.
- Adjust the table and food options as needed by modifying the `table1`, `table2`, and `table3` functions.

## License

Feel free to modify and use it for your purposes.
