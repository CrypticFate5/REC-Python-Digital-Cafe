# Consider the below words as key words and check the given input is key word or not.

# keywords: {break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var}

# Input format:

# Take string as an input from stdin.

# Output format:

# Print the word is key word or not.

# Example Input:

# break

# Output:

# break is a keyword

# Example Input:

# IF

# Output:

# IF is not a keyword


# For example:

# Input	Result
# break
# break is a keyword
# IF
# IF is not a keyword


s="break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var"
st=input()
if(st in s):
    print(st,"is a keyword")
else:
    print(st,"is not a keyword")
