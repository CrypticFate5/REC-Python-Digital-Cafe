# Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one “e”, one “i”, one “l”, and one “v”. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.

# Sample Input 1

# evil 

# live

# Sample Output 1

# Those strings are anagrams.

# Sample Input 2

# meet 

# met

# Sample Output 2

# Those strings are not anagrams.

st1=input()
st2=input()
d1={}
d2={}
if(len(st1)!=len(st2)):
    print("Those strings are not anagrams.")
else:
    for i in st1:
        if i in d1.keys():
            d1[i]+=1
        else:
            d1[i]=1
    for i in st2:
        if i in d2.keys():
            d2[i]+=1
        else:
            d2[i]=1
    if(d1==d2):
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")
