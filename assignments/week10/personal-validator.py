"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age_str = input("Enter your age: ")
phone = input("Enter your phone number: ")

name_valid = all(part.isalpha() for part in name.split())
if name_valid:
    name_result = "Valid (contains only letters and spaces)"
else:
    name_result = "Invalid (should contain only letters and spaces)"

if age_str.isdigit():
    age = int(age_str)
    if 18 <= age <= 65:
        age_result = f"Valid ({age} years old)"
        if 18 <= age <= 30:
            age_group = "Young Adult (18-30)"
        elif 31 <= age <= 50:
            age_group = "Adult (31-50)"
        else:
            age_group = "Senior Adult (51-65)"
    else:
        age_result = "Invalid (age not in 18-65 range)"
        age_group = "N/A"
else:
    age_result = "Invalid (age must be a number)"
    age_group = "N/A"

phone_valid = phone.isdigit() and len(phone) == 10
if phone_valid:
    phone_result = "Valid (10-digit number)"
    formatted_phone = "+91-" + phone
else:
    phone_result = "Invalid (must be exactly 10 digits)"
    formatted_phone = "N/A"

print("\nValidation Results:")
print("Name: %s" % name_result)
print("Age: %s" % age_result)
print("Phone: %s" % phone_result)

print("\nFormatted Information:")
print("Name: {}".format(name.upper()))
print("Age Group: {}".format(age_group))
print("Phone: {}".format(formatted_phone))