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

#Workflow
# - implement a login function 
# - handle exceptions
# - add registartion 
# - behaviours for student 
# - behaviour for school

from school import School
from student import Student

database = {"students":{"Kristina":"pass123"}, 
            "schools": {"Awesome School":"pass234"}}
            
def login(database):
    
    username = input("Please enter your username:")
    password = input("Please enter password:")

    role = None # role should be ENUM type

# restructure into one for loop
    if username in database["students"].keys():
        role = "student"
        if database["students"][username] == password:
            print("Welcome to your ",role," account. \n", "You are loggen in as ", username)
        else: 
            print("Wrong Password")

    elif username in database["schools"].keys():
        role = "school"
        if database["school"][username] == password:
            print("Welcome to your ",role," account. \n", "You are loggen in as ", username)
        else:
            print("Wrong Password")

    else:
        print("No account with such username")

    return role, username


""" The function initializes a school instance,
    initializes the semester instance and a student instance,
    evaluates the student.
"""

# how do we initialize the program??? Who initializes the first semester? 
# (length, exercises)
def runAndDeploy():


    role, account = None, None
    while role == None or account == None:
        role, account = login(database)

    #current_semester = Semester(exercises)

    """
    if role =="school":

        student = database["schoold"][account]

        calendar = current_semester.calendar()
        day = calendar.getCurrentDay()

        if day == 0:
            print("Let us initialize a new semester!")
            semester = school.setStudyPlan()

        print("Hello, this is the ", day, "th day of the semester.")
        #print("What would you like to do?")


    #s = School("Michel Lucius")
    #firstSemester = s.setStudyPlan()

    if role == "student":
       
        student = database["students"][account]

        calendar = current_semester.calendar()
        day = calendar.getCurrentDay()

        print("Hi, this is the ", day, "th day of your semester")
        print("Exercise of the day: ", day.exercise)

        student.study() 


    #student = Student("Jack", firstSemester)
    #student.study()

    evaluateStudent(student)
    """
    return

""" The function takes an inctance of class Student as a parameter
    and returns the student's score based on their solutions to the exercises."""
def evaluateStudent(student):

    studentRecord = student.exercises

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