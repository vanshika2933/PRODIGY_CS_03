import re

def check_password_strength(password):
    # Criteria for password strength
    length_regex = r'.{8,}'
    uppercase_regex = r'[A-Z]'
    lowercase_regex = r'[a-z]'
    digit_regex = r'[0-9]'
    special_char_regex = r'[!@#$%^&*()_+{}\[\]:;\"\'<>,.?/\\~-]'
    
    # Score for each criterion
    score = 0
    
    # Check length
    if re.match(length_regex, password):
        score += 1
        
    # Check uppercase letters
    if re.search(uppercase_regex, password):
        score += 1
        
    # Check lowercase letters
    if re.search(lowercase_regex, password):
        score += 1
        
    # Check digits
    if re.search(digit_regex, password):
        score += 1
        
    # Check special characters
    if re.search(special_char_regex, password):
        score += 1
    
    return score

def password_strength_feedback(score):
    if score == 5:
        return "Strong password"
    elif score >= 3:
        return "Moderate password"
    elif score >= 1:
        return "Weak password"
    else:
        return "Very weak password"

# Example usage
password = input("Enter your password: ")
strength_score = check_password_strength(password)
feedback = password_strength_feedback(strength_score)
print("Password strength:", feedback)