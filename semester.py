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
    def __init__(self):
        self.length = 0
        self.exercises = {} 
        self.id = None

# exercises = {1:Exercise}
    def print(self):
        for index, exercise in exercises.items():
            print(index, "   ", exercise.id, "\n") #exercise ID is exercise name


class Exercise():
    def __init__(self, task, solution, Id): 
        self.task = task
        self.solution = solution
        self.id = Id

    def print(self):
        print(self.id) # is id the name or just ID ? or a tuple of (int,str)
        print(self.task)
        print(self.solution)


class Answer:
    
    def __init__(self, answer, exerciseID):
        self.studentAnswer = answer
        self.exerciseID = exerciseID