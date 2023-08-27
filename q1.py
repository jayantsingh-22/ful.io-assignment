# Regex module
import re

# Function for matching
def validate_contact_number(contact_number):
    # Regex for valid contact numbers
    pattern = r'^(\+?)(\+?\d{1,2}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    
    # Checking if the contact number matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False

# Test cases
contact_numbers = {
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
}

# Iterating and checking if numbers are valid or not
for number in contact_numbers:
    if validate_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
