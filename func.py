def register_students(name, age , roll_no):
    if name.strip() == "":
        return "Error: Name can't be empty."

    elif age < 15 or age > 25:
        return "Error: Age must be between 15 and 25."

    elif roll_no <= 0:
        return "Error: Roll number must be positive."

    else:
        print(name,age,roll_no,sep="-")
        return "Registration successful!"

enter_name = input("enter students name:")
enter_age = int(input("enter students age:"))
enter_roll_no = int(input("enter students roll no :"))


register_students(enter_name, enter_age,enter_roll_no)

def validate_marks():
    subjects =["python","mathematics","english","science","computer networks"]
    scores =[]
    i = len(scores)
    while i<=4:
        scores.append(input("enter marks"))
        i+=1
    for subjects,scores in zip(subjects,scores):
        print(subjects,scores,sep="-")
validate_marks()
                        
            

