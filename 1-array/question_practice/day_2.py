
#####################     ARRAYS:     #############################################

''' Question: 1   Maximum and Minimum Element in an Array'''

# Solution:

# arr = []
# n = int(input("Enter the size: "))
# for i in range(n):
#     ele = int(input("Enter the elements: "))
#     arr.append(ele)
# print(arr, end=" ")
#
# curr_max = arr[0]
# curr_min = arr[0]
#
# for i in range(len(arr)):
#     if arr[i] > curr_max:
#         curr_max = arr[i]
#
#     if arr[i] < curr_min:
#         curr_min = arr[i]
# print("\nThe max: ", curr_max)
# print("\nThe min: ", curr_min)
#
#
# #   Brute Froce:
# arr = []
# n = int(input("Enter the size of 1-array: "))
#
# for i in range(n):
#     ele = int(input("Enter the elements: "))
#     arr.append(ele)
#
# print("The 1-array: ", arr)
# print(max(arr))
# print(min(arr))




'''Reverse the Array'''

# arr = []
# n = int(input("Enter the size: "))
#
# for i in range(n):
#     ele = int(input("Enter the elements: "))
#     arr.append(ele)
# print("\nThe 1-array: ", arr, end=" ")
#
# reverse_arr = arr[::-1]
# print("\nThe reverse 1-array: ",reverse_arr)




'''Contains Duplicate'''
#
# n = int(input("Enter the size: "))
# arr = []
#
# for i in range(n):
#     ele = int(input("Enter the elements: "))
#     arr.append(ele)
# print(arr)
#
# duplicate = arr[0]
# for i in range(len(arr)):
#     if arr[i] == duplicate:
#         print("The duplicate is: ",duplicate)
#         break;
#     else:
#         print("No duplicates")



'''Repeat and Missing Number Array'''

# n = int(input("Enter the size: "))
# arr = list(int(num) for num in input("Enter the elements: ").strip().split())[:n]
#
# reapeat = arr[0]
# reapeat_list = []
# for i in range(len(arr)):
#     if i == reapeat:
#         reapeat_list.append(i)
# print("A = ", reapeat_list)
#
# missing_value = []
# for i in range(arr[0], arr[-1]+1):
#     if i not in arr:
#         missing_value.append(i)
# print("B = ", missing_value)



#   To get the missing value from the list

# n= int(input("Enter the size: "))
# arr = list(map(int, input("Enter the elements: ").strip().split()))[:n]
#
# missing_value = set(range(arr[0], arr[-1]+1)) - set(arr)
# print(list(missing_value))