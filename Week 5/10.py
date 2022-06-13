# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:

# Input: 

# thequickbrownfoxjumpsoverthelazydog

# Output: 

# true

# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:

# Input: 

# arvijayakumar

# Output: false

 



# Constraints:



# 1 <= sentence.length <= 1000

# sentence consists of lowercase English letters.

st=input()
flag=0
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if(i not in st):
        flag=1
        break
if(flag==1):
    print("false")
else:
    print("true")
