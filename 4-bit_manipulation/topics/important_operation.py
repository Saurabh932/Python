'''  To Take power of n:
            1. Used in finding subset or subsequencing.'''
# arr = [1,2,3]
# print(1<<len(arr))


''' To find Rightmost set bit  '''
# a = 8
# print(a & ~(a-1))


'''   Counting the number of set bit:   '''
def count_set(n):
    count = 0
    while n:
        count += n&1    # Checking if rightmost bit is 1, then incrementing count with 1
        n >>= 1     # Then discarding the rightmost value
    return count

n = int(input("Enter the number: "))
print("The total number of set bit is: ",count_set(n))