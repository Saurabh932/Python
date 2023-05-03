''' --> Creating 1D 1-array using Naive Method: '''

# n = 5
# arr = [int(input("Enter the input: "))]*n
# print(arr)


''' -->  Creating 1D 1-array using list comprehension:  
            
            Here we are multiplying the number of rows by the empty list and hence the entire list is created with every element zero.'''
#
# n = 5
# # arr = [0 for i in range(n)]
# arr = [int(input("Enter the inpot: ")) for i in range(n)]
# print(arr)


'''  -->  Creating a 2-D list using Naive Method:  
            
            Explanation: 

Here we are multiplying the number of columns and hence we are getting the 1-D list of size equal to the number of columns 
and then multiplying it with the number of rows which results in the creation of a 2-D list.

Something to be careful:

Using this method can sometimes cause unexpected behaviors. In this method, each row will be referencing the same column. 
This means, even if we update only one element of the 1-array, it will update same column in our 1-array.
                                                                                                    '''
# row = 3
# col = 3
#
# arr = [[0]*col]*row
# print(arr)


# # Example 2: updating only one elements:
# row = 3
# col = 3
#
# arr = [[0]*col]*row
# print("Before --> ", arr)
#
# arr[0][0] = 1  # Updating only one elements
# print("After --> ", arr)



