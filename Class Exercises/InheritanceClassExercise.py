def displayAll(list):
    for item in list:
        item.description()

class Person:
    def __init__(self, name, phonenumber) :
        self.name = name
        self.phonenumber = phonenumber

    def description(self):
        print(f'Name: {self.name} - cell#: {self.phonenumber}')

class Student(Person):
    def __init__(self, name, phonenumber, school):
        super().__init__(name, phonenumber)
        self.school = school

    def description(self):
        Person.description(self)
        print(f'I attend to {self.school}')


class Employee(Person):
    def __init__(self, name, phonenumber, employer):
        super().__init__(name, phonenumber)
        self.employer = employer

    def description(self):
        print(f'Works at {self.employer}')
        Person.description(self)
    

print('Welcome to my phone list')
print('-'*40)
contacts = []
type = input('If you want to enter a person (P)\nIf you want to enter a student (S)\nIf you want to enter an employee (E), to quit (Q):').upper()

while type !='Q':
    
    if type == 'P':
        name = input('Please enter the name:')
        cell = input('Please enter the phone number:')
        person = Person(name, cell)

        contacts.append(person)

    elif type == 'S':
        name = input('Please enter the name:')
        cell = input('Please enter the phone number:')
        school = input('Please enter the school name:')
        student = Student(name, cell, school)

        contacts.append(student)

    elif type == 'E':
        name = input('Please enter the name:')
        cell = input('Please enter the phone number:')
        employer = input('Please enter the work place:')
        employee = Employee(name, cell, employer)

        contacts.append(employee)

    elif type != 'Q':
        print('Invaid selection - please select from one of the following options:')

    type = input('If you want to enter a person (P)\nIf you want to enter a student (S)\nIf you want to enter an employee (E), to quit (Q):').upper()

print('Phone List:')
displayAll(contacts)

print('Thank you for using my phone list.')