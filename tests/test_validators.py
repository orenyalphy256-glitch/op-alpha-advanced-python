# test_validators.py

# Import the validation function
from contact_manager.validators import is_valid_phone

def test_valid_numbers():
    assert is_valid_phone("+25401234567")
    assert is_valid_phone("0712345678")
    assert is_valid_phone("abc123") #Assuming alphanumeric is valid