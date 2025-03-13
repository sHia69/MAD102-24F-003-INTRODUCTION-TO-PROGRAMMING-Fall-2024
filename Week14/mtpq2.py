"""
Answer any one question (A or B).

A. Write a program for managing a library's borrowing system. The program should support:

Book Information: Title, author, and the number of available copies.
Member Records: Member name, contact information, and borrowed books.
Borrowing System: Allow members to borrow and return books.
Status Report: Display the list of borrowed books, along with the member names and due dates.
Tasks to Perform:

Add details for three books and their available copies.
Register two library members.
Process the borrowing of books and update availability.
Display the borrowing status and remaining available books.

-OR-

B. Develop a program to manage a school timetable. The program should allow for the following:

Teacher Details: Store information like name, subject specialization, and availability.
Student Information: Keep track of student names, grades, and enrolled subjects.
Timetable Creation: Assign teachers to specific time slots and subjects, ensuring no conflicts in availability.
Display Timetable: Generate a timetable showing subjects, teacher names, and allocated time slots.
Tasks to Perform:

Create entries for at least two teachers and their availability.
Add details for three students and their enrolled subjects.
Assign teachers to subjects and display the timetable.
Show a list of students enrolled in each subject.
"""
# Answer A: Managing a Library's Borrowing System
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class Member:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.borrowed_books = {}

    def borrow_book(self, book, due_date):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books[book.title] = due_date
        else:
            print(f"No copies of {book.title} available.")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.copies += 1
            del self.borrowed_books[book.title]
        else:
            print(f"{self.name} has not borrowed {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def display_borrowing_status(self):
        for member in self.members:
            print(f"Member: {member.name}")
            for book_title, due_date in member.borrowed_books.items():
                print(f"  Borrowed Book: {book_title}, Due Date: {due_date}")
        print()

    def display_available_books(self):
        for book in self.books:
            print(f"Book: {book.title}, Author: {book.author}, Available Copies: {book.copies}")
        print()

# Create library
library = Library()

# Add books
book1 = Book("1984", "George Orwell", 3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register members
member1 = Member("Alice", "alice@example.com")
member2 = Member("Bob", "bob@example.com")
library.register_member(member1)
library.register_member(member2)

# Process borrowing
due_date = datetime.now() + timedelta(days=14)
member1.borrow_book(book1, due_date)
member2.borrow_book(book2, due_date)
member1.borrow_book(book3, due_date)

# Display borrowing status and available books
library.display_borrowing_status()
library.display_available_books()

# Answer B: Managing a School Timetable

class Teacher:
    def __init__(self, name, subject, availability):
        self.name = name
        self.subject = subject
        self.availability = availability

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.enrolled_subjects = []

    def enroll_subject(self, subject):
        self.enrolled_subjects.append(subject)

class Timetable:
    def __init__(self):
        self.schedule = {}

    def assign_teacher(self, subject, teacher, time_slot):
        if time_slot not in self.schedule:
            self.schedule[time_slot] = {}
        if subject not in self.schedule[time_slot]:
            self.schedule[time_slot][subject] = teacher
        else:
            print(f"Conflict: {subject} already assigned to {self.schedule[time_slot][subject].name} at {time_slot}")

    def display_timetable(self):
        for time_slot, subjects in self.schedule.items():
            print(f"Time Slot: {time_slot}")
            for subject, teacher in subjects.items():
                print(f"  Subject: {subject}, Teacher: {teacher.name}")
        print()

    def display_students_per_subject(self, students):
        subject_students = {}
        for student in students:
            for subject in student.enrolled_subjects:
                if subject not in subject_students:
                    subject_students[subject] = []
                subject_students[subject].append(student.name)
        for subject, student_names in subject_students.items():
            print(f"Subject: {subject}, Students: {', '.join(student_names)}")
        print()

# Created timetable
timetable = Timetable()

# Added teachers
teacher1 = Teacher("Mr. Smith", "Math", ["Mon 9 AM", "Wed 9 AM"])
teacher2 = Teacher("Ms. Johnson", "Science", ["Tue 10 AM", "Thu 10 AM"])

# Added students
student1 = Student("Alice", "Grade 10")
student2 = Student("Bob", "Grade 10")
student3 = Student("Charlie", "Grade 10")

# Enrolled students in subjects
student1.enroll_subject("Math")
student2.enroll_subject("Science")
student3.enroll_subject("Math")
student3.enroll_subject("Science")

# Assigned teachers to subjects
timetable.assign_teacher("Math", teacher1, "Mon 9 AM")
timetable.assign_teacher("Science", teacher2, "Tue 10 AM")

# Display timetable
timetable.display_timetable()

# Display students per subject
timetable.display_students_per_subject([student1, student2, student3])