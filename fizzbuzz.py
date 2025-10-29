n=int(input("enter a number :"))
for i in range(1,n):
    if (i%3==0 and i%5==0):
            print(i," = FizzBuzz")
    else:
        if (i%3==0):
            print(i," = Fizz")
        else:
            if(i%5==0):
                print(i," = Buzz")
            else:
                print(i)