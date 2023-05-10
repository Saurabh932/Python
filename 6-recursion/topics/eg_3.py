''' Question : Find the factorial of a number; '''

def factorial(n):
    if n == 0:
        return 1

    pre_fact = factorial(n-1)
    return n * pre_fact

n = int(input("Enter the number: "))
print("The Factorial is: ", factorial(n))