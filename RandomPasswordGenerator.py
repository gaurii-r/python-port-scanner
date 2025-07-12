import random
import string

pass_len = 8

# Character set: letters (uppercase + lowercase), digits, and punctuation
charValues = string.ascii_letters + string.digits + string.punctuation

# Empty string to store the password
password = ""

# Loop to generate password
for i in range(pass_len):
    password += random.choice(charValues)
    
# Print the generated password
print("Your random password is:", password)
