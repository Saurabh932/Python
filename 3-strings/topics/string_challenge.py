'''  Question 1: Change a string into lower case and upper case:  '''

# a = input("Enter the string: ")
# print(a.lower())
# print(a.upper())


''' Question 2: From a biggest number from the numeric string:  '''

# a = input("Enter the string: ")
# largest = ""
# lst = sorted(a, reverse=True)
# for i in lst:
#     largest += i
# print(largest)


''' Question 3: Count the element which occur max time.'''
line = input("Enter the string: ")

for i in line:
    freq = 0
    occ = line.count(i)
    if occ > freq:
        freq = str(occ)
print(max(freq))
