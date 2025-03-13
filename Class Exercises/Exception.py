"""Create a program that will handle looking up student’s grades
•The grades will be part of a dictionary – with the student’s name as the keys, 
and the courses and grades as a dictionary of values
•Provide appropriate error handling in case the user asks for a student that 
does not have any grades"""

# Define the dictionary with students' grades
grades = {
    "Alice": {"Math": "A", "Science": "B+"},
    "Bob": {"Math": "B", "History": "A-"},
    "Charlie": {"Science": "A", "History": "B"}
}

def get_student_grades(student_name):
    try:
        # Attempt to retrieve the student's grades
        student_grades = grades[student_name]
        return student_grades
    except KeyError:
        # Handle the case where the student does not exist
        return f"No grades found for student: {student_name}"

# Example usage
student_name = input("Enter the student's name: ")
print(get_student_grades(student_name))