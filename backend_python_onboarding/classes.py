class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경되었습니다.')

class ForeignStudent(Student):

    def __init__(self, name, major, country):
        super().__init__(name, major)
        self.country = country


    def study(self):
        print(f'{self.name} is studying now')


foreign_stud_1 = ForeignStudent('이테킷', '국어국문학과', '미국')




















# student_1_name = student_1.name
# print(student_1_name)

# student_1_graduated = student_1.is_graduated
# print(student_1_graduated)

# student_1.study()








