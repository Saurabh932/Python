'''Question 1: Reverse the String
'''
# # a = input("Enter the string: ")
# # rev_str = a[::-1]
# # print("The reverse string is ", rev_str)
#
#
'''Question 2: Fibonacci Number, by FAANG
'''
# # n = int(input("Enter the length of the serise: "))
# # t1 = 0
# # t2 = 1
# #
# # for i in range(0, n-1):
# #     if i == 0:
# #         print(t1, end=" ")
# #     if i == 1:
# #         print(t2, end=" ")
# #     else:
# #         next_t = t1+t2
# #         t1 = t2
# #         t2 = next_t
# #         print(next_t, end=" ")
# #
# # #
# # def fib(n):
# #     t1 = 0
# #     t2 = 1
# #
# #     for i in range(0,n-1):
# #         if i==0:
# #             return t1
# #         if i==1:
# #             return t2
# #         if i>=0:
# #             next_t = t1+t2
# #             t1 = t2
# #             t2 = next_t
# #
# #         return next_t
# #     # return 0
# #
# # n = int(input("Enter the size: "))
# # print(fib(n))
#
#
#
'''Question 3: Check If Two String Arrays are Equivalent, by Facebook
  - Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
'''
# #
# # def eqv(a, b):
# #     for i in a:
# #         for j in b:
# #             if i == j:
# #                 return True
# #             else:
# #                 return False
# #
# #     return 0
# #
# #
# # a = input("Enter 1st word: ")
# # b = input("Enter 2nd word: ")
# #
# # print(eqv(a,b))
#
#
#
''' Question 4: Matrix Diagonal Sum, by Adobe
 - Given a square matrix mat, return the sum of the matrix diagonals.
 - Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
 that are not part of the primary diagonal.'''
#'''
# # r = int(input("Enter the size of rows: "))
# # c = int(input("Enter the size of columns: "))
# #
# # matrix = []
# #
# # for i in range(r):
# #     a=[]
# #     for j in range(c):
# #         a.append(int(input("Enter the row elements :")))
# #     matrix.append(a)
# #
# # for i in range(r):
# #     for j in range(c):
# #         print(matrix[i][j], end=' ')
# #     print()
# #
# # dia1 = 0
# # dia2 = 0
# # for i in range(r):
# #     for row in a[i]:
# #     for j in range(c):
# #         dia1 = dia1 + i[r-i-1] j[c-j-1]
# #         dia2 = dia2 + i[i-r-1] j[j-c-1]
# #
# # # '''one liner to take matrix frm user'''
# # # mat = [[int(input()) for x in range (c)] for y in range(r)]
# # # print(mat)
#
#
#
#
'''Question 5: Final Prices With a Special Discount in a Shop, by Dream11
- Given the 1-array prices where prices[i] is the price of the ith item in a shop.
- There is a special discount for items in the shop, if you buy the ith item,
  then you will receive a discount equivalent to prices[j] where j is the minimum index
  such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.
- Return an 1-array where the ith element is the final price
  you will pay for the ith item of the shop considering the special discount.'''

# # Solution:
# # n = int(input("Enter the size of the 1-array: "))
# # price = []
# # for x in range(n):
# #     ele = int(input("Enter the elements: "))
# #     price.append(ele)
# # print(price)
#
# # for i in range(0, n):
# #     for j in range(1,n):
# #         if price[i]>=price[j]:
# #             final_price = price[i] - price[j]
# #             print("The final price: "+ final_price, end=" ")
# #         else:
# #             print(price[i])
#
#
#
# # def discounted_price(price, discount):
# #
# #     dis = price - (float(price * discount)/100.0)
# #     return dis
# #
# # price = int(input("Enter the price: "))
# # discount = float(input("Enter the discount: "))
# # print(discounted_price(price, discount))
#
#
#
#
'''Question 6: Reverse Words in a String III, by Amazon
# - Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
# '''
#
# def reverse_string(string):
#     st = list()
#
#     for i in range(len(string)):
#         if string[i] != " ":
#             st.append(string[i])
#
#         else:
#             while len(st)>0:
#                 print(st[-1], end="")
#                 st.pop()
#             print(end=" ")
#
#     while len(st)>0:
#         print(st[-1], end="")
#         st.pop()
#
# if __name__ == "__main__":
#     string = input("Enter the string: ")
#     reverse_string(string)



'''Question 7: Armstrong Number'''

# def check_armstrong(num):
#     temp = num
#     sum = 0
#
#     while temp>0:
#         digit = temp%10
#         sum += digit**3
#         temp //= 10
#
#     if num == sum:
#         return True
#     else:
#         return False
#
# print(check_armstrong(153))


# n = int(input("Enter the number: "))
# sum=0
# temp=n
#
# while temp>0:
#     digit = temp%10
#     sum += digit**3
#     temp //= 10
#
# if n == sum:
#     print(True)
# else:
#     print(False)



'''Question 8: Prime Number'''

# def isprime(num):
#     if num%2 != 0 and num%num == 0:
#         return True
#     else:
#         return False
#
# num = int(input("Enter the number: "))
# print(isprime(num))



'''Question 9: Factorial Number'''

# def factrial(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * i
#     return fact
#
# num = int(input("Enter the number: "))
# print(factrial(num))


'''Question 10: Pascal Number'''

