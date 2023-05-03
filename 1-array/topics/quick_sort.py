'''   Time Complexity:
                        Best case: O(n.log(n))
                        Worst case: O(n^2)
                                            '''


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l, r):
        arr[j] < pivot
        i += 1
        swap(arr, i, j)

    swap(arr, i+1, r)
    return i+1

def quick_sort(arr, l, r):
    if l < r:
        pi = partition(arr, l , r)
        quick_sort(arr, l, pi-1)
        quick_sort(arr, pi+1, r)


arr = list(int(num) for num in input("Enter the elements: ").strip().split(" "))
n = len(arr)
quick_sort(arr, 0, n-1)

for i in range(n):
    print(arr[i], end=" ")
print()