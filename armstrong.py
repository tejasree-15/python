n=int(input("enter a number:"))
original=n
sum_of_powers=0
num_digit=len(str(n))
while n>0:
    digit=n%10
    sum_of_powers+=digit**num_digit
    n//=10
if original==sum_of_powers:
    print("It is an ARMSTRONG number :",original)
else:
    print("Not an ARMSTRONG number :",original)