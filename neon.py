n = int(input("enter a number :"))
square = n * n
digit_sum = 0
while square > 0:
    digit_sum += square % 10
    square //= 10
if digit_sum == n:
    print("It is a Neon Number : ")
else:
    print("Not a Neon Number : ")