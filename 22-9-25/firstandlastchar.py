s=input("enter a string:")
if len(s)>1:
    newstring=s[-1]+s[1:-1]+s[0]
else:
    newstring=s
print(newstring)
    
