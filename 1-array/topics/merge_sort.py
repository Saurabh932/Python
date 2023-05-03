'''   Time Complexity:
                        Best case: O(n.log(n))
                        Worst case: O(n.log(n))
                                                 '''

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    # Temporary arrays
    arr_1 = [0] * (n1)
    arr_2 = [0] * (n2)

    for i in range(n1):  # storing elements from l to mid
        arr_1[i] = arr[l + i]

    for j in range(n2):  # storing elements from mid to r
        arr_2[j] = arr[mid + 1 + j]

    # Iterating through arr_1 and arr_2
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if arr_1[i] < arr_2[j]:
            arr[k] = arr_1[i]
            k += 1
            i += 1

        else:
            arr[k] = arr_2[j]
            k += 1
            j += 1

    #     If i and j pointer of arr_1 and arr_2 didn't traverse completely then we again traverse it.
    while i < n1:
        arr[k] = arr_1[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = arr_2[j]
        k += 1
        j += 1


def merge_sort(arr, l, r):
    if l < r:
        mid = int((l + r) / 2)
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)

        merge(arr, l, mid, r)


arr = list(int(num) for num in input("Enter the elements: ").strip().split(" "))
n = len(arr)
merge_sort(arr, 0, n-1)

for i in range(n):
    print(arr[i], end=" ")
print()
