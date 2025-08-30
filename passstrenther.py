import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (!@#$%^&* etc.).")

    if strength == 5:
        return "Strong password!", []
    elif strength >= 3:
        return "Moderate password.", remarks
    else:
        return "Weak password.", remarks

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result, feedback = check_password_strength(pwd)
    print(result)
    for remark in feedback:
        print("-", remark)