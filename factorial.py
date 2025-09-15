n=int(input("enter a positive number:"))
fact=1
if n>0:
    for i in range (1,n+1):
        fact=fact*i
    print("factorial of a given number is:",fact)
else:
    print("invalid")
