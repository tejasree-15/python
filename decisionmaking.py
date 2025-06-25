#if
a= 10
if a==10:
    print("the if statement is executed..")

#ifelse
age= int(input("enter age: "))
if age>=18:
    print("eligible for vote",age)
else:
    print("sorry!! not eligible because your age is",age)
#elif
userid = input("enter your userid  :")
password= input("enter your password  :")
if userid=="abcd12345" and password=="tej@1506":
    print("welcome to our netbanking of tttbank")
elif userid=="efgh6789" and password=="sri@2906":
    print("welcome to our netbanking of sssbank") 
else:
    print("the userid and password is incorrect...Tryagain!!")

#nestedif
a=10
b=20
c=30
if a==10 and c==30:
    print("the outer if executed..")
    if a==10:
        print("the inner if executed..")
    else:
        print("the inner else executed..")
else:
    print("the outer else executed..")