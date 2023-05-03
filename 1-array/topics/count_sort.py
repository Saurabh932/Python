'''   We are -
              1. Find the count of every distinct element in the 1-array.
              2. Calculate the position of each elements in the sorted 1-array.

              '''


def count_sort(array):
    size = len(array)
    output = [0] * size

    # Initialize count 1-array
    count = [0] * 10

    # Store the count of each elements in count 1-array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original 1-array in count 1-array
    # place the elements in output 1-array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original 1-array
    for i in range(0, size):
        array[i] = output[i]


# n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements: ").strip().split(" "))
count_sort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
