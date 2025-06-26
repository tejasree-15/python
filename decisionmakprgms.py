#write a python program to find whether the number is positive or not.
num=int(input("enter a number: "))
if num>0:
	print("the number is positive",num)

#write a program to find biggest of two numbers
a=int(input("enter a value: "))
b=int(input("enter b value: "))
if a>b:
	print("a is greater",a)
else:
	print("b is greater",b)

#accept the percentage from the user and display the grade according to the following criteria.
pr=int(input("enter your percentage:"))
if pr<=25:
	print("your grade is D")
elif pr>=25 and pr<=45:
	print("your grade is C")
elif pr>=46 and pr<=50:
	print("your grade is B")
elif pr>=51 and pr<=60:
	print("your grade is B+")
elif pr>=61 and pr<=80:
	print("your grade is A")
elif pr>80:
	print("your grade is A+")
else:
	print("you are failed!!")

#write a program to display the week names by taking input from the user.
day=int(input("enter your day:"))
if day==1:
	print("sunday")
elif day==2:
	print("monday")
elif day==3:
	print("tuesday")
elif day==4:
	print("wednesday")
elif day==5:
	print("thursday")
elif day==6:
	print("friday")
elif day==7:
	print("saturday")
else:
	print("invalid week no")

#write a python program display the monuments according to the city given by user.
city=(input("enter the city name:"))
if city == "hyderabad":
    print("charminar")
elif city=="delhi":
    print("red port")
elif city=="agra":
    print("tajmahal")
elif city=="chennai":
    print("marina beach")
elif city=="rajahmundry":
    print("godavari")
else:
    print("wrong city selected")
#accept the number of days from the user and calculate the library according to the following.
num= int(input("enter the day:"))
if num>=5:
	print("the charge is:",num*2)
elif num<=6:
	print("the charge is:",num*3)
elif num>=11 and num<=15:
	print("the charge is:",num*4)
elif num>=15:
	print("the charge is:",num*5)
else:
	print("the number is invalid",num)

#write a program accept 2 numbers from the user and a operator from the user and perform accordingly.
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
opr=(input("enter a operator :"))
if opr=="+":
	print("the answer:",num1+num2)
elif opr=="-":
	print("the answer:",num1-num2)
elif opr=="/":
	print("the answer:",num1/num2)
elif opr=="*":
	print("the answer:",num1*num2)  
else:
	print("wrong operator selected..")

#write a program to accept a number from 1 to 12 and display name of the month and days in that month 
mon_num=int(input("enter the month no:"))
if mon_num==1:
	print("the month is january it has 31 days")
elif mon_num==2:
	print("the month is february it has 30 days")
elif mon_num==3:
	print("the month is march it has 31 days")
elif mon_num==4:
	print("the month is april it has 30 days")
elif mon_num==5:
	print("the month is may it has 31 days")
elif mon_num==6:
	print("the month is june it has 30 days")
elif mon_num==7:
	print("the month is july it has 31 days")
elif mon_num==8:
	print("the month is august it has 31 days")
elif mon_num==9:
	print("the month is september it has 30 days")
elif mon_num==10:
	print("the month is october it has 31 days")
elif mon_num==11:
	print("the month is november it has 30 days")
elif mon_num==12:
	print("the month is december it has 31 days")
else:
	print("invalid month number")

#write a program to display "HELLO" if a number entered by user is a multiple of five otherwise print "BYE".
num=int(input("enter a number:"))
if num%5==0:
	print("HELLO")
else:
	print("BYE")

#write a program to display percentages according to following criteria.
#>90 -->A,>80 and <=90 --->B,>60 and <=80 --->C,<=60 ---D
pr=int(input("enter your percentage:"))
if pr>90:
	print("your grade is A")
elif pr>80 and pr<=90:
	print("your grade is B")
elif pr>60 and pr<=80:
	print("your grade is C")
elif pr<=60:
	print("your grade is D")
else:
	print("failedd!!") 





