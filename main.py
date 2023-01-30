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