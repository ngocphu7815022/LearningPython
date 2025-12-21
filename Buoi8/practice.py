class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        return f"Tên: {self.name}, điểm: {self.score}"

    def is_passed(self):
        if self.score >= 5:
            return True
        else:
            return False


student_obj = Student("Phú", 10)
student_obj1 = Student("John", 2)

print(student_obj.display_info())
print(student_obj.is_passed())

print(student_obj1.display_info())
print(student_obj1.is_passed())
