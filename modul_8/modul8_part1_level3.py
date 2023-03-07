from peewee import *

conn = SqliteDatabase('courses.sqlite')


class Students(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        table_name = 'Students'
        database = conn


class Courses(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    time_start = CharField(column_name='date_start')
    time_end = CharField(column_name='date_end')

    class Meta:
        database = conn


class StudentCourses(Model):
    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)

    class Meta:
        database = conn
        table_name = 'Student_courses'

# 0. Все студенты
# print("№0. Все студенты старше 30 лет:")
# for student in Students.select():
#     print(student.name)

# task №1 (Всех студентов старше 30 лет)
print("№1. Все студенты старше 30 лет:")
for student in Students.select().where(Students.age > 30):
    print(student.name, student.age)

# task №2 ( Всех студентов, которые проходят курс по python.)
print("№2. Все студенты, которые проходят курс по python:")
for request in Students.select().join(StudentCourses).join(Courses).where(Courses.name == 'python'):
    print(request.name)

# task №3 (Всех студентов, которые проходят курс по python из Spb.)
print("№3. Все студенты, которые проходят курс по python из города СПБ:")
for request in Students.select().join(StudentCourses).join(Courses).where(Courses.name == 'python',Students.city == 'Spb'):
    print(request.name)

conn.close()
