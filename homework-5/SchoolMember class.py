#!/usr/bin/env python3.6


class SchoolMember:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print('(Создан {0}: {1})'.format(type(self).__name__, self.name))

    def show(self):
        """ Print all information about
        class isinstance.

        :returns: None.
        """
        print("Имя: {0} Возраст: {1} Зарплата: {2}"
              .format(self.name, self.age, self.salary))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        super().__init__(name, age, salary)


class Student(SchoolMember):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        super().__init__(name, age, salary)

if __name__ == '__main__':
    persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]
    for person in persons:
        person.show()
