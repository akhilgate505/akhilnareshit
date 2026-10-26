# Program 2: Student marks and result
# All data and calculations are inside this file.

student_name = "Ravi"
marks = [80, 75, 90, 68, 85]

total = sum(marks)
average = total / len(marks)

print("STUDENT REPORT")
print("Student name:", student_name)
print("Marks:", marks)
print("Total marks:", total)
print("Average marks:", round(average, 2))

if all(mark >= 35 for mark in marks):
    print("Result: Pass")
else:
    print("Result: Fail")
