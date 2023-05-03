''' Question 1.  Search in Rotated Sorted Array
                There is an integer 1-array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting 1-array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the 1-array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
                                                                        '''
#
# def search_index(arr, n, target):
#     start = 0
#     end = n
#     while start <= end:
#         mid = int((start+end)/2)
#         if arr[mid] == target:
#             return mid
#
#         # Checking left side:
#         if arr[start] < arr[mid]:
#             if target >= arr[start] and target < arr[mid]:
#                 end = mid-1
#             else:
#                 start = mid+1
#
#         # Checking right side:
#         else:
#             if target > arr[mid] and target < arr[e]:
#                 start = mid+1
#             else:
#                 end = mid-1
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(","))[:n]
# target = int(input("Enter the target: "))
#
# print("The position of the target is: ", search_index(arr, n, target))


'''Question 2:  Find Minimum in Rotated Sorted Array
                Suppose an 1-array of length n sorted in ascending order is rotated between 1 and n times. 
                zFor example, the 1-array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an 1-array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the 1-array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated 1-array nums of unique elements, return the minimum element of this 1-array.'''

#
# def minium_element(arr, n):
#     min_ele = arr[0]
#     for i in range(n):
#         if arr[i] < min_ele:
#             min_ele = arr[i]
#     return min_ele
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(","))
#
# print("The minimum element: ", minium_element(arr,n))


'''Question 3: Product of Array Except Self'''
#
# def product(arr, n):
#     prod = []
#     for i in range(0,n):
#         prod_current = 1
#         for j in range(0,n):
#             if i == j:
#                 continue
#
#             prod_current = prod_current * arr[j]
#         prod.append(prod_current)
#
#     return prod
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(", "))[:n]
#
# print("The product is: ", product(arr, n))



''' Question 4: Kth smallest element
                Given an 1-array arr[] and an integer K where K is smaller than size of 1-array, 
                the task is to find the Kth smallest element in the given 1-array. 
                It is given that all 1-array elements are distinct.'''

# def smallest_kth_element(arr, n, k):
#     arr.sort()
#     return arr[k-1]
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(" "))[:n]
# k = int(input("Enter the Kth smallest elements: "))
#
# print(smallest_kth_element(arr, n, k))


