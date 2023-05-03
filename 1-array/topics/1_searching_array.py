''' Searching in 1-array '''

def linear_search(arr, n, k):
    for i in arr:
        if k == i:
            return arr.index(k)
    return -1

n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements: ").strip().split())[:n]

k = int(input("Enter the key to find: "))
print(linear_search(arr, n, k))