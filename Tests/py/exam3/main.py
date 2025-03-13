# Question 11 B.
# Purpose: Design a program to manage course registrations for a university.
# The system manages student information, course details, and allows for course registration with capacity checks.

# Student Details Class
class StudentDetails:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses_enrolled = [] 

    def enroll_in_course(self, course):
        if course.register_student(self):  
            self.courses_enrolled.append(course)
        else:
            print(f"Error: Cannot enroll {self.name} in {course.course_name}. Course is full.")

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Courses Enrolled: {', '.join(course.course_name for course in self.courses_enrolled)}")

# Course Details Class
class CourseDetails:
    def __init__(self, course_name, course_code, instructor, max_capacity):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_students = []  # List to store students enrolled in this course

    def register_student(self, student):
        if len(self.enrolled_students) < self.max_capacity:
            self.enrolled_students.append(student)
            return True  # Successfully enrolled
        else:
            return False  # Course full, registration failed

    def display_info(self):
        print(f"\nCourse Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Max Capacity: {self.max_capacity}")
        print(f"Enrolled Students: {len(self.enrolled_students)}")
        print(f"List of Enrolled Students: {', '.join(student.name for student in self.enrolled_students)}")

# Example usage
def main():
    # Create courses with different instructors and capacities
    course1 = CourseDetails("Java Programming", "MAD100", "Dr. Smith", 2)
    course2 = CourseDetails("Intro to Python", "MAD102", "Dr. Johnson", 2)
    course3 = CourseDetails("HTML & CSS", "WEB110", "Dr. Davis", 2)

    # Create students
    student1 = StudentDetails("John", "0928456")
    student2 = StudentDetails("Julia", "0948542")

    # Enroll students in courses
    student1.enroll_in_course(course1)
    student1.enroll_in_course(course2)
    
    student2.enroll_in_course(course2)
    student2.enroll_in_course(course3)

    # Attempt to enroll a student in a full course
    student1.enroll_in_course(course3)  # Should fail, as course3 has a max capacity of 2

    # Display student information
    student1.display_info()
    student2.display_info()

    # Display course information
    course1.display_info()
    course2.display_info()
    course3.display_info()

if __name__ == "__main__":
    main()