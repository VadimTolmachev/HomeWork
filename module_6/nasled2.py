# Множественное наследование. Метод Super
# Функция super() используется для вызова методов родительского класса из дочернего

# принцип DRY (Don’t Repeat Yourself) - не повторятся
# Почему избегают дублирования кода?
# 1) Упрощение поддержки: изменения в коде базового класса автоматически распространяются на все дочерние классы.
# 2) Читаемость: меньше кода — легче читать и понимать структуру программы.
# 3) Расширяемость: при необходимости можно добавлять новые атрибуты и методы в базовый класс,
# минимизируя изменения в дочерних классах.

# множественное наследование, миксины (Mixins) — вспомогательные классы, добавляющие функционал,
# но не предназначенные для создания отдельных объектов.
# При множественном наследовании важно учитывать иерархию наследования, также известную как цепочка наследования
# Правило приоритетов:
# Класс, указанный слева, имеет более высокий приоритет.
# важный момент в использовании множественного наследования: 
# super() следует цепочке наследования MRO и вызывает следующий класс по порядку.

class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)

    def info(self):
        print(f'Привет меня зовут {self.name}')

class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')

class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()

# human = Human('Вадим')
student = Student('Денис', 'Урбант', 'python 0')
# print(human.name)
# print(student.name)
# human.info()
# student.info()
student.about()
print(Human.mro())
print(Student.mro())