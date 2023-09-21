import pandas as pd

# Read data from the Excel file named "harmonics.xlsx"
data = pd.read_excel("harmonics.xlsx")

# Function to check if a value is within a range
def is_within_range(value, min_value, max_value):
    return min_value <= value <= max_value

# User inputs
user_xb = float(input("Enter a value for 'xb': "))
user_ac = float(input("Enter a value for 'ac': "))
user_bd = float(input("Enter a value for 'bd': "))
user_xd = float(input("Enter a value for 'xd': "))

# Test values
# user_xb = float((0.886))
# user_ac = float((0.382))
# user_bd = float((2.618))
# user_xd = float((1.618))

# Print user inputs
print(f"User inputs: 'xb': {user_xb}, 'ac': {user_ac}, 'bd': {user_bd}, 'xd': {user_xd}")

# Initialize a list to store matched names
matched_names = []

# Iterate through the rows in the Excel data
for index, row in data.iterrows():
    if (
        is_within_range(user_xb, row["xb_min"], row["xb_max"])
        and is_within_range(user_ac, row["ac_min"], row["ac_max"])
        and is_within_range(user_bd, row["bd_min"], row["bd_max"])
        and is_within_range(user_xd, row["xd_min"], row["xd_max"])
    ):
        matched_names.append(row["name"])  # Remember the matched name

# Determine the message to print based on the number of matches
num_matches = len(matched_names)
if num_matches == 1:
    match_message = "Harmonic found"
elif num_matches > 1:
    match_message = "More than one Harmonic found!"

# Print the message
print(match_message)

# Print the matched names with ordinals (if more than one match)
if num_matches > 1:
    for i, name in enumerate(matched_names, start=1):
        ordinal = "st" if i == 1 else "nd" if i == 2 else "rd" if i == 3 else "th"
        print(f"{i}{ordinal} match: {name}")
elif num_matches == 1:
    print(f"Name: {matched_names[0]}")
else:
    print("No matches found")