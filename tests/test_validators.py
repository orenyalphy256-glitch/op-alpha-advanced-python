# test_validators.py

# Import the validation function
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validators import is_valid_phone

def test_valid():
    assert is_valid_phone("0712345678")
    assert not is_valid_phone("")