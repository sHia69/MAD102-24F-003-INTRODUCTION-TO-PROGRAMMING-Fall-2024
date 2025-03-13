# Author: Hia Al Saleh
# Date: November 22nd of the year 2024
# File: Assignment_9.py

"""
Purpose: Answer the following questions:

Question 1: Get Values from a List Based on Index (5 Marks)
Objective:
To develop a Python function that retrieves values from a predefined list using an index provided by
the user, ensuring robust exception handling for invalid inputs or operations.

Requirements:
1. IndexError: If the index is out of range, an IndexError should be caught, and an appropriate
   message should be displayed.
2. ValueError: If the user provides a non-integer input for the index, a ValueError should be raised
   and handled.
3. The function should only accept valid indices and provide meaningful feedback for incorrect
   inputs.
"""

"""
Question 2: Online Course Enrollment System (15 Marks)
Objective:
To develop an online course enrollment system. The system will allow students to enroll in courses,
but the program must ensure that the user input (email, course code chosen, and number of
courses) is valid.

Requirements:
1. The user is asked to input their name, email, and the number of courses they wish to enroll in.
2. Then the user is asked to choose the course from the list of courses offered.
3. The program should handle the below exceptions:
   - TypeError: If the number of courses is not a valid integer, raise a TypeError with the
     message: "Please enter a valid number for courses."
   - ValueError: If the number of courses is less than or equal to zero, raise a ValueError with
     the message: "You must enroll in at least one course."
4. Custom Exception for validating email: Used to ensure that the email validation specifically
   checks for the domain @stclaircollege.ca and to check if the email contains only alphanumeric
   characters before the @. Program should raise an error if the email is not valid.
5. Custom Exception for invalid course code: Validate the course code chosen for enrollment, if
   the course code selected by the student is not offered raise an error message.
6. After successful enrollment, display a message showing the student's name, email, and the
   number of courses they are enrolled in.
7. Handle any unexpected exceptions that may occur and display a generic error message.

Steps to be implemented in the program:
1. Write a function enroll_student that takes user inputs and processes the enrollment.
2. Create a dictionary of courses offered by the organization (course code as key and course name
   as value), for example:
   offered_courses = {
       "MAD102": "Introduction to Computer Science",
       "MAD103": "Data Fundamentals",
       "MAD100": "Java Programming 1",
       "MIT211": "System configuration",
       "MAD155": "Introduction to Linux"
   }
3. The program should handle TypeError and ValueError for invalid numbers of courses they like
   to choose.
4. The program needs to confirm if the student's selected course code is from one of the
   organization's courses. The application should notify the user to choose an appropriate course
   code from the available course list if the user inputs an invalid course code.
5. Validate the email ID to ensure that the email validation specifically checks for the domain
   @stclaircollege.ca and allows only alphanumeric characters before the @.
6. The maximum number of courses a student can enroll is 4.
7. Ensure all exception handling is robust and print the student's enrollment information after
   successful input.
"""

# Question 1: Get Values from a List Based on Index (5 Marks)

# Function to get values from a predefined list based on user input index
def get_values_from_list():
     predefined_list = [10, 20, 30, 40, 50]
     try:
          index = int(input("Enter the index to retrieve value: "))
          value = predefined_list[index]
          print(f"Value at index {index} is {value}")
     except IndexError:
          print("Index out of range. Please enter a valid index.")
     except ValueError:
          print("Invalid input. Please enter an integer.")

# Question 2: Online Course Enrollment System (15 Marks)

# Custom Exception Classes
class InvalidEmailError(Exception):
     pass
 
class InvalidCourseCodeError(Exception):
     pass

# Student and Course Classes
class Student:
    # Student class with first name, last name, email, and courses enrolled
     def __init__(self, first_name, last_name, email):
          self.first_name = first_name
          self.last_name = last_name
          self.email = email
          self.courses = []
    # Function to enroll a student in a course
     def enroll(self, course):
          self.courses.append(course)

class Course:
    # Course class with course code, course name, and credit hours
     def __init__(self, course_code, course_name, credit_hours):
          self.course_code = course_code
          self.course_name = course_name
          self.credit_hours = credit_hours

# Function to validate email format
def validate_email(email):
     if not email.endswith("@stclaircollege.ca") or not email.split('@')[0].isalnum():
          raise InvalidEmailError("Invalid email. Please use a valid @stclaircollege.ca email address.")
# Function to enroll a student in courses
def enroll_student():
     offered_courses = {
          "MAD102": "Introduction to Computer Science",
          "MAD103": "Data Fundamentals",
          "MAD100": "Java Programming 1",
          "MIT211": "System configuration",
          "MAD155": "Introduction to Linux"
     }

     print("Welcome to the Online Course Enrollment System!")
     # Input student details and enroll in courses
     try:
          first_name = input("Enter your first name: ")
          last_name = input("Enter your last name: ")
          email = input("Enter your email: ")
          validate_email(email)
          
          num_courses = int(input("Enter the number of courses you wish to enroll in (max 4): "))
          if num_courses <= 0:
                raise ValueError("You must enroll in at least one course.")
          if num_courses > 4:
                raise ValueError("You can enroll in a maximum of 4 courses.")
          
          student = Student(first_name, last_name, email)
          
          print("Available Courses:")
          print("-" * 20)
          for code, name in offered_courses.items():
                print(f"{code}: {name}")
          
          for i in range(num_courses):
                while True:
                     course_code = input(f"Enter the course code for course {i + 1}: ")
                     if course_code in offered_courses:
                          course = Course(course_code, offered_courses[course_code], 3)  # Assuming 3 credit hours for simplicity
                          student.enroll(course)
                          break
                     else:
                          print("Invalid course code. Please choose a valid course code.")
          
          print("\nEnrollment Successful!")
          print("-" * 20)
          print(f"Student Name: {student.first_name} {student.last_name}")
          print(f"Student Email: {student.email}")
          print(f"Number of Courses: {num_courses}")
          print("Courses Enrolled:")
          for course in student.courses:
                print(f"- {course.course_name}")
          print("Enrollment process is completed. Thank You!")
     
     except InvalidEmailError as e:
          print(e)
     except ValueError as e:
          print(e)
     except TypeError:
          print("Please enter a valid number for courses.")
     except Exception as e:
          print(f"An unexpected error occurred: {e}")

# Main Function
if __name__ == "__main__":
     get_values_from_list()
     enroll_student()