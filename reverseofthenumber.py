def reverse1(num):
    reverse=0
    while num>0:
       digit=num%10
       reverse=reverse*10+digit
       num//=10
    return reverse
def reverse2():
    number=int(input("enter a number (minimum 4 digits):"))
    if number<1000:
        print("please enter a number with at least 4 digits")
        return
    reverse3=reverse1(number)
    print("original number:",number)
    print("reversed number:",reverse3)
reverse2()
