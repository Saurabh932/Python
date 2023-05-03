''' Printing a Sub-Array:'''

# def subarray(arr, n):
#     sub_array = [[]]
#     for i in range(0, n+1):
#         for j in range(i):
#             sub_array.append(arr[j:i])
#     return sub_array

# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the number: ").strip().split())[:n]
# print("The sub-1-array is: ", subarray(arr,n), end="\n")



'''Question 1:   Maximum Subarray  -- Given an integer 1-array nums,
                 find the subarray which has the largest sum and return its sum.'''
#
# def max_subarray(arr, n):
#     sub_array = []
#     sum_array = 0
#     for i in range(0, len(arr)):
#         for j in range(i, len(arr)):
#             sum_array += arr[j]
#             sub_array.append(sum_array)
#
#     return max(sub_array)
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split())
#
# print(max_subarray(arr, n))



''' Question 2:   Search an element in a sorted and rotated Array  
              --- Given a sorted and rotated 1-array arr[] of size N and a key, the task is to find the key in the 1-array.
                Note: Find the element in O(logN) time and assume that all the elements are distinct.'''

def position(arr, n, key):
    s = 0
    e = len(arr)-1

    while s <= e:
        mid = int((s+e)/2)
        if arr[mid] == key:
            return mid

        # Checking if the left part is sorted:
        if arr[s] < arr[mid]:
            if key >= arr[s] and key < arr[mid]:
                e = mid-1
            else:
                s = mid+1

        # Checking if the right part is sorted:
        else:
            if key > arr[mid] and key < arr[e]:
                s = mid+1
            else:
                e = mid-1

n = int(input("Enter the size: "))
arr = list(int(num) for num in input("Enter the elements in sorted order and rotate it: ").strip().split(", "))
key = int(input("Enter the key: "))

print("The index is: ", position(arr,n,key))




