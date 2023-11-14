
#Generate Password: Use a combination of random characters to
#generate a password of the specified length.
#Display the Password: Print the generated password on the screen

import secrets
import string

#function for random password base on complexity
def generate_password(length, complexity):
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    character_set = []

    if complexity == 'low' :
        character_set += upper_case + lower_case
        
    elif complexity == 'medium':
        character_set += string.ascii_letters + digits 
        
    elif complexity == 'strong':
        character_set += string.ascii_letters + digits + special_characters 

    password = ''.join(secrets.choice(character_set) for _ in range(length))
    
    return password

    
length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity (low/medium/strong): ").lower()

while complexity not in ['low', 'medium', 'strong']:
    
    print("Invalid complexity. Please enter low, medium, or strong.")
    complexity = input("Enter the complexity (low/medium/strong): ").lower()

password = generate_password(length, complexity)
print(f"Generated Password: {password}")
6


