students = {
    "Aarav": {
        "age": 17,
        "subjects": ["Maths", "Science", "English"],
        "marks": (85, 92, 78),
        "hobbies": {"Reading", "Cricket"}
    },
    "Diya": {
        "age": 16,
        "subjects": ["Maths", "Science", "English"],
        "marks": (95, 88, 91),
        "hobbies": {"Painting", "Reading"}
    },
    "Kabir": {
        "age": 17,
        "subjects": ["Maths", "Science", "English"],
        "marks": (45, 38, 55),
        "hobbies": {"Cricket", "Gaming"}
    },
    "Meera": {
        "age": 16,
        "subjects": ["Maths", "Science", "English"],
        "marks": (72, 81, 69),
        "hobbies": {"Dancing", "Painting"}
    }
}
students["rohan"] = {"age":18,
                     "subjects":["Maths", "science", "English"],
                     "marks": (88,74,94),
                     "hobbies": {"reading", "gaming"}}

students["Aarav"]["age"] = 18

students["Aarav"]["hobbies"].add("photography")

print("diya second subject",students["Diya"]["subjects"][1])
y = 0
z = 0
marks_total =[]
for name, value in students.items():
    x = 0
    largest = 0
    print("Students name:", name)

    for marks in value["marks"]:
        x += marks
        if marks < 40:
            print("failed",name,marks)
    marks_total.append(x)
    print("Total marks:", x)
    print()
    if x >= z:
        z = x
    y += x
if largest < x:
        largest = x
        print("Topper Student:",name,largest)
print("all total marks list ",marks_total)
print("avg marks",y/5)
