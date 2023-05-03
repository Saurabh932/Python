''' Question 1:  Given an 1-array a[] of size n. For every i from 0 to n-1 output max(a[0], a[1],..., a[i]).
    Approach:
1. Keep a variable mx which stores the maximum till i
th element.
2. Iterate over the 1-array and update,
mx = max(mx, a[i])
    '''

#
# def max_till_i(arr, n):
#     till_i = []
#     ''' Maximum value stored at every iteration so take very small number because we have to maximize at every step.'''
#     mx = -19999999
#     for i in range(0, len(arr)):
#         mx = max(arr[i], mx)
#         till_i.append(mx)
#     return till_i
#
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split())
#
# print(max_till_i(arr, n))


'''Question 2:  Sum of all SubArrays 

    Formula to find no. of sub-1-array:
     number of subarray = nC2 * n = n*(n+1)/2
  
  Problem - Given an 1-array a[] of size n. Output sum of each subarray of the given 1-array.
  
  Idea: Iterate over all subarrays and output the sum after each iteration.
  
  Approach: 
  1. Write a nested loop, where outer loop runs from i=0 to i=n-1 and inner loop runs from j=i to j=n-1.
  2. Keep a curr variable which stores the sum from i to j. 
  3. Output curr after each iteration of inner loop. After inner loop ends, update curr = 0.
    '''


# def sub_array(arr, n):
#     subarray = []
#     current_sum = 0
#     for i in range(0, n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += arr[j]
#             subarray.append(current_sum)
#
#     return subarray
#
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split())[:n]
#
# print(sub_array(arr, n))



'''
    Arrays Challenge-Longest Arithmetic Subarray (Google kickstart)
Problem An arithmetic 1-array is an 1-array that contains at least two integers and the differences between consecutive integers are equal.
For example, [9, 10], [3, 3, 3], and [9, 7, 5, 3] are arithmetic arrays, while [1, 3, 3, 7], [2, 1, 2], and [1, 2, 4] are not arithmetic arrays.

Sarasvati has an 1-array of N non-negative integers. The i-th integer of the 1-array is Ai.
She wants to choose a contiguous arithmetic subarray from her 1-array that has
the maximum length. Please help her to determine the length of the longest contiguous arithmetic subarray.
'''

# def longest_subarray(arr, n):
#     ans = 2
#     previous_diff = arr[1] - arr[0]
#     j = 2
#     curr_ans = 2
#
#     while j<n:
#         if previous_diff == arr[j] - arr[j-1]:
#             curr_ans = curr_ans+1
#
#         else:
#             previous_diff = arr[j] - arr[j-1]
#             curr_ans = 2
#
#         ans = max(ans, curr_ans)
#         j = j+1
#     return ans
#
#
# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the numbers: ").strip().split())[:n]
#
# print(longest_subarray(arr, n))
