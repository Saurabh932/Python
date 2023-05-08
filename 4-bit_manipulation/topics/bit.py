'''  Get Bit() -->  AND Operator  '''

# def get_bit(n, pos):
#     return ((n & (1<<pos)) != 0)    # In this line we have done AND operation on n and pos where 1 is lefted by number of pos which is 2
#                                     # n = 0101,  if we want to shift 1 at the postion we do left shift times postion
# print(get_bit(5,2))


'''  Set Bit()  -->  OR Operator  
                n = 0101
    Suppose we need to set bit at postion i=1
            1 << i ==0010           # NOTE: Here we have left shifted 1 which is 0001
        0101 | 0010 = 0111   '''

# def set_bi(n, pos):
#     return ((n | (1<<pos)))
#
# print(set_bi(5,1))


'''  Clear Bit() -->  NOT Operator
            n = 0101
        Suppose we need to clear bit at position i=2 means need to make zero
            1 << i = 0100           # NOTE: Here we have left shifted 1 which is 0001
            ~0100 = 1011        
            0101 & 1011 = 0001   '''

# def clear_bit(n, pos):
#     mask = ~(1<<pos)
#     return (n & mask)
#
# print(clear_bit(5,2))


'''  Update Bit() -->  It is noting but Clear Bit and SET Bit
            n = 0101
        Suppose we need to update bit at position i=1 to 1
            1 << i = 0010             # NOTE: Here we have left shifted 1 which is 0001
            ~0010 = 1011        
            0101 & 1011 = 0101  
            1 << i == 0010 
            0101 | 0010 = 0111              '''

def upadate_bit(n, pos, value):
    mask = ~(1 << pos)
    n = n & mask
    return (n | (value<<pos))

print(upadate_bit(5,1,1))