import sqlite3

studens = [('Max', 'Brooks', 24, 'Spb'),
           ('John', 'Stones', 15, 'Spb'),
           ('Andy', 'Wings', 45, 'Manhester'),
           ('Kate', 'Brooks', 34, 'Spb'),
           ('Andrew', 'Dolgirev', 42, 'Kazan'),
           ('Maxim', 'Tirinov', 42, 'Kazan')]

courses = [('python', '2021-07-21', '2021-07-21'),
           ('java', '2021-07-13', '2021-07-13')]

student_courses = [(1, 1),
                   (2, 1),
                   (3, 1),
                   (4, 2),
                   (5, 1)]

conn = sqlite3.connect('courses.sqlite')

coursor = conn.cursor()

coursor.execute('DROP TABLE IF EXISTS Students')
coursor.execute('\n'
                '    CREATE TABLE Students( -- таблица студентов\n'
                '    id INTEGER PRIMARY KEY, -- идентификатор студента\n'
                '    name VARCHAR(50), -- имя студента\n'
                '    surname VARCHAR(50), -- фамилия \n'
                '    age INT, -- возраст (полных лет)\n'
                '    city VARCHAR(50) -- город \n'
                '    )')
coursor.executemany("INSERT INTO Students (name,surname,age,city) VALUES (?,?,?,?)", studens)

coursor.execute('DROP TABLE IF EXISTS Courses')
coursor.execute('\n'
                '    CREATE TABLE Courses( -- таблица курсов\n'
                '    id INTEGER PRIMARY KEY, -- идентификатор курса\n'
                '    name VARCHAR(50), -- наименование курса\n'
                '    date_begin DATE, -- дата начала курса \n'
                '    date_end DATE  -- планируемая дата окончания \n'
                '    )')
coursor.executemany("INSERT INTO Courses (name,date_begin,date_end) VALUES (?,?,?)", courses)

coursor.execute('DROP TABLE IF EXISTS Student_courses')
coursor.execute("\n"
                "    CREATE TABLE Student_courses( -- таблица связи студентов и курсов\n"
                "    course_id  INTEGER, -- идентификатор курса\n"
                "    student_id   INTEGER, -- идентификатор курса\n"
                "    FOREIGN KEY (course_id)  REFERENCES Courses (id), \n"
                "    FOREIGN KEY (student_id)  REFERENCES Students (id) \n"
                "    )")
coursor.executemany("INSERT INTO Student_courses (student_id,course_id) VALUES (?,?)", student_courses)

# task №1 (Всех студентов старше 30 лет)
print("№1. Все студенты старше 30 лет:")
coursor.execute("SELECT * FROM Students WHERE age > 30")
print(coursor.fetchall())

# task №2 ( Всех студентов, которые проходят курс по python.)
coursor.execute('''SELECT Students.name,Students.surname \n'''
                '''FROM Students \n'''
                '''JOIN Student_courses ON Student_courses.student_id = Students.id \n'''
                '''JOIN Courses ON Courses.id = Student_courses.course_id \n'''
                '''WHERE Courses.name = 'python' ''')
print("№2. Все студенты, которые проходят курс по python:")
print(coursor.fetchall())

# task №3 (Всех студентов, которые проходят курс по python из Spb.)
coursor.execute('''SELECT Students.name,Students.surname \n'''
                '''FROM Students \n'''
                '''JOIN Student_courses ON Student_courses.student_id = Students.id \n'''
                '''JOIN Courses ON Courses.id = Student_courses.course_id \n'''
                '''WHERE Courses.name = 'python' AND Students.city = 'Spb' ''')

print("№3. Все студенты, которые проходят курс по python из города СПБ:")
print(coursor.fetchall())

conn.commit()
conn.close()

