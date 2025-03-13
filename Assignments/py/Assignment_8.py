# Author: Hia Al Saleh
# Date: November 15th of the year 2024
# File: Assignment_8.py

# Purpose: Create a Python program with three classes: Employee, Manager, and Project.
# The program should allow the creation of employees, assign managers to projects, and display the project details.

# Requirements:
""" 1. Employee Class:
    Attributes:
    - Name: The name of the employee. 
    - Address: The address of the employee.
    - Salary: The employee's salary.
    - Job Title: The employee's job title.
    Methods:
    - generatingReports: A method that returns a formatted string displaying the employee's name, address, salary, and job title."""

""" 2. Project Class:
    Attributes: 
    - Name: The project name. 
    - Start date (type-date): The project start date. 
    - End date (type-date): The project end date. 
    - Manager (type-Manager): The manager assigned to the project. This must be an instance of the Manager class. 
    - Team members (type-list): A list of Employee instances who are project team members. 
    Methods: 
    - add_team_member(<Team member>): Adds a team member to the project. This member must be an instance of Employee.  
    - get_team_members: Returns a list of all team members assigned to the project with job titles.
    - display_project_details: Returns a formatted string with project name, start and end dates, manager details, and team members' details."""

""" 3. Manager Class (Inherits from Employee):
    Attributes: 
    - Inherits all attributes from Employee with job_title defaulting to "Manager" and being non-editable. 
    - Reportee (type-list): Employees who directly report to the manager should be added to this list based on the project the manager oversees. 
    Methods: 
    - generatingReports: Overrides Employee's method, returns all information about the manager (name, address, salary, and job title), including the list of team members managed by this manager."""

""" 4. Implementation of classes:
    - Create an instance of Manager.  
    - Create a Project instance and assign the project’s manager. (Note: Project should be created with an assigned manager but team members can be added later.)  
    - Create two Employee instances and add them as team members to the project using the “add_team_member(<Team member>)” method. 
    - Display employee details using the “generatingReports” method. 
    - Display the project details using the “display_project_details” & “get_team_members” methods. 
    - Display the manager’s report using the “generatingReports” method. """

# Note: For the Start date & End date (type-date): You can import the “date” from the “datetime” library.

from datetime import date # imported date class from datetime module
import textwrap # imported textwrap module to indent the list of team members


# Employee Class
class Employee:
    def __init__(self, name, address, salary, job_title):
        self.name = name
        self.address = address
        self.salary = salary
        self.job_title = job_title

# Method to generate reports
    def generatingReports(self):
        return (f"Employee Name: {self.name}\n"
                f"Employee Address: {self.address}\n"
                f"Employee Salary: {self.salary}\n"
                f"Employee Job Title: {self.job_title}")
    
# Manager Class
class Manager(Employee):
    def __init__(self, name, address, salary):
        super().__init__(name, address, salary, "Manager")
        self.reportee = []

# Method to generate reports
    def generatingReports(self):
        reportee_list = "\n".join([f"- {reportee.name}, {reportee.job_title}" for reportee in self.reportee])
        return (f"Manager Name: {self.name}\n"
                f"Manager Address: {self.address}\n"
                f"Manager Salary: {self.salary}\n"
                f"Manager Job Title: {self.job_title}\n"
                f"Reportees:\n{textwrap.indent(reportee_list, '    ')}") # Indent the list of reportees
    
# Project Class
class Project:
    def __init__(self, name, start_date, end_date, manager):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.manager = manager
        self.team_members = []

    # Method to add team members
    def add_team_member(self, team_member):
        self.team_members.append(team_member)
        self.manager.reportee.append(team_member)

    # Method to get team members
    def get_team_members(self):
        team_members_list = "\n".join([f"- {member.name}, {member.job_title}" for member in self.team_members])
        return textwrap.indent(team_members_list, '    ') # Indent the list of team members

    # Method to display project details
    def display_project_details(self):
        return (f"Project Name: {self.name}\n"
                f"Project Start Date: {self.start_date}\n"
                f"Project End Date: {self.end_date}\n"
                f"Manager Details:\n{textwrap.indent(self.manager.generatingReports(), '    ')}\n"
                f"Team Members:\n{self.get_team_members()}")

# Created two Employee instances
employee1 = Employee("David A. Thomas", "123 Main Street, Anytown, USA, 12345", 50000, "Software Engineer")
employee2 = Employee("Randy Pausch", "100 Mount Eden Road,Mount Eden,Auckland 5022", 60000, "Software Developer")


# Created an instance of Manager
manager = Manager("John Doe", "456 Elm Street, Suite 3, Los Angeles, CA 90001, USA ", 100000)
# Created a Project instance and assign the project’s manager
project = Project("Project A", date(2024, 11, 1), date(2024, 12, 1), manager)

# Added them as team members to the project
print("=" * 50)
print("❖ Employee Details ❖") # Added ❖ symbol to make it more visible and neat.
project.add_team_member(employee1)
project.add_team_member(employee2)

# Display employee details
print(employee1.generatingReports())
print()
print(employee2.generatingReports())
print("=" * 50)

# Display the project details
print("❖ Project Details ❖")
print(project.display_project_details())
print("=" * 50)

# Display the manager’s report
print("❖ Manager Report ❖")
print(manager.generatingReports())