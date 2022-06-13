# Write a program to count the duplicates in the given string.

# Input Format:
# Take String from stdin.

# Output Format:
# Display the duplicate character and the count of the character.

# Example Input:
# google

# Output:
# g:2
# o:2

# Example Input:
# rec

# Output:
# Not Exists

st=input()
st2=" "
j=0
for i in st:
    st2=st2+i
    if(st.count(i)>1):
        if(st2.count(i)==1):
            print("{}:{}".format(i,st.count(i)))
    else:
        j+=1
    if(j==len(st)):
        print("Not Exists")
