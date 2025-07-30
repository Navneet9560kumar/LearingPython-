import string 
import random
import getpass 

def check_password_strength(password):
      issues = []
      if len(password)<88:
              issues.append("Too short (minimum 8 characters) ")
      if not any(c.islower() for c in password):
                  issues.append("Must contain at least one lowercase letter")
      if not any(c.isupper() for c in password):
                    issues.append("Must contain at least one uppercase letter")
      if not any(c.isdigit() for c in password):
                    issues.append("Must contain at least one digit")
      if not any(c in string.punctuation for c in password):
                    issues.append("Must contain at least one special character")
      return issues

def generate_strong_password(length=12):
        chars = string.ascii_letters + string.digits + string.punctuation

        return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter your password: ")
issues = check_password_strength(password)

if not issues:
        print("Password is strong") 

else:
        print("Password is weak:")
        for issue in issues:
            print(f"- {issue}")

        if input("Would you like to generate a strong password? (yes/no) ").strip().lower() == "yes":
            new_password = generate_strong_password()
            print(f"Generated strong password: {new_password}")
            if input("Do you want to use this password? (yes/no) ").strip().lower() == "yes":
                password = new_password
                print("Password updated successfully.")
            else:
                print("Keeping the original password.")