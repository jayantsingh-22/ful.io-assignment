import re


def is_valid_contact_number(contact_number):
    pattern = r'^(\+?1-?)?(\d{3}|\(\d{3}\)|\d{3})[-. ]?\d{3}[-. ]?\d{4}$'

    # Use re.match() to check if the input matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False


contact_number = input("Enter a contact number: ")

if is_valid_contact_number(contact_number):
    print(f"{contact_number} is a valid contact number.")
else:
    print(f"{contact_number} is not a valid contact number.")
