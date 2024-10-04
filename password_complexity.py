import re

def assess_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

   
    if strength_score == 5:
        return "Strong password! Your password meets all the recommended criteria."
    elif strength_score == 4:
        return "Good password, but adding a special character will make it even stronger."
    elif strength_score == 3:
        return "Fair password, but try using a mix of uppercase, numbers, and special characters to strengthen it."
    elif strength_score == 2:
        return "Weak password, consider using at least 8 characters, with a mix of letters, numbers, and special characters."
    else:
        return "Very weak password! It is recommended to have a longer password with uppercase, lowercase, numbers, and special characters."

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
