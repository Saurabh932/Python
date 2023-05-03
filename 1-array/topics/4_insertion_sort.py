''' Insertion sort: Insert an elements from an unsorted 1-array to its correct position in the sorted 1-array.  '''

def insertion_sort(arr, n):

    for i in range(1, len(arr)):
        current = arr[i]
        previous = i-1

        while arr[previous] > current and previous >= 0:
            arr[previous+1] = arr[previous]
            previous -= 1

        arr[previous+1] = current

    return arr

n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements: ").strip().split(", "))

print("The sorted 1-array is: ", insertion_sort(arr, n))