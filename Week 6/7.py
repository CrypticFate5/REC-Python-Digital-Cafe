# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Write a program if n array is monotonic or not. Print "True" if is monotonic or "False" if it is not. Array can be monotone increasing or decreasing

# Sample Input1

# 6578

# Sample Output1

# True

# Sample Input2

# 6543

# Sample Output2

# True

# Sample Input 3

# 6787

# Sample Output3

# False

st=input()
l=st.split()
la=[]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>=l[j] or l[i]<=l[j]):
            la.append(0)
            break
if 1 in la:
    print("False")
else:
    print("True")
