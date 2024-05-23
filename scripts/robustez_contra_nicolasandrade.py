def verify_password_strength(password):

    sufficient_length = len(password) >= 8


    contains_uppercase = any(c.isupper() for c in password)


    contains_lowercase = any(c.islower() for c in password)


    contains_digits = any(c.isdigit() for c in password)


    contains_special_characters = any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)


    score = sufficient_length + contains_uppercase + contains_lowercase + contains_digits + contains_special_characters


    if score >= 5:
        print("The password is strong!")
    else:
        print("The password is not strong enough.")


    print("Password score:", score)


password = input("Enter your password: ")


verify_password_strength(password)
