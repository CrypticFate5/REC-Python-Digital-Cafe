# Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an appropriate error message.

# Sample Input 1

# 3

# Sample Output 1

# That's a triangle

# Sample Input 2

# 7

# Sample Output 2

# That's a heptagon

# Sample Input 3

# 11

# Sample Output 3

# That number of sides is not supported by this program.

n=int(input())
l=["triangle","quadrilateral","pentagon","hexagon","heptagon","octagon","nanogon","decagon"]
if(n>10):
    print("That number of sides is not supported by this program.")
else:
    print("That's a",l[n-3])
