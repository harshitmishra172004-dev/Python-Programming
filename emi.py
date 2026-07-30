#Check loan eligibility based on income,credit score and existing EMI using nested if-else statements.
income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
if income >= 50000:
    if credit_score >= 700:
        existing_emi = float(input("Enter your existing EMI: "))
        if existing_emi <= (income * 0.4):
            print("You are eligible for the loan.")
        else:
            print("You are not eligible for the loan due to high existing EMI.")
    else:
        print("You are not eligible for the loan due to low credit score.")
else:
    print("You are not eligible for the loan due to low income.")