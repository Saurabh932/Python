''' Bubble sorting:  Reapeatedly swap two adjecent elements if they are in wrong order.   '''

def bubble_sort(arr, n):
    counter = 1
    while counter < n+1:
        for i in range(len(arr) - counter):
            if arr[i] > arr[i+1]:
                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[i+1] = temp
                arr[i+1], arr[i] = arr[i], arr[i+1]

        counter+=1
    return arr

n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements: ").strip().split(", "))

print(bubble_sort(arr,n))