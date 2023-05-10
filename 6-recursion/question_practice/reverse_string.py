''' Question: Reverse the string using Recursion.
            Logic:
                  The logic is that we take off each element from the string till it is null then strat print the first element from
                  the string and concatenate the string[0].
            '''

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

string = input("Enter the string: ")
print(reverse(string))