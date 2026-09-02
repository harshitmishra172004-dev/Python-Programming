#WAP to find the fibonacci series using recursion and take a user input.
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range (num):
    print(fibo(i), end =" ")  