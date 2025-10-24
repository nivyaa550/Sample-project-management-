# main.py - Student Grade Calculator

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

print("Student Grade Calculator")

marks = []
for i in range(3):
    m = float(input(f"Enter mark {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / len(marks)

print(f"Total Marks: {total}")
print(f"Average: {average}")
print(f"Grade: {calculate_grade(average)}")
