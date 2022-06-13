# In a particular jurisdiction, older license plates consist of three uppercase letters followed by three digits. When all of the license plates following that pattern had been used, the format was changed to four digits followed by three uppercase letters.

# Write a program that begins by reading a string of characters from the user. Then your program should display a message indicating whether the characters are valid for an older style license plate or a newer style license plate. Your program should display an appropriate message if the string entered by the user is not valid for either style of license plate.

# Sample Input 1

# ABC123

# Sample Output 1

# The plate is a valid older style plate.

# Sample Input 2

# 123ABCD

# Sample Output 2

# The plate is not valid.

# Sample Input 2

# 1234ABC

# Sample Output 3

# The plate is a valid newer style plate.

st=input()
if(st[0:3].isupper() and st[4:len(st)].isdigit()):
    print("The plate is a valid older style plate.")
elif(st[0:4].isdigit() and st[5:len(st)].isupper()):
    print("The plate is a valid newer style plate.")
else:
    print("The plate is not valid.")
