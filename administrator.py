class Administrator():
    
    def __init__(self, id):
        self.id = id
        
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