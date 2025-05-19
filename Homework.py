class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__ (self): #Перегружаем магический метод __str__
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __eq__(self, other):    #Магический метод сравнения "=="
        if isinstance(other, Student):
            return self.get_average_grade()==other.get_average_grade()
        return NotImplemented

    def __ne__(self, other):    #Магический метод сравнения "!="
        if isinstance(other, Student):
            return self.get_average_grade()!=other.get_average_grade()
        return NotImplemented

    def __lt__(self, other):    #Магический метод сравнения "<"
        if isinstance(other, Student):
            return self.get_average_grade()<other.get_average_grade()
        return NotImplemented

    def __gt__(self, other):    #Магический метод сравнения ">"
        if isinstance(other, Student):
            return self.get_average_grade()>other.get_average_grade()
        return NotImplemented

    def __le__(self, other):    #Магический метод сравнения "<="
        if isinstance(other, Student):
            return self.get_average_grade()<=other.get_average_grade()
        return NotImplemented

    def __ge__(self, other):    #Магический метод сравнения ">="
        if isinstance(other, Student):
            return self.get_average_grade()>=other.get_average_grade()
        return NotImplemented

    def rate_lecturer(self, lecturer, course, grade):   #Реализация функции оценки лекторов от студентов
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):    #Функция нахождения средней оценки для студента
        all_grades=[]
        for course, grade_list in self.grades.items():
            all_grades.extend(grade_list) 
        if not all_grades:
            return "Ошибка"
        return sum(all_grades)/len(all_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


#Добавлены дочерние классы для родительского класса Mentor:
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):   #Функция нахождения средней оценки для лектора
        all_grades = []
        for course, grade_list in self.grades.items():
            all_grades.extend(grade_list)
        if not all_grades:
            return "Ошибка"
        return sum(all_grades)/len(all_grades)

    def __str__ (self): #Перегружаем магический метод __str__
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_average_grade()}\n')

    def __eq__(self, other):    #Магический метод сравнения "=="
        if isinstance(other, Lecturer):
            return self.get_average_grade()==other.get_average_grade()
        return NotImplemented

    def __ne__(self, other):    #Магический метод сравнения "!="
        if isinstance(other, Lecturer):
            return self.get_average_grade()!=other.get_average_grade()
        return NotImplemented

    def __lt__(self, other):    #Магический метод сравнения "<"
        if isinstance(other, Lecturer):
            return self.get_average_grade()<other.get_average_grade()
        return NotImplemented

    def __gt__(self, other):    #Магический метод сравнения ">"
        if isinstance(other, Lecturer):
            return self.get_average_grade()>other.get_average_grade()
        return NotImplemented

    def __le__(self, other):    #Магический метод сравнения "<="
        if isinstance(other, Lecturer):
            return self.get_average_grade()<=other.get_average_grade()
        return NotImplemented

    def __ge__(self, other):    #Магический метод сравнения ">="
        if isinstance(other, Lecturer):
            return self.get_average_grade()>=other.get_average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):  #Адаптация функции rate_hw для Reviewer
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__ (self): #Перегружаем магический метод __str__
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses += ['Введение в программирование']


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python','Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python','Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)

some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 9)

print(some_reviewer)
print(some_lecturer)
print(some_student)

# Для задания №4 Создаю по 2 экземпляра студентов:
student1 = Student("Alice", "Smith", "female")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]

student2 = Student("Bob", "Brown", "male")
student2.courses_in_progress = ["Python", "Git"]
student2.finished_courses = ["Основы ООП"]

# Для задания №4 Создаю по 2 экземпляра лекторов:
lecturer1 = Lecturer("John", "Doe")
lecturer1.courses_attached = ["Python", "Git"]

lecturer2 = Lecturer("Jane", "Doe")
lecturer2.courses_attached = ["Python", "Git"]

# Для задания №4 Создаю по 2 экземпляра проверяющих:
reviewer1 = Reviewer("Mike", "Johnson")
reviewer1.courses_attached = ["Python", "Git"]

reviewer2 = Reviewer("Emma", "Wilson")
reviewer2.courses_attached = ["Python", "Git"]

# Проверяю методы выставления оценок
# Студенты оценивают лекторов:
student1.rate_lecturer(lecturer1, "Python", 10)
student1.rate_lecturer(lecturer2, "Git", 9)
student2.rate_lecturer(lecturer1, "Python", 8)
student2.rate_lecturer(lecturer2, "Git", 6)

# Проверяющие оценивают студентов:
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Git", 9)
reviewer2.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Git", 7)

# Вызываю магические и другие методы:
print("_"*47)
print("Информация о проверяющих:")
print(reviewer1)
print(reviewer2)

print("_"*47)
print("Информация о лекторах:")
print(lecturer1)
print(lecturer2)

print("_"*47)
print("Информация о студентах:")
print(student1)
print(student2)

print("_"*47)
print("Сравнение студентов:")
print("student1 > student2:", student1 > student2)
print("student1 == student2:", student1 == student2)
print("student1 <= student2:", student1 <= student2)

print("_"*47)
print("Сравнение лекторов:")
print("lecturer1 < lecturer2:", lecturer1 < lecturer2)
print("lecturer1 != lecturer2:", lecturer1 != lecturer2)
print("lecturer1 >= lecturer2:", lecturer1 >= lecturer2)

print("_"*47)
print("Средние оценки студентов:")
print(f"Студент {student1.name}: {student1.get_average_grade()}")
print(f"Студент {student2.name}: {student2.get_average_grade()}")

print("_"*47)
print("Средние оценки лекторов:")
print(f"Лектор {lecturer1.name}: {lecturer1.get_average_grade()}")
print(f"Лектор {lecturer2.name}: {lecturer2.get_average_grade()}")