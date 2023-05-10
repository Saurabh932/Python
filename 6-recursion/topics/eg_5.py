''' Question : Check if the 1-array is in sorted order;  '''


def sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return True

    return arr[0] < arr[1] and sort(arr[1:])


arr = list(int(num) for num in input("Enter the element: ").strip().split(" "))
print("The condition is ", sort(arr))
