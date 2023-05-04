''' Question 1: Valid Palindrome
                A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
                removing all non-alphanumeric characters, it reads the same forward and backward.
                Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''

# print(dir(str))
# a = input("Enter the string: ")
# a_str = ""
#
# for i in a:
#     if i.isalnum():
#         a_str += i.lower()
# print("The stripped string are: ",a_str)
#
# for i in range(len(a_str)):
#     if a_str[i] != a_str[len(a_str)-1-i]:
#         print(False)
# print(True)


''' Question 2:  Valid Anagram
                Given two 3-strings s and t, return true if t is an anagram of s, and false otherwise.
                An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
                typically using all the original letters exactly once.'''

# s = input("Enter the first string: ")
# t = input("Enter the second string:")
#
# x = [s[i] for i in range(0,len(s))]
# x.sort()
# y = [t[j] for j in range(0, len(t))]
# y.sort()
#
# if x == y:
#     print(True)
# else:
#     print(False)


'''  Question 3: Valid Parentheses
                Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
#                                                                       '''
# def valid_parentheses(str):
#     while True:
#         if "()" in str:
#             str = str.replace("()", "")
#         elif "[]" in str:
#             str = str.replace("[]", "")
#         elif "{}" in str:
#             str = str.replace("{}", "")
#         else:
#             return not str
#
# str = input("Enter the string inside parentheses: ")
#
# print(valid_parentheses(str))


'''     NOT UNDERSTOOD:
 Question 4:  Longest Substring Without Repeating Characters
                Given a string s, find the length of the longest substring without repeating characters.'''

#
# def lengthOfLongestSubstring(s):
#     x = []
#     count = 0
#     max_count = 0
#     for i in range(len(s)):
#         if s[i] not in x:
#             x.append(s[i])
#             count += 1
#         else:
#             x = x[x.index(s[i]) + 1:]
#             x.append(s[i])
#             count = len(x)
#         max_count = max(max_count, count)
#     return max_count
#
#
# s = input("Enter the string: ")
# print(lengthOfLongestSubstring(s))
#
#
#
#         return string
#
#     if string[0] != string[1]:
#         return string[0] + remove_consecutive(string[1:])
#     return remove_consecutive(string[1:])
#
# string = input("Enter the string: ")
# print(remove_consecutive(string))