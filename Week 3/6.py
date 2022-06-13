# The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

# Sample Input 1

# February

# Sample Output 1

# February has 28 or 29 days in it.

# Sample Input 2

# March

# Sample Output 2

# March has 31 days in it.

# Sample Input 3

# April

# Sample Output 3

# April has 30 days in it.

st=input()
l31=["January","March","May","July","August","October","December"]
if(st in l31):
    print(st,"has 31 days in it.")
elif(st=="February"):
    print("February has 28 or 29 days in it.")
else:
    print(st,"has 30 days in it.")
