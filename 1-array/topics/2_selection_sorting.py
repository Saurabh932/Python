''' Selection Sorting :  Find the minimum element in unsorted 1-array and swap it with elements at the biginning.  '''

def selection_sorting(arr, n):
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                # temp = arr[j]
                # arr[j] = arr[i]
                # arr[i] = temp
                arr[j], arr[i] = arr[i], arr[j] # Another way of writing swaping

    return arr


n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements; ").strip().split())

print(selection_sorting(arr, n))