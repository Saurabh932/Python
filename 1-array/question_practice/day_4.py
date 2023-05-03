'''
Question 1:  Chocolate Distribution Problem
            Given an 1-array of N integers where each value represents the number of chocolates in a packet.
            Each packet can have a variable number of chocolates. There are m students,
            the task is to distribute chocolate packets such that:

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and
the packet with minimum chocolates given to the students is minimum.
'''
from _testcapi import INT_MAX

#
# def chocolate(arr,n,m):
#     arr_sort = sorted(arr)
#     lt = [[]]
#     new_diff = []
#     for i in range(0, n+1):
#         for j in range(i):
#             lt.append(arr_sort[j:i])
#
#     for i in range(0, len(lt)):
#         if len(lt[i]) == m:
#             diff = max(lt[i]) - min(lt[i])
#             new_diff.append(diff)
#
#     return min(new_diff)
#
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split())[:n]
# m = int(input("Enter the number of stidents: "))
#
# print("The minimum choclates: ", chocolate(arr, n, m))


'''
   Question 2:  Best Time to Buy and Sell Stock
                You are given an 1-array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
                                        '''
# def max_profit(arr, n):
#     m = arr[0]
#     for i in range(0, n):
#         if arr[i] < m:
#             m = arr[i]
#
#     m_index = arr.index(m)
#     l = arr[m_index]
#     for j in range(m_index, n):
#         if arr[j] > l:
#             l = arr[j]
#             profit = l - m
#
#     return profit
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the number: ").strip().split())[:n]
#
# print("The maximum profit is: ", max_profit(arr, n))


''' 
    Question 3.  Maximum Product Subarray
                 Given an integer 1-array nums, find a subarray that has the largest product, and return the product.                          '''

# def product_subarray(arr, n):
#     result = arr[0]
#     for i in range(0,n):
#         product = arr[i]
#         for j in range(i+1,n):
#             result = max(result, product)
#             product = product * arr[j]
#         result = max(result, product)
#     return result
#
# n = int(input("Enter the number: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(","))[:n]
#
# print("The Kth element: ", product_subarray(arr, n))


'''
    Question 4:  A permutation of an 1-array of integers is an arrangement of its members into a sequence or linear order.
                For example, 
                            for arr = [1,2,3], 
                            the following are all the permutations of arr: 
                                            [,21,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
                                                                                                    '''

# def permutation(nums : list[int]):
#     n = len(nums)
#     pivot = 0
#     # finding pivot
#     for i in range(n-1,0,-1):
#         if nums[i-1] < nums[i]:
#             pivot = i
#             break
#
#     if pivot == 0 :
#         nums.sort()
#         return
#
#     # then find the swap which first number>pivot
#     swap = n-1
#     while nums[pivot-1] >= nums[swap]:
#         swap -= 1
#
#     # swap
#     nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
#
#     # reverse from point
#     nums[pivot:] = sorted(nums[pivot:])
#     return nums
#
# arr = list(int(num) for num in input("Enter the element: ").strip().split(","))
# print(permutation(arr))


'''
    Question 5:  Maximum Subarray
                Given an integer 1-array nums, find the subarray with the largest sum, and return its sum.'''


# def max_sub_array(arr):
#     max_sum = arr[0]
#     curr_sum = arr[0]
#
#     for i in range(1, len(arr)):
#         curr_sum = max(arr[i], curr_sum + arr[i])
#         max_sum = max(max_sum, curr_sum)
#
#     return max_sum
#
# arr = list(int(num) for num in input("Enter the elements: ").strip().split(","))
# print("The max sub-1-array is: ",max_sub_array(arr))