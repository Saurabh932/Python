''' Question 1;  Write a programm to check if a given number is power of 2.'''

''' Normal Method:'''
# def find(n):
#    if (n == 0):
#       return False
#    while (n != 1):
#       if (n % 2 != 0):
#          return False
#       n = n // 2
#    return True
#
# # Driver code
# if(find(8)):
#    print('Yes')
# else:
#    print('No')

'''Bit Mnipulation:  '''

'''      LOGIC;
        In a given number when we filp(means changin 0 to 1 and 1 to 0) rightmost set bit (which is 1) and remaining bits after that then we get n-1 digit.
            n = 6 = 0110     if we do the above logic and flip 1 at postion 1 we get
            n-1 = 5 = 0101

            (n & n-1) has same bits as n except the rightmost set bit
            0110 & 0101 = 0100  '''

''' Apporach:  n has only one set bit, and n-1 will have all set bit after that postion.
               which means if we use AND operation on n and n-1 it will give 0'''

# def is_power_2(n):
#     return (n and (n & (n-1) == 0))   # First n is used for base case where n=0 and this will make it zero
#
# print(is_power_2(16))



''' Question 2: Write a program to count the number of 1's in binary representation of a number.

  logic: (n & n-1) has same bits as n except the rightmost set bit. We repeat this steps till we get 0 and count no. steps 
         which will give us number of 1's in the binary number
   n = 19 = 01011
   n-1 = 18 = 01010
   
   n = n & n-1
   n = 01010(18)   
   
   if we repeat this process till we get 0
   n = 18
   n-1 = 17
   n = n & n-1 = 16
   
   n = 16
   n-1 = 15
   n = n & n-1 = 0
   
   Above we have repeated the steps 3 times so the number of 1's.     '''

# def no_ones(n):
#     count = 0
#     while n != 0:
#         n = n & (n-1)
#         count += 1
#     return count
#
# n = int(input("Enter the number: "))
# print("The number of 1's are: ", no_ones(n))



''' Question 3: write a program to generate all possible subset of set.
                            {a,b,c}
                {}      000     0
                {c}     001     1 
                {b}     010     2
                {b,c}   011     3
                {a}     100     4
                {a,c}   101     5
                {a,b}   110     6
                {a,b,c} 111     7
                
        We Iterate 2^n-1 times 
        
        logic: 
                # In i loop, i is iterating from 0 to 2^n-1 where (1<<n) is 2^n
                                    # i = 0 --> 000 --> [0]
                                    # i = 1 --> 001 --> [1]
                                    # i = 2 --> 010 --> [2]
                                    # i = 3 --> 011 --> [1,2]
                                    # ... # i = 7 --> 111 --> [1,2,3]
                                     
                # In j loop we are checking if the bit is set bit so we use and operateor
                               # for example i = 2 = 010
                               #  at j = 0 = 001         010 & 001 == 000
                               #  at j = 1 = 010         010 & 010 == 010
                               #  at j = 2 = 100         010 & 100 == 000
                               #   So for [1,2,3] we only take [2] because position 1 has set bit '''

# def sub_sets(arr, n):
#     for i in range(0, (1<<n)):
#         for j in range(0, n):
#             if(i & (1<<j)):
#                 print(arr[j], end=" ")
#         print()
#
# arr = list(a for a in input("Enter the input: ").strip().split(","))
# sub_sets(arr, len(arr))
