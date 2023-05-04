'''  Question 1. Remove Consecutive Characters
                 Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.

                 '''

'''  Apporach:
            string = "aaabcccddd"
            Initially, both i and j are set to 0:
            
            string = "aaabcccddd"
            i = 0
            j = 0
            
            Now, the loop starts and the first character in the string is compared to the character at position j. 
            Since they are equal, i is incremented:
            
            string = "aaabcccddd"
            i = 1
            j = 0
            
            The next character is then compared to the character at position j. Since they are equal, i is incremented again:
            string = "aaabcccddd"
            i = 2
            j = 0
            
            This time, the character is different from the character at position j, so j is incremented:
            string = "aaabcccddd"
            i = 2
            j = 1
            
            And the character at position i is assigned to the character at position j:
            string = "aabcccddd"
            i = 2
            j = 1

            The process continues until the end of the string is reached:
            string = "abcd"
            i = 9
            j = 3
            
            Finally, the value of j is incremented and the string is sliced to return the final result:
            string = "abcd"'''

def consecutive(string):
    if len(string) < 2:
        return

    j = 0
    for i in range(len(string)):
        if string[j] != string[i]:
            j += 1
            string[j] = string[i]

    j += 1
    string = string[:j]
    return string


if __name__ == "__main__":
    string = input("Enter the string: ")
    string = list(string.rstrip())
    string = consecutive(string)
    print(*string, sep="")
