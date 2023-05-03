''' Question 1: Two Sum
                Given an 1-array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
                You may assume that each input would have exactly one solution, and you may not use the same element twice.
            You can return the answer in any order.'''

# def two_sum(arr, n, target):
#     index = []
#     for i in range(0, n-1):
#         for j in range(i+1,n):
#             addition = arr[i] + arr[j]
#
#             if addition == target:
#                 new_list = i,j
#                 index.append(new_list)
#     return index
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(","))
# target = int(input("Enter the target: "))
# #
# print("The 2sum are: ", two_sum(arr,n,target))


''' Question 2: 3Sum
                Given an integer 1-array nums, return all the triplets [nums[i], nums[j], nums[k]]
                such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
            Notice that the solution set must not contain duplicate triplets.
'''

# def three_sum(arr, n):
#     triplet = []
#
#     for i in range(0, n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#
#                 if i != j and i != k and j != k and arr[i] + arr[j] + arr[k] == 0:
#                     ele = arr[i], arr[j], arr[k]
#                     triplet.append(ele)
#
#         return triplet
#     return 0
#
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elemets: ").strip().split(","))[:n]
#
# print("The 3sum are: ",three_sum(arr,n))



''' Question 3:  Given Sum Pair
                Find if there is a pair with a given sum in the rotated sorted Array
                Given an 1-array arr[] of distinct elements size N that is sorted and then around an unknown point, 
                the task is to check if the 1-array has a pair with a given sum X.'''

# def sum_pair(arr, n, target):
#     subarray = []
#     sum = 0
#     for i in range(n+1):
#         for j in range(i):
#             subarray.append(arr[j:i])
#
#     for i in range(len(subarray)):
#         for j in range(i,len(subarray)):
#             sum += j
#             if sum == target:
#                 return True
#             else:
#                 return False
#
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(","))[:n]
# target = int(input("Enter the target: "))
# print(sum_pair(arr, n, target))



''' Question 4:  Find minimum number of merge operations to make an 1-array palindrome.
                Given an 1-array of positive integers. We need to make the given 1-array a ‘Palindrome’. 
                The only allowed operation is”merging” (of two adjacent elements). 
                Merging two adjacent elements means replacing them with their sum. 
                The task is to find the minimum number of merge operations required to make the given 1-array a ‘Palindrome’.
                    
            Logic:  The basic logic behind this question is that we just have to count the number of time the mergering operation
                    or addition of non-equal elements have done.'''

#
# def merge_operation(arr):
#     n = len(arr)
#     i,j = 0, n-1
#     ans = 0
#
#     while i<=j:
#         if arr[i] == arr[j]:
#             i += 1
#             j -= 1
#
#         elif arr[i] > arr[j]:
#             j -= 1
#             arr[j] += arr[j-1]
#             ans += 1
#
#         else:
#             i += 1
#             arr[i] += arr[i+1]
#             ans += 1
#
#     return ans
#
# arr = list(int(num) for num in input("Enter the elements; ").strip().split(' '))
# print("The number of operation required is: ", merge_operation(arr))


''' Question 5:  Arrange given numbers to form the biggest number.  

        steps:
              1. First we convert int to str.
              2. Then we loop through the 1-array for i from 0 to len(arr) and for j from i+1 to len(arr)
              3. Then we concatenate first-second and second-first string and compare which is bigger and then swap.
                '''

# def biggest_number(arr):
#
#     for i in range(len(arr)):
#         arr[i] = str(arr[i])
#
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[j]+arr[i] >= arr[i]+arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#
#     result = "".join(arr)
#     print("The biggest number is: ", result)
#
# if __name__ == "__main__":
#     arr = list(int(num) for num in input("Enter the elements: ").strip().split(', '))
#     biggest_number(arr)