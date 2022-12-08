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

from semester import Semester, Exercise

class School:
    """user_goal
       reuse: setNumberOfExercises(), addExercise()
    """
    def __init__(self, name, id=None):
      self.name = name
    #  self.id = id

    """The fucntion expects two strings that correspond to an exercise task and a solution."""
    def addExcercise(self, exerciseDatabase):

        print("~~~You are adding a new exercise~~~")
        task = input("Please enter the task:")
        solution = input("Please enter the solution:")
        print("\n")
        exercise = Exercise(task, solution, self.id)

        return exercise

    def evaluateStudent(student):

        studentRecord = student.progress

        for exercise in studentRecord.keys():
            studentAnswer = studentRecord[exercise]
            if isinstance(studentAnswer, str):
                if exercise.solution == studentAnswer:
                    studentRecord[exercise] = 1
                else:
                    studentRecord[exercise] = 0

        student.score = sum(studentRecord.values())

        print(student.name, "'s score is ", student.score)

        return