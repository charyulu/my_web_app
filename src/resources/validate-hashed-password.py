# Check hashed password against user input
user_input = "your_password_here"  # Password entered by the user
if bcrypt.checkpw(user_input.encode(), hashed_password):
    print("Password matches!")
else:
    print("Invalid password.")