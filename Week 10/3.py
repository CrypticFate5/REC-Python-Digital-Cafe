# In this exercise you will write a function that determines whether or not a password is good. We will define a good password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one number. Your function should return True if the password passed to it as its only parameter is good. Otherwise it should return False. Include a main program that reads a password from the user and reports whether or not it is good. Ensure that your main program only runs when your solution has not been imported into another file.

# Sample Input 1

# chennai

# Sample Output 1

# That isn't a good password.

# Sample Input 2

# Chennai18

# Sample Output 2


# That's a good password.

t=input()
if(len(t)>=8):
    lc=0
    uc=0
    n=0
    for i in t:
        if(i.isupper()):
            uc+=1
        elif(i.islower()):
            lc+=1
        elif(i.isdigit()):
            n+=1
    if(uc>0 and lc>0 and n>0):
        print("That's a good password.")
    else:
        print("That isn't a good password.")
else:
    print("That isn't a good password.")
