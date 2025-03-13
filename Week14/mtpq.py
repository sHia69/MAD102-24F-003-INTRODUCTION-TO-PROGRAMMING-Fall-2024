"""""
Answer any one question (A or B).

A. Design a program to manage memberships at a fitness center. The system should include:

Membership Details: Member name, age, and membership type (e.g., monthly, annual).
Trainer Assignments: Assign trainers to specific members based on their fitness goals.
Workout Schedules: Define workout plans for members, including time slots.
Progress Tracking: Track the progress of each member (e.g., weight loss, muscle gain).
Tasks to Perform:

Add three members with different membership types.
Assign a trainer to each member based on their fitness goal.
Create workout schedules for the members.
Display the member details along with their trainers and workout schedules.

-OR-

B. Create a program to manage events for a community center. The program should include:

Event Details: Name, date, time, and venue.
Organizer Information: Name of the person organizing the event and their contact details.
Attendee Registration: Allow people to register for an event by providing their name and contact number.
Event Summary: Display a list of all events, including the names of the organizers and registered attendees.
Tasks to Perform:

Plan three events with dates and venues.
Add two organizers and link them to the events.
Register five attendees across different events.
Display the list of events with organizers and attendees.
"""
# Answer A: Manage Memberships at Fitness Center
class Member:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.trainer = None
        self.workout_schedule = None
        self.progress = {}

    def assign_trainer(self, trainer):
        self.trainer = trainer

    def set_workout_schedule(self, workout_schedule):
        self.workout_schedule = workout_schedule

    def update_progress(self, metric, value):
        self.progress[metric] = value

    def display_details(self):
        print(f"Member Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Membership Type: {self.membership_type}")
        if self.trainer:
            print(f"Trainer: {self.trainer.name}")
        if self.workout_schedule:
            print(f"Workout Schedule: {self.workout_schedule.schedule}")
        print(f"Progress: {self.progress}")
        print()

class Trainer:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class WorkoutSchedule:
    def __init__(self, schedule):
        self.schedule = schedule

class FitnessCenter:
    def __init__(self):
        self.members = []
        self.trainers = []

    def add_member(self, member):
        self.members.append(member)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def display_all_members(self):
        for member in self.members:
            member.display_details()

# Created fitness center
fitness_center = FitnessCenter()

# Added trainers
trainer1 = Trainer("John Doe", "Weight Loss")
trainer2 = Trainer("Jane Smith", "Muscle Gain")
trainer3 = Trainer("Emily Davis", "Cardio")
fitness_center.add_trainer(trainer1)
fitness_center.add_trainer(trainer2)
fitness_center.add_trainer(trainer3)

# Added members
member1 = Member("Alice", 30, "Monthly")
member2 = Member("Bob", 25, "Annual")
member3 = Member("Charlie", 35, "Monthly")
fitness_center.add_member(member1)
fitness_center.add_member(member2)
fitness_center.add_member(member3)

# Assigning trainers to members
member1.assign_trainer(trainer1)
member2.assign_trainer(trainer2)
member3.assign_trainer(trainer3)

# Created workout schedules
schedule1 = WorkoutSchedule("Mon, Wed, Fri - 6 AM to 7 AM")
schedule2 = WorkoutSchedule("Tue, Thu - 7 AM to 8 AM")
schedule3 = WorkoutSchedule("Mon, Wed, Fri - 8 AM to 9 AM")
member1.set_workout_schedule(schedule1)
member2.set_workout_schedule(schedule2)
member3.set_workout_schedule(schedule3)

# Display member details
fitness_center.display_all_members()

# Answer B: Manage Events for a Community Center
class Event:
    def __init__(self, name, date, time, venue):
        self.name = name
        self.date = date
        self.time = time
        self.venue = venue
        self.organizer = None
        self.attendees = []

    def assign_organizer(self, organizer):
        self.organizer = organizer

    def register_attendee(self, attendee):
        self.attendees.append(attendee)

    def display_details(self):
        print(f"Event Name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Venue: {self.venue}")
        if self.organizer:
            print(f"Organizer: {self.organizer.name} ({self.organizer.contact})")
        print("Attendees:")
        for attendee in self.attendees:
            print(f" - {attendee.name} ({attendee.contact})")
        print()

class Organizer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Attendee:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class CommunityCenter:
    def __init__(self):
        self.events = []
        self.organizers = []

    def add_event(self, event):
        self.events.append(event)

    def add_organizer(self, organizer):
        self.organizers.append(organizer)

    def display_all_events(self):
        for event in self.events:
            event.display_details()

# Create community center
community_center = CommunityCenter()

# Add organizers
organizer1 = Organizer("Alice Johnson", "alice@example.com")
organizer2 = Organizer("Bob Brown", "bob@example.com")
community_center.add_organizer(organizer1)
community_center.add_organizer(organizer2)

# Plan events
event1 = Event("Yoga Class", "2023-11-01", "10:00 AM", "Room A")
event2 = Event("Cooking Workshop", "2023-11-02", "02:00 PM", "Room B")
event3 = Event("Art Exhibition", "2023-11-03", "05:00 PM", "Room C")
community_center.add_event(event1)
community_center.add_event(event2)
community_center.add_event(event3)

# Assign organizers to events
event1.assign_organizer(organizer1)
event2.assign_organizer(organizer2)
event3.assign_organizer(organizer1)

# Register attendees
attendee1 = Attendee("Charlie", "charlie@example.com")
attendee2 = Attendee("David", "david@example.com")
attendee3 = Attendee("Eve", "eve@example.com")
attendee4 = Attendee("Frank", "frank@example.com")
attendee5 = Attendee("Grace", "grace@example.com")
event1.register_attendee(attendee1)
event1.register_attendee(attendee2)
event2.register_attendee(attendee3)
event3.register_attendee(attendee4)
event3.register_attendee(attendee5)

# Display event details
community_center.display_all_events()