n = input("enter a number:")
n = int(n)


# is positive or negstive
if n > 0:
    print("number is positive")
elif n < 0:
    print("number is negative")
else:
    print("number is zero")


#is even or odd
if n % 2 == 0:
    print("number is even")
else:
    print("number is odd")


# is divisible by 3 , 5 ,7 
if n % 3 == 0:
    if n % 5 == 0:
        if n % 7 == 0:
            print("number is divisible by 3, 5 and 7")
        else :
            print("number is divisible by 3 and 5")
    elif n % 7 == 0:
        print("number is divisible by 3 and 7")
    else:
        print("number is divisible by 3")
elif n % 5 == 0:
        if n % 7 == 0:
            print("number is divisible by 5 and 7")   
        else:
            print("number is divisible by 5")
elif n % 7 ==0:
    print("number is divisible by 7")
else:
    print("number isnt divisible by either 3, 5, 7")
    

  # is it a square 
if n**0.5 == int(n**0.5):
    print("is a square")

 # is it divisible by 10 or betwween 100 to 1000
if n % 10 == 0:
    print("number n is divisible by 10")
else :
    print("number n is not divisible by 10")
if n >= 100 and n <= 1000:
    print("number n is in range of 1000 to 100")
else :
    print("number n is not in range of 1000 to 100")

      