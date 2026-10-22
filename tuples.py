list = []
n = int(input("enter how many no. will be in the tuple:\n"))
if n >= 0 and n <= 10:
    for i in range(n):
        x = int(input("enter the no. in tuple:(0 - 100)"))
        if x >= 0 and x <= 100:
            list.append(x)
        else :
            print("error: no. should be in range of (0 -100)")
else :
        print("error: no. should be in range of (0 -10)")


marks = tuple(list)
print("marks:",marks)
no_subjects = len(marks)
print("no. of subjects",no_subjects)
first_sub = 0
last_sub = no_subjects - 1
print("first subject:",marks[first_sub])
print("last subject:",marks[last_sub])
if n > 4:
    print("first four:",marks[:4])
print("total marks:",sum(marks))
print("subjects with 92 marks:",marks.count(92))
print("does it has full 100 marks:",100 in marks)
print("maximum marks:",max(marks))
print("minimum marks:",min(marks))
new = (89 ,67)
new_marks = marks + new
print("new tuple with extra added marks",new_marks)
repeat = marks*2
print("repeating tuple:",repeat)
