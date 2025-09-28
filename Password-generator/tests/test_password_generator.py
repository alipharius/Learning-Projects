import string
from password_generator import generate_password, contains_upper, contains_symbols

def test_contains_upper_true():
    assert contains_upper("Abc") is True

def test_contains_upper_false():
    assert contains_upper("abc") is False

def test_contains_symbols_true():
    assert contains_symbols("a!b") is True

def test_contains_symbols_false():
    assert contains_symbols("abc") is False

def test_generate_password_length():
    pwd = generate_password(length=12, symbols=True, uppercase=True)
    assert len(pwd) == 12

def test_generate_password_types():
    pwd = generate_password(length=100, symbols=True, uppercase=True)
    
    # Check if it contains at least one uppercase
    has_upper = any(c in string.ascii_uppercase for c in pwd)
    assert has_upper is True
    
    # Check if it contains at least one symbol
    has_symbol = any(c in string.punctuation for c in pwd)
    assert has_symbol is True

def test_generate_password_without_symbols_uppercase():
    pwd = generate_password(length=50, symbols=False, uppercase=False)
    
    # Should have no uppercase
    has_upper = any(c in string.ascii_uppercase for c in pwd)
    assert has_upper is False
    
    # Should have no symbols
    has_symbol = any(c in string.punctuation for c in pwd)
    assert has_symbol is False
