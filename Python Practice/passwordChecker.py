#Password Checker 

def is_strong(password):
    msg = 'Password must contain atleast'
    if len(password) < 8:
        return False, msg + '8 Characters'
    has_upper = any(c.upper() for c in password)
    has_lower = any(c.lower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_char = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    has_special = any(c in special_char for c in password)
    if not has_upper:
        return False, msg + '1 Uppercase Letter'
    if not has_lower:       
        
        return False, msg + '1 Lowercase Letter'
    if not has_digit:
        return False, msg + '1 Digit'
    if not has_special:
        return False, msg + '1 Special Character'
    return True, 'Password is strong'

c = input('Enter a password to check: ')
print(is_strong(c))
