N = int(input())

class student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students_arr = []

for i in range(N):
    input_student = input().split(" ")
    students_arr.append(student(input_student[0], int(input_student[1])))

students_arr.sort(key= lambda x: x.grade)

for student_info in students_arr:
    print(student_info.name, end=" ")
    
