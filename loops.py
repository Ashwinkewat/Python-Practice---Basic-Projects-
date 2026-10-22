N = int(input("enter a number"))
a = N
count = 0
total = 0
number = 0
num = 9
even_digits = 0
odd_digits = 0
two_apperance = 0
zero = 0
result = ""
while a > 0:
   i = a % 10
   if  i == 0:
      zero = 1
   a = a//10
   c = i + total
   total += i
   count += 1
   if number <= i:
       number = i
   if num >= i:
       num = i
   x = i % 2
   if x == 0 :
       even_digits+=1
   else:
       odd_digits+=1     
   if i == 2:
       two_apperance+=1   
   result += str(i)
print("reverse of no:",result)
print("no. of digits:", count)
print("sum of digits", c)
print("largest number", number)
print("smallest number", num)
print("no. of odd digits:", odd_digits)
print("no. of even digits:", even_digits)
print("occurence of two:",two_apperance)
if zero == 1:
    zero="true"
else:
    zero="false"
print("contains zero:",zero)
if result == str(N):
    print("is a palindrome:yes")
else:
    print("is a palindrome:no")
