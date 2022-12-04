"""
    15/11/22
    Kristina Kudryavtseva, kristina.kudryavtseva.001@student.uni.lu
    SPOP main file

    The program is an exercise platform for students.
    The program accomodates two types of users: schools, students.
    Schools set the study plan for each semester.
    Students solve the exercises, are evaluated and ranked based on their solutions.

    This file contains the Semester class.

"""

# does a Semester instance depend on a student or vice versa?
# a pointer to the current day - in Semester or in Student
class Semester():

    def __init__(self, length, calendar):
        self.length = length
        self.calendar = calendar # calendar is a linked list of days 

class Exercise():

    def __init__(self, question, solution, level):
        self.question = question
        self.solution = solution
        self.level = level

class Day():

    def __init__(self, id, exercise):
        self.id = id
        self.exercise = exercise
        self.next = None # last day in the calendar