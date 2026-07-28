terms = int(input("How many terms of the Fibonacci series do you want? "))
n1, n2 = 0, 1
count = 0
if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(f"Fibonacci series up to {terms} term:")
    print(n1)
else:
    print("Fibonacci series:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1