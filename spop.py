"""
    15/11/22
    Kristina Kudryavtseva, kristina.kudryavtseva.001@student.uni.lu
    SPOP main file

    The program is an exercise platform for students.
    The program accomodates two types of users: schools, students.
    Schools set the study plan for each semester.
    Students solve the exercises, are evaluated and ranked based on their solutions.

    Thsi file must be executed in order to run the program.
    This file contains the runAndDeploy() function needed to deploy and run the system,
    as well as the student evaluation function evaluateStudent().

"""

# tasks 
# implement eoExplore - student can view score, student has a score variable associated with them 



from school import School
from semester import Exercise, Semester
from student import Student
from interface import * 

accounts = {}

accounts[1] = Student(password="pass123", name="Kristina", id = 1)
accounts[2] = School(password="pass234", name="Awesome School", id =2)

print(accounts)
#a database of IDs, each id points to username-password pair 


""" The function initializes a school instance,
    initializes the semester instance and a student instance,
    evaluates the student.
"""

def runAndDeploy():

    state = State()
    interface = userInterface(state, accounts)
    interface.login()
    actor = accounts[interface.state.loggedInID]
    while(True):
        menu = interface.menu(state.mode)
        choice = interface.getUsrChoice()
        move = interface.moveTo(choice, actor, actionlist=menu)

        if interface.state.action == "Log Out":
            break

    print("Your session ended.")
    return

""" The function takes an instance of class Student as a parameter
    and returns the student's score based on their solutions to the exercises."""

# execution of the program
runAndDeploy()
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

from school import School
from student import Student

class State:

    def __init__(self):
        self.loggedInID = 0
        self.mode = None
        self.semester = None
        self.exerciseID = 0
        self.action = None
        
class userInterface:

    def __init__(self, state, accounts):
        self.state = state
        self.accounts = accounts #account dictionary
        return

    def login(self):

        username = input("Username: ")
        password = input("Password: ")
        credentials = (username, password)
        loggedInID = None
        role = None

        for ID in self.accounts.keys():
            if self.accounts[ID].username == username and self.accounts[ID].password == password:
                loggedInID = ID
                if isinstance(self.accounts[ID], Student):
                    role = "Student"
                else:
                    role = "School"
                print("Welcome to your ",role," account.")
                print("You are loggen in as ", username)
            else: 
                print("An account with such credentials does not exist")        

        self.state.loggedInID = loggedInID
        self.state.mode = role    

        return 

    def logout(self):
        print("You are logged out.")
        #role, loggedInID = None, None 
        self.state.mode = None
        self.state.loggedInID = 0
        return 


    def menu(self, mode): #not only print
        actionlist = {}
        if mode == "School":
            if self.state.semester == None: 
                print("No semester is currently in progress")
                actionlist = {1:"Initialize new semester", 2:"Log Out"}

            else: 
                print("Semester {} is currently in progress".format(self.state.semester.id))  
                actionlist = {1:"Add an Exercise", 2:"Delete an Exercise", 3:"Log Out"}
        
        elif mode == "Student":
            if self.state.semester == None: 
                print("No semester is currently in progress")
                actionlist = {1:"Log Out"}

            else: 
                print("Semester {} is currently in progress".format(self.state.semester.id))  
                actionlist = {1:"Study", 2:"Log Out"}

        else:
            actionlist = {1:"Log In"}

        for k, v in actionlist.items():
            print("{:<8} {:<15}".format(k, v))

        return actionlist
    
    def getUsrChoice(self) -> int:
        choice = int(input("Choose an option: "))
        return choice

    def moveTo(self, choice, actor, actionlist):

        action = actionlist[choice]
        self.state.action = action

        if action == "Initialize new semester":
            self.state.semester = actor.initNewSemester()

        elif action == "Add an Exercise":
            actor.addExercise(self.state.semester)

        elif action == "Delete an Exercise":
            actor.printSemester(self.state.semester)
            exerciseId = self.getUsrChoice()
            actor.deleteExercise(exerciseId, self.state.semester)
            print("You just deleted an exercise with id {}".format(exerciseId))

        elif action == "Study":
            actor.printSemester()
            exerciseID = self.getUsrChoice()

            if exerciseID not in actor.record.keys():
                actor.openExercise(exerciseID)
                actor.enterAnswer(exerciseID, self.state.semester)
            else:
                exercise = self.state.semester.exercises[exerciseID]
                exercise.print()
        else: 
            self.logout()

        return #change modes
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

class Authenticated:

    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.loggedIn = False
        