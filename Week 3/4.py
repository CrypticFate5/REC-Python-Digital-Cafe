# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All three sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene.

# Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that states the triangle’s type.

# Sample Input 1

# 60

# 60

# 60

# Sample Output 1

# That's a equilateral triangle

# Sample Input 2

# 40

# 40

# 80

# Sample Output 2

# That's a isosceles triangle

# Sample Input 3

# 50

# 60

# 70

# Sample Output 3

# That's a scalene triangle

a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c):
    print("That's a equilateral triangle")
elif(a==b or b==c or a==c):
    print("That's a isosceles triangle")
else:
    print("That's a scalene triangle")
