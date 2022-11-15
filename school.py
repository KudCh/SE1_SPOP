"""
    15/11/22
    Kristina Kudryavtseva, kristina.kudryavtseva.001@student.uni.lu
    SPOP main file

    The program is an exercise platform for students.
    The program accomodates two types of users: schools, students.
    Schools set the study plan for each semester.
    Students solve the exercises, are evaluated and ranked based on their solutions.

    This file contains the School class and corresponding functions,
    which requires user input from the school actor.

"""

from semester import Semester


class School:
    """user_goal
       reuse: setNumberOfExercises(), addExercise()
    """
    def __init__(self, name):
      self.name = name

    """The function populates a semester of length n
       with n exercises based on the input of the school actor.
    """
    def setStudyPlan(self):

        print(self.name.upper(), "sets the study plan this semester.\n")
        semesterLength = self.setNumberOfExercises()
        exercises = []

        i = semesterLength
        while(i):
            print(i, "exercises need(s) to be added\n")
            exercises.append(self.addExcercise())
            i -= 1

        print("Semester with ", semesterLength, " exercises initialized!\n")

        semester = Semester(semesterLength, exercises)

        return semester


    """The function expects an integer input and returns this integer."""
    def setNumberOfExercises(self):

        n = int(input("Enter the number of exercises for this semester: "))

        return n

    """The fucntion expects two strings that correspond to an exercise task and a solution."""
    def addExcercise(self):

        print("~~~You are adding a new exercise~~~")
        task = input("Please enter the task:")
        solution = input("Please enter the solution:")
        print("\n")
        ex = (task, solution)

        return ex