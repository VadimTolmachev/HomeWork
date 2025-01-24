class Human:
    head = True

    def say_hello(self):
        print('Здравствуйте')

class Student(Human):

    def about(self):
        print('Я студент.')

class Teacher(Human):
    pass

student = Student()
teacher = Teacher()

print(student.head)

student.about()

student.say_hello()
teacher.say_hello()