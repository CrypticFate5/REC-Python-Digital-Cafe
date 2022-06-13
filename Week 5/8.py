# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.

# Constraints:



# 1 <= s.length <= 10^4

# s consists of parentheses only '()[]{}'.


# For example:

# Input	Result
# ()
# true
# ()[]{}
# true
# (]
# false


s=input()
a=s.count('(')
b=s.count(')')
c=s.count('{')
d=s.count('}')
e=s.count('[')
f=s.count(']')
if(a==b and c==d and e==f):
    print("true")
else:
    print("false")
