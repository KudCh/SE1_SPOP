from semester import Semester, Day, Exercise
from random import choice
# semester has a state - > calendar that shows what day it is
# program has a timer that counts days in the calendar 

class Administrator():
    
    def __init__(self, id):
        self.id = id
        
    def setStudyPlan(self, exerciseDatabase): #database 

        print("You are setting a study plan for this semester.\n")
        semesterLength = self.setNumberOfExercises()
        exercises = [None]
        for i in range(semesterLength):
            exercises.append(choice(exerciseDatabase))
        calendar = (None, [])

        """
        for i in range(1, semesterLength):
        # add a node to the linked list
            i+=1
        """

        print("Semester with ", semesterLength, " exercises initialized!\n")

        semester = Semester(semesterLength, exercises)

        return semester


    """The function expects an integer input and returns this integer."""
    def setNumberOfExercises(self):

        n = int(input("Enter the number of exercises for this semester: "))

        return n

