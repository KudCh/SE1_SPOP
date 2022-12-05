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

from administrator import Administrator
from school import School
from semester import Exercise
from student import Student

userDatabase = {"students":{"Kristina":"pass123"}, 
                "schools":{"Awesome School":"pass234"}, 
                "admins":{"admin":"admin123"}}

defaultExercise = Exercise("Who is the Liskov substitution principle named after?", "Barbara Liskov")
exerciseDatabase = [defaultExercise]

def login(database):
    
    username = input("Please enter your username:")
    password = input("Please enter password:")

    role = None 

    for role in ["student", "school", "admin"]:

        if username in database[role+"s"].keys():
            if database[role+"s"][username] == password:
                print("Welcome to your ",role," account. \n", "You are loggen in as ", username)
            else: 
                print("Wrong Password")
            return role, username

    print("No account with such username")
    return      


""" The function initializes a school instance,
    initializes the semester instance and a student instance,
    evaluates the student.
"""

def runAndDeploy():


    role, username = None, None
    while role == None or username == None:
        role, username = login(userDatabase)

    current_semester = None

    if role =="admin":

        admin = Administrator(username)
        print("Initialize a new semester")
        current_semester = admin.setStudyPlan(exerciseDatabase)

    if role == "student":
       
        student = Student(username)
        try:
            student.exercises = current_semester.exercises
        except: 
            print("No semester in progress")

        student.study(current_semester.exercises[current_semester.current]) # redo the implementation

    if role == "school":
        school = School(username)
        school.addExcercise()

    evaluateStudent(student)
    return

""" The function takes an instance of class Student as a parameter
    and returns the student's score based on their solutions to the exercises."""
def evaluateStudent(student):

    studentRecord = student.progress

    for exercise in studentRecord.keys():
        studentAnswer = studentRecord[exercise]
        if isinstance(studentAnswer, str):
            if exercise[1] == studentAnswer:
                studentRecord[exercise] = 1
            else:
                studentRecord[exercise] = 0

    student.score = sum(studentRecord.values())

    print(student.name, "'s score is ", student.score)

    return

# execution of the program
runAndDeploy()