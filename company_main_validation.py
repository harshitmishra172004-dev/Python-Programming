# Company Email Validation

email = input("Enter company email address: ")

# Split email into username and domain
parts = email.split("@")

if len(parts) == 2:
    username = parts[0]
    domain = parts[1]

    # Verify company domain
    if domain.endswith("dev.com"):
        print("Valid Company Email")

        # Extract department code
        dept_code = username[:3].upper()

        print("Username:", username)
        print("Department Code:", dept_code)
        print("Domain:", domain)
    else:
        print("Invalid Company Domain")
else:
    print("Invalid Email Format")