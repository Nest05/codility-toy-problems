import sqlite3

# Setup the db -> instanciate the database going to be used by us

# method within a class that will allow us to connect to the db



class CourseManagementSystem:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT,
                instructor TEXT    
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                email TEXT    
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            )
        ''')

        self.conn.commit()


    def add_course(self, name, instructor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO courses (name, instructor) VALUES (?, ?)", (name, instructor))
        self.conn.commit()

    def add_student(self, first_name, last_name, email):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
        self.conn.commit()

    def register_student(self, student_id, course_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO registrations (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        self.conn.commit()

    def get_all_courses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()
    
    def get_all_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    
    def get_students_in_a_course(self, course_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students INNER JOIN registrations ON students.id = registrations.student_id WHERE registrations.course_id = ?", (course_id,))
        return cursor.fetchall()

if __name__ == '__main__':
    
    moringa_course_management = CourseManagementSystem("moringa_course_manager.db")


    moringa_course_management.add_course('Software Development', 'Joseph Wambua')
    moringa_course_management.add_course('Character Development', 'Clare Oparo')

    moringa_course_management.add_student("Nestor", "Masinde", "nestor.masinde@gmail.com")
    moringa_course_management.add_student("Naomi", "Lagat", "naomi.lagat@gmail.com")

    moringa_course_management.register_student(1, 1)
    moringa_course_management.register_student(2, 1)
    moringa_course_management.register_student(1, 2)


# print(moringa_course_management.get_all_courses())

print(moringa_course_management.get_students_in_a_course(2))