# import main
from classes import *

def average_grade_student(students , course):
    if len(students):
        sum_ = 0
        for student in students:
            if isinstance(student, Student) and student.grades and course in student.grades:
                sum_ = sum_ + sum(student.grades[course])
                # print((student.grades[course]))
        return sum_ / len(students)
    else:
        return 0

def average_grade_lecturer(lecturers , course):
    if  len(lecturers):
        sum_ = 0
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and lecturer.grades and course in lecturer.grades:
                sum_ = sum_ + sum(lecturer.grades[course])
        return sum_ / len(lecturers)
    else:
        return 0