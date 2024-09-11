# from abc import ABC
# from School import School
#
# class User(ABC):
#     def __init__(self,user_id,name,role):
#         self.id = user_id
#         self.name = name
#         self.role = role
#
#     def display_user_details(self):
#         return f'User details :\nID = {self.id}\nName = {self.name}\nRole = {self.role}'
#
#
# class Student(User):
#     def __init__(self, user_id: int, name: str):
#         super().__init__(user_id, name, "student")
#         self.id = user_id
#         self.name = name
#         self.marks = []
#
#     def total_grades(self):
#         if self.marks:
#             return sum(self.marks)
#         return -1
#
#     def average_grades(self):
#         mark_sum = self.total_grades()
#         if mark_sum == -1:
#             print("Mark List Not Added!")
#             return 0
#
#         no_of_subjects = len(self.marks)
#         average_mark = mark_sum/no_of_subjects
#         return average_mark
#
#     def student_details(self):
#         marks = self.average_grades()
#         return (f'Student details : \nID = {self.id}\nName = {self.name}\nAverage Mark = {marks}'
#                 f'\nGrade = {self.find_grade(marks)}')
#
#     @staticmethod
#     def find_grade(grade: float):
#         if grade>90:
#             return "A"
#         elif grade>80:
#             return "B"
#         elif grade>70:
#             return "C"
#         elif grade>60:
#             return "D"
#         elif grade>50:
#             return "E"
#         elif grade == 0:
#             return "Not Calculated"
#         else:
#             return "F"
#
#
# class MarkListNotAddedError(Exception):
#     pass
#
#
#
# class Faculty(User):
#     def __init__(self, user_id, name):
#         super().__init__(user_id, name,'faculty')
#         self.students = []
#
#     @staticmethod
#     def add_student_mark(student_id : int ,school : School,mark_list : list[int]):
#         student : Student = school.find_student_by_id(student_id)
#         student.marks = mark_list
#         return "Mark List Added Successfully"
#
#
# s = Student(1,"joel")
# print(s.student_details())
#
#
#
#
#
#
#
#
