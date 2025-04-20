# IMPORTANT NOTE: This script is for educational purposes only. Do not use it in production without proper security measures.
# This script generates a hashed password using bcrypt.
# It is important to use a strong hashing algorithm for password storage.
# bcrypt is a popular library for hashing passwords in Python.
# Use bcrypt for better security. It is specifically designed for password hashing and includes salting to protect against rainbow table attacks.
# Avoid hashlib for passwords unless you add your own salting mechanism, as it is not purpose-built for secure password storage.
# Make sure to install the bcrypt library if you haven't already:
# pip install bcrypt

import bcrypt

# Password to be hashed
password = "charyulu123"

# Generate salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)

# Print the hashed password
print("Hashed Password:", hashed_password.decode())