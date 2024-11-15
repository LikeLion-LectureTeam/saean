# 딕셔너리(Dictionaries)

# student = {
#     "student_no": "202301234",
#     "major": "English",
#     "grade": 1
# }

# print(student.get("gpa", "해당 키-값 쌍이 없습니다."))

# print(list(student.keys()))

# print(list(student.values()))


# tech = {
#     "HTML": "Advanced",
#     "JavaScript": "Intermediate",
#     "Python": "Expert",
#     "Go": "Novice"
# }

# for value in tech.values():
#     print(value)

# for key in tech.keys():
#     print(key)

# for key, value in tech.items():
#     print(f'{key} - {value}')


# 중첩(Nesting)

# student_1 = {
#     "student_no": "1",
#     "gpa": "4.3"
# }

# student_2 = {
#     "student_no": "2",
#     "gpa": "3.8"
# }

# students = [student_1, student_2]


# for student in students: 
#     student['graduated'] = False
#     print(student)


# student = {
#     "subjects": ["회계원리", "중국어회화"]
# }

# print(student["subjects"])

# subjects_list = student["subjects"]

# for subject in subjects_list:
#     print(subject)

student = {
    "scholarship": {
        "name": "국가장학금",
        "amount": "1000000"
    }
}

print(student)

# for key in student.keys():
#     print(key)

for value in student.values():
    for value_2 in value.values():
        print(value_2)




















# 추가
# student["gpa"] = 4.5
# print(student)

# # 수정
# student["gpa"] = 4.3
# print(student)

# # 삭제
# del student["grade"]
# print(student)
