# import classes
from classes import  * # Student, Lecturer ,Reviewer
from my_functions import *

if __name__ == "__main__":

    student1 = Student('Дмитрий','Трисмаков','м')
    student2 = Student('Марат','Мовламов','м')

    lecturer1  = Lecturer('Олег','Булыгин')
    lecturer2  = Lecturer('Елена','Никитина')

    reviewer1 = Reviewer('Александр','Бардин')
    reviewer2 = Reviewer('Олег','Булыгин')

    reviewer1.rate_hw(student1,'Python',9)
    reviewer1.rate_hw(student1,'Python',9)
    reviewer1.rate_hw(student1,'git',5)

    reviewer1.rate_hw(student2,'Python',10)
    reviewer1.rate_hw(student2,'Python',10)
    reviewer1.rate_hw(student2,'git',10)

    student1.grade_lecturer(lecturer1,'Python',10 )
    student1.grade_lecturer(lecturer1,'Python',9 )
    student1.grade_lecturer(lecturer1,'git',10 )
    student1.grade_lecturer(lecturer1,'git',10 )

    student2.grade_lecturer(lecturer1,'Python',10 )
    student2.grade_lecturer(lecturer1,'Python',9 )
    student2.grade_lecturer(lecturer1,'git',10 )

    if  student1 > student2:
        print(f'{student1.name} > {student2.name}\n')
    else:
        print(f'{student1.name} < {student2.name}\n')
    if  student2 > student1:
        print(f'{student2.name} > {student1.name}\n')

    if lecturer1 < lecturer2:
        print(f'{lecturer1.name} < {lecturer2.name}\n')
    else:
        print(f'{lecturer1.name} > {lecturer2.name}\n')

    print( f'Проверяющий: \n{reviewer1}\n')
    print( f'Лектор: \n{lecturer1}\n')
    print( f'Студент: \n{student1}\n')
    print( f'Студент: \n{student2}\n')

    # print(lecturer1.name, lecturer1.grades)
    print(student1.name, student1.grades)
    print(student2.name, student2.grades)
    #
    print(f"Сердний бал по Python у студентов:  {average_grade_student([student1, student2], 'Python')}")
    print( f"Сердний бал по git у студентов: { average_grade_student([student1, student2], 'git')}")

    print(f"Сердний бал по Python у лекторов: { average_grade_lecturer([lecturer1 , lecturer2], 'Python') }")
    print(f"Сердний бал git лекторов: {average_grade_lecturer([lecturer1 , lecturer2], 'git')}")