''' Printing characters using character 1-array:  '''
n = int(input("Enter the size: "))
arr = list(a for a in input("Enter the input: "))[:n+1]
i = 0
while arr[i] != '\0':
    print(arr[i])
    i+=1