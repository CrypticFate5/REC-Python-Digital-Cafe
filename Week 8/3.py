# Take a complete sentence as an input and remove duplicate word in it and print (sorted order), then count all the words which have a length greater than 3 and print.

# Input

# we are good are we good

# Output

# are good we

# Count = 1

st=sorted(set(input().split()))
c=0
for i in st:
    print(i,end=' ')
    if(len(i)>3):
        c+=1
print("\nCount =",c)
