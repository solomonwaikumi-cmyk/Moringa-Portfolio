# Final Script: Password Strength Checker

import re

# List of commonly used weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "111111", "iloveyou", "admin", "letmein",
    "welcome", "monkey", "dragon", "master", "sunshine",
    "princess", "password123", "123123", "654321", "superman"
]


# Task 2: Check password length (minimum 8 characters recommended)
def check_length(password):
    """Checks if the password meets the minimum length requirement."""
    if len(password) >= 8:
        return True, "- Length: OK (8+ characters)"
    else:
        return False, f"- Length: Too short ({len(password)} characters). Use at least 8 characters."


# Task 2: Check for uppercase and lowercase letters
def check_case(password):
    """Checks if the password contains both uppercase and lowercase letters."""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if has_upper and has_lower:
        return True, "- Case: OK (contains uppercase and lowercase letters)"
    elif not has_upper and not has_lower:
        return False, "- Case: Missing uppercase and lowercase letters. Add both for a stronger password."
    elif not has_upper:
        return False, "- Case: Missing uppercase letters. Add at least one uppercase letter."
    else:
        return False, "- Case: Missing lowercase letters. Add at least one lowercase letter."


# Task 2: Check for numbers and special characters
def check_numbers_special(password):
    """Checks if the password contains at least one number and one special character."""
    has_number = any(char.isdigit() for char in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\\/;'`~]", password))

    if has_number and has_special:
        return True, "- Numbers & Special Characters: OK"
    elif not has_number and not has_special:
        return False, "- Numbers & Special Characters: Missing both. Add at least one number and one special character (e.g. !, @, #)."
    elif not has_number:
        return False, "- Numbers: Missing. Add at least one number (0-9)."
    else:
        return False, "- Special Characters: Missing. Add at least one special character (e.g. !, @, #, $)."


# Task 2: Check against a list of common passwords
def check_common_passwords(password):
    """Checks if the password is a commonly used weak password."""
    if password.lower() in COMMON_PASSWORDS:
        return False, "- Common Password: This is a very common password. Choose something unique and harder to guess."
    else:
        return True, "- Common Password Check: OK (not a known common password)"


# Task 4: Updated check_password_strength function
def check_password_strength(password):
    """Evaluates the password using all checks and returns feedback."""
    results = []

    # Call each function and collect feedback
    length_ok, length_msg = check_length(password)
    case_ok, case_msg = check_case(password)
    num_spec_ok, num_spec_msg = check_numbers_special(password)
    common_ok, common_msg = check_common_passwords(password)

    results.append(length_msg)
    results.append(case_msg)
    results.append(num_spec_msg)
    results.append(common_msg)

    # Determine overall strength
    if all([length_ok, case_ok, num_spec_ok, common_ok]):
        return "Strong password! Good job."
    else:
        return "Weak password. Recommendations:\n" + "\n".join(results)


# Task 3: User input with while loop validation
print("=== Password Strength Checker ===")

while True:
    password = input("\nEnter a password to check (or type 'quit' to exit): ")

    if password.lower() == "quit":
        print("Exiting password checker. Goodbye!")
        break

    if not password:
        print("No password entered. Please enter a password to check.")
        continue

    # Task 5: Call the function and display results
    result = check_password_strength(password)
    print("\nResult:", result)