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


for student in Students.select():
    print(student.name)

conn.close()
