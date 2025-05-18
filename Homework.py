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

    def rate_lecturer(self, lecturer, course, grade):   #Реализация функции оценки лекторов от студентов
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):    #Функция нахождения средней оценки студента
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

    def get_average_grade(self):   #Функция нахождения средней оценки лектора
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

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)

some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 9)

print(some_reviewer)
print(some_lecturer)
print(some_student)