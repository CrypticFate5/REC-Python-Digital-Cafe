# The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate (5 percent) when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values are displayed using two decimal places.

# Sample Input

# 100

# Sample Output

# The tax is 5.00 and the tip is 18.00, making the total 123.00

n=int(input())
ans=n+ n*0.05 + n*0.18
print("The tax is {:.2f}".format(0.05*n),"and the tip is {:.2f},".format(0.18*n),"making the total {:.2f}".format(ans))
