''' Question 1: Write a program to find a unique number in an 1-array where all number expect one, are present twice '''

# def unique_no(arr):
#     xor_sum = 0
#     for i in range(len(arr)):
#         xor_sum = xor_sum ^ arr[i]
#     return xor_sum
#
# arr = list(int(i) for i in input("Enter the input: ").strip().split(","))
# print("The unique no. is: ", unique_no(arr))


''' Question 2: Write a program to find a unique numbers in an 1-array where all number are present twice
            
            logic:
                  We do  same as Question 1 but to sperate two numbers we do and operation with xor_sum which is giving 0.'''
#
# def unique_no(arr):
#     xor_sum = 0
#     for i in range(len(arr)):
#         xor_sum = xor_sum ^ arr[i]
#
#     # To seperate the xor_sum we do (x & ~(x-1)) to find rightmost bit
#     xor_sum = xor_sum & ~(xor_sum-1)
#     #  Seperate the number --> & with the number, different
#
#     # Storing the seperated number
#     set_1 = 0
#     set_2 = 0
#     for i in range(len(arr)):
#         if xor_sum & arr[i]:    # In this condition if the condition is true or set bit or non-zero is present then we set 1st unique number
#             set_1 = set_1 ^ arr[i]
#         else:
#             set_2 = set_2 ^ arr[i]
#     return set_1, set_2
#
# arr = list(int(i) for i in input("Enter the input: ").strip().split(","))
# print("The unique no. is: ", unique_no(arr))


''' Question 3: Write a program to find a unique number in an 1-array where all number expect one, are present thrice.
            Logic: we count the bit of 1's an 0' at every unit, if the total no. of bit of 1 and 0 are non-divisible by 3
                    then we append the bit and by continuning this steps we get the unique number. 
                    [1,2,3,4,1,2,3,1,2,3]
                1    2    3    4
               001  010  011  100                                      The required answer ---->     0
               001  010  011  ^^^
               001  010  011  
               ^^^  ^^^  ^^^  
               
               at unit bit: 1's ==> 6%3 == 0   (We didn't consider this)
                            0's ==> 4%3 != 0   (We consider this so we append 0 in the answer)
               
               at unit bit: 1's ==> 6%3 == 0   (We didn't consider this)
                            0's ==> 4%3 != 0   (We consider this so we append 0 in the answer)
                            
               at unit bit: 1's ==> 6%3 == 0   (We consider this so we append 1 in the answer)
                            0's ==> 4%3 != 0   (We didn't consider this)
 '''

# def get_bit(n, pos):
#     return ((n & (1<<pos)) != 0)
#
# def set_bit(n, pos):
#     return (n | (1<<pos))
#
# def unique(arr, n):
#     result = 0
#     for i in range(0, 32):  # In this line we have given 32bit space and we traverse till 32 bits
#         sum = 0
#         for j in range(len(arr)):  # In this we are traversing from 0 to len(arr)
#             if get_bit(arr[j],i):   # In this we are checking which elements has set bit at i_th position.
#                 sum += 1          # if i has set bit then we do +1.
#
#         if sum%3 != 0:     # Then we divide sum with 3 if it is not divisble then we append it in the answer.
#             result = set_bit(result, i)
#
#     return result
#
# n = int(input("Enter the length: "))
# arr = list(int(num) for num in input("Enter the input: ").strip().split(","))[:n]
# print("The unique number is: ",unique(arr, n))