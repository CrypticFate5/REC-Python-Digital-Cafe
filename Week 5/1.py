# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: 
# A man, a plan, a canal: Panama

# Output: 
# 1
# Example 2:

# Input: 
# race a car

# Output: 
# 0
#  Constraints:

# s consists only of printable ASCII characters.

s=input()
ss=""
for i in s:
    if(i.isalnum()):
        ss+=i.lower()
ssr=ss[::-1]
if(ss==ssr):
    print("1")
else:
    print("0")
