#Arthematic operators
a= int(input("enter a number: "))
b= int(input("enter a number: "))
print("the addition ",a+b)
print("the subtraction ",a-b) 
print("the multiplication ",a*b)
print("the division ",a/b)
print("the floor division ",a//b)
print("the  modulardivision",a%b)
print("the power ",a**b)
#RELATIONAL OPERATOR
a= int(input("enter a number: "))
b= int(input("enter a number: "))
print("the greater value ",a>b)
print("the lesser value ",a<b)
print("the greater than or equals too value ",a>=b)
print("the less than or equals too value  ",a<=b)
print("the equals too value ",a==b)
print("the not equals too value ",a!=b)
#LOGICAL OPERATOR
#AND:
a=23
b=45
c=a>=34 and b<=50
print(c)
#OR
a=67
b=89
c=a!=67 or b==89
print(c)
#NOT
a=10
print(not(a))#F
b=0
print(not(b))#T
#Bitwise operator
#AND(&)
a=5
b=9
c=a&b
print(c) 
#OR(|)
a=15
b=13
c=a|b
print(c)
#EXOR(^)
a=12
b=14
c=a^b
print(c)

#MEMBERSHIP OPERATOR
a= ["apple","banana"]
print("apple" in a)
print("pp" not in a)
print("banana" in a)
print("nn" not in a)

#IDENTITY OPERATOR
x=[1,2,3]
y=[4,5,6]
z=x
print(x is y)
print(y is z)
print(x is z)
print(x is not y)
print(y is not z)
print(x is not z)
        