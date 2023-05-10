''' Question: Print the order of n in:
              1> Increasing order
              2> Decreasing order'''

def inc(n):
    if n == 0:
        return
    inc(n-1)
    print(n, end=" ")

def dec(n):
    if n == 0:
        return
    print(n, end=" ")
    dec(n-1)

n = int(input("Enter the number: "))
inc(n) 
dec(n)