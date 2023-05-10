''' Question;  Find the first and the last occuring number in an 1-array: '''


# In first occur, we first check wheather the key is present on first index or not. if present we print the index and if not then move
#   forward to check.
def first_occur(arr, n, i, key):
    if i == n:
        return -1

    if arr[i] == key:
        return i

    return first_occur(arr, n, i+1, key)

# In last occur, we first move forward till last element in the 1-array. the from last we check wheather arr[i] is equal to key or not.

def last_occur(arr, n, i, key):
    if i == n:
        return -1

    rest_array = last_occur(arr, n, i+1, key)
    if rest_array != -1:
        return rest_array

    if arr[i] == key:
        return i

    return -1

n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements: ").strip().split(" "))[:n]
key = int(input("Enter the element to found: "))
print(first_occur(arr, n, 0, key))
print(last_occur(arr, n, 0, key))