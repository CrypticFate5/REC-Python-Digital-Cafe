# In the game of Scrabble™, each letter has points associated with it. The total score of a word is the sum of the scores of its letters. More common letters are worth fewer points while less common letters are worth more points. The points associated with each letter are shown below:

# Points Letters

# 1 A, E, I, L, N, O, R, S, T and U

# 2 D and G

# 3 B, C, M and P

# 4 F, H, V, W and Y

# 5 K

# 8 J and X

# 10 Q and Z

# Write a program that computes and displays the Scrabble™ score for a word. Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.

# A Scrabble™ board includes some squares that multiply the value of a letter or the value of an entire word. We will ignore these squares in this exercise.

# Sample Input

# REC

# Sample Output

# REC is worth 5 points.

st=input()
st1="AEILNORSTU"
st2="DG"
st3="BCMP"
st4="FHVWY"
st5="K"
st8="JX"
st10="QK"
d={}
s=0
for i in st:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i in d.keys():
    if i in st1:
        s+=d[i]
    elif i in st2:
        s+=2*d[i]
    elif i in st3:
        s+=3*d[i]
    elif i in st4:
        s+=4*d[i]
    elif i in st5:
        s+=5*d[i]
    elif i in st8:
        s+=8*d[i]
    elif i in st10:
        s+=10*d[i]
print("{} is worth {} points.".format(st,s))
