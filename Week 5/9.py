# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.

# Example 1:

# Input: 

# RLRRLLRLRL

# Output:

# 4

# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:

# Input: 

# RLLLLRRRLR

# Output: 

# 3

# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

# Example 3:

# Input: 

# LLLLRRRR

# Output: 

# 1

# Explanation: s can be split into "LLLLRRRR".

 

# Constraints:

# 1 <= s.length <= 1000

# s[i] is either 'L' or 'R'.

# s is a balanced string.

st=input()
cr=0
cl=0
ans=0
for i in st:
    if(i=='R'):
        cr+=1
    else:
        cl+=1
    if(cr==cl):
        ans+=1
print(ans)
