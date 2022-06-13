# In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were first entered. For example, if the user enters:

# first

# second

# first

# third

# second

# then your program should display:

# first

# second

# third

l=[]
st=input()
while(st!='\n'):
    if(st not in l):
        l.append(st)
        print(st)
    try:
        st=input()
    except EOFError:
        break;
        
