# class Student:
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = ['Python','git']
        self.grades = {}

# студенты ставят оценки лекторам
    def grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached :
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def  __average_grade_func(self):
        avrg = 0
        count = 0
        for lst in self.grades.values():
            avrg = avrg + sum(lst)
            count = count + len(lst)
        # tmp = list(self.grades.values())
        if count != 0:
            avrg = avrg / count
        return round(avrg,1)

    def __str__(self):
        return f"Имя: {self.name}  \nФамилия: {self.surname} " \
               f"\nСредняя оценка за домашние задания: {self.__average_grade_func()} " \
               f"\nКурсы в процессе изучения: {', '.join((self.courses_in_progress))}" \
               f"\nЗавершенные курсы: {str(self.finished_courses)}"

    def __gt__(self, other):
        if not isinstance(other,Student):
            print('не Student')
            return
        return self.__average_grade_func() > other.__average_grade_func()

    def __lt__(self, other):
        if not isinstance(other,Student):
            print('не Student')
            return
        return self.__average_grade_func() < other.__average_grade_func()

# class Mentor:
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python','git']

# class Lecturer(Mentor):
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = ['Python','git']
        self.grades = {}
        self.average_grade = 0

    def  __average_grade_func(self):
        avrg = 0
        count = 0
        for lst in self.grades.values():
            avrg = avrg + sum(lst)
            count = count + len(lst)
        if count != 0:
            avrg = avrg / count
        return round(avrg,1)

    def __str__(self):
        return (f"Имя: {self.name}  \nФамилия: {self.surname} \n{self.__average_grade_func()}")
        return

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('не Lecturer')
            return
        return self.__average_grade_func() > other.__average_grade_func()

    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            print('не Lecturer')
            return
        return self.__average_grade_func() < other.__average_grade_func()

#class Reviewer(Mentor):
class Reviewer(Mentor):
    def __str__(self):
        return(f"Имя: {self.name}  \nФамилия: {self.surname}" )

# проверяющие cтавят оценки студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'