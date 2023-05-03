''' In wave sort the output is in wave form where 1st element is higher than second and third is also higher than 2nd. '''


def wave_sort(arr):
    n = len(arr)

    for i in range(1, n-1, 2):
        if arr[i] > arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

        if arr[i] > arr[i+1] and i <= n-2:
            arr[i], arr[i+1] = arr[i+1], arr[i]


arr = list(int(num) for num in input("Enter the elements: ").strip().split(" "))
wave_sort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")