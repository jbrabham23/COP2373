# Jadyn Brabham
# Chapter 6, Assignment 6
# This program will have a user enter their phone number, social security
# number, and zip code. Then the program will validate the input values
# using regular expressions and then display the valid input values.

import re

# Function to validate a phone number.
def validate_phone_number(phone):
    # Regular expression for valid phone number formats (XXX-XXX-XXXX or
    # (XXX) XXX-XXXX)
    pattern = r'(\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}'
    if re.fullmatch(pattern, phone):
        return True
    return False

# Function to validate Social Security Number(SSN)
def validate_ssn(ssn):
    # Regular expression for valid SSN format (XXX-XX-XXXX)
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.fullmatch(pattern, ssn):
        return True
    return False

# Function to validate zip code
def validate_zip_code(zip_code):
    # Regular expression for valid zip code format (XXXXX or XXXXX-XXXX)
    pattern = r'^\d{5}(-\d{4})?$'
    if re.fullmatch(pattern, zip_code):
        return True
    return False

# Main function to get user input and display validation results.
def main():
    # Ask the user for their phone number, social security number, and zip code.
    phone_number = input("Enter your phone number "
                         "(XXX-XXX-XXXX or (XXX) XXX-XXXX): ")
    ssn = input("Enter your Social Security Number "
                "(XXX-XX-XXXX): ")
    zip_code = input("Enter your Zip Code (XXXXX or "
                     "XXXXX-XXXX): ")

    # Validate the inputs
    is_phone_valid  = validate_phone_number(phone_number)
    is_ssn_valid = validate_ssn(ssn)
    is_zip_valid = validate_zip_code(zip_code)

    # Display results
    if is_phone_valid:
        print("Phone number is valid.")
    else:
        print("Phone number is not valid.")

    if is_ssn_valid:
        print("Social Security Number is valid.")
    else:
        print("Social Security Number is not valid.")

    if is_zip_valid:
        print("Zip Code is valid.")
    else:
        print("Zip Code is not valid.")

# Call the main function
if __name__ == "__main__":
    main()
