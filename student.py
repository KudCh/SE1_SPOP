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
from authenticated import Authenticated
from semester import Answer

class Student(Authenticated):

# we have to reinitialize a student when a new semester starts
# Student != Semester

    #a list of student answers to exercises
    record = []
# Progress: contains a pointer to the current day in a semester and a list of ex+student solutions
    def __init__(self, password, name, id, ):
        super().__init__(name, password)
        self.id = id
       # self.exercises = {None:None} 
       # self.progress = [] # semester, semester day, completed exercises with a score 

    # prints exercise task if exerciseID points to an existing exercise
    def openExercise(self, exerciseID, semester):
        exercise = None
        for exID in semester.exercises.keys():
            if exID == exerciseID:
                exercise = semester.exercises[exID]

        if exercise:         
            print(exercise.question)

        return 

    def enterAnswer(self, exerciseID, semesterID):
        answer = input("Please enter your solution:")

        #pre-condition that the exercise exists
        #answerObj = Answer(answer, exerciseID)
        self.record[exerciseID]=answer

        return 

    def printSemester(self, semester):

        for index, exercise in semester.exercises.items():
            status = "to do"
            score = "unknown"
            if exercise.id in self.record.keys():
                status = "done"
                if self.record[exercise.id] == exercise.solution: # assert 1-word replies?
                    score = "correct"
            print(index, "   ", exercise.task,"   ", status, "   ", score, "\n")
