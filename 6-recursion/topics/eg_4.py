''' Find Fibonacci of nth number: '''

def fib(n):
    if n == 0 or n == 1:
        return n
    first_pre = fib(n-1)
    second_pre = fib(n-2)
    return first_pre + second_pre


n = int(input("Enter the number: "))
print("The fibonacci is: ", fib(n))