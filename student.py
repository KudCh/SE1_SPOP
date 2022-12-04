"""
    15/11/22
    Kristina Kudryavtseva, kristina.kudryavtseva.001@student.uni.lu
    SPOP main file

    The program is an exercise platform for students.
    The program accomodates two types of users: schools, students.
    Schools set the study plan for each semester.
    Students solve the exercises, are evaluated and ranked based on their solutions.

    This file contains the Student class and corresponding functions,
    which expect user input from the student actor.

"""

from school import School

class Student:
    exercises = []
    score = None

# we have to reinitialize a student when a new semester starts
# Student != Semester

# Progress: contains a pointer to the current day in a semester and a list of ex+student solutions
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Possibly useless
    """
    def study(self):

        print(self.name, "is solving exercises")

        for exercise in self.exercises.keys():
            self.openExercise(exercise)
            studentSolution = self.enterSolution()

            self.exercises[exercise] = studentSolution # wrong. we can evaluate automatically and store the score
    """

    # prints exercise task
    def openExercise(self, exercise):
        print(exercise[0], " ?")
        return exercise[0]


    def enterSolution(self):
        solution = input("Please enter your solution:")
        return solution