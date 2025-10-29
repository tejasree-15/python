n=int(input("enter a number:"))
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if reverse==original:
    print("It is a palindrome number : ")
else:
    print("not a palindrome number : ")