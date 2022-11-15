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

from school import School
from student import Student


""" The function initializes a school instance,
    initializes the semester instance and a student instance,
    evaluates the student.
"""
def runAndDeploy():

    s = School("Michel Lucius")
    firstSemester = s.setStudyPlan()

    student = Student("Jack", firstSemester)
    student.study()

    evaluateStudent(student)

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