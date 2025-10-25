# validators.py
# Import necessary modules
import re

# Regular expression for validating a phone contact number
PHONE_RE = re.compile(r'^\+?\d[\d\s\-]{6,}$')

# Function to validate phone numbers
def is_valid_phone(phone):
    return bool(PHONE_RE.match(phone))