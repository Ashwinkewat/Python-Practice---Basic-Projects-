list = []
even_list = []
unique = []
result = 0
n = int(input("enter how many students you are gonna give marks:", ))
hmarks=0
lmarks=100
pass_count = 0
avg_count = 0
avg = 0
if n <= 10 and n > 0:
    for i in range(n):
        x = int(input("enter the marks(0 - 100)"))
        if x < 100 and x > 0:
            list.append(x)
            result += x
            avg = result // n
            if hmarks < x:
                hmarks = x
            if lmarks > x:
                lmarks = x
            if x > 40:
                pass_count+=1
            if x > avg:
                avg_count+=1
            if x % 2 == 0:
                even_list.append(x)
            for y in list:
                if x not in unique:
                    unique.append(x)

        else:
            print("error range should be in 0 -100;")
else:
    print("error:no. should be in range of 1 to 10.")
print("marks:",list)
list.reverse()
print("reverse list:",list)
print("total:",result)
print("average marks:",avg)
print("highest marks:",hmarks)
print("lowest marks:",lmarks)
print("how many students passed:", pass_count)
print("even marks:",even_list)
unique.sort()
print("only unique marks:",unique)