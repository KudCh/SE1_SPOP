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