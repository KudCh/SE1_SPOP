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
from authenticated import Authenticated

#task = input("Please enter the task:")
#solution = input("Please enter the solution:")

#semesterId = 1

#semesters = []
#current_semester = Semester() 

class School(Authenticated):
    """user_goal
       reuse: setNumberOfExercises(), addExercise()
    """
    def __init__(self, name, password, id):
        super().__init__(name, password)
        self.id = id
    #  self.name = name
    #  self.id = id

    def initNewSemester(self):
        semester = Semester()
        numberOfEx = self.setNumberOfExercises()
        semester.length = numberOfEx
        semester.id = input("Please enter the semester ID: ")

        for i in range(semester.length):
            self.addExercise(semester)

        return semester

    def setNumberOfExercises(self):

        num = int(input("Enter how many exercises you'd like to add: "))
        if isinstance(num, int)and num>0:
            return num
        else:
            return 0

    """The fucntion expects two strings that correspond to an exercise task and a solution."""
    def addExercise(self, semester, id=0):

        task = input("Please enter exercise task: ")
        solution = input("Please enter exercise solution: ")

        exercise = Exercise(task, solution, id)
        semester.exercises[len(semester.exercises)] = exercise

        return exercise

    def deleteExercise(self, exerciseID, semester):
        semester.exercises.pop(exerciseID)
        return 

    def printSemester(self, semester):

        for index, exercise in semester.exercises.items():
            print(index, "   ", exercise.task, "\n") #exercise ID is exercise name
        return

    def giveFeedbackToStudent(student):
        return