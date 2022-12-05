database = {"students":{"Kristina":"pass123"}, "schools": {"Awesome School":"pass234"}}

def login(database):
    
    username = input("Please enter your username:")
    password = input("Please enter password:")

    role = None # role should be ENUM type
    loggedInID = None

# restructure into one for loop
    if username in database["students"].keys():
        role = "student"
        if database["students"][username] == password:
            loggedInID = username
            print("Welcome to your ",role," account. \n", "You are loggen in as ", username)
        else: 
            print("Wrong Password")

    elif username in database["schools"].keys():
        role = "school"
        if database["school"][username] == password:
            loggedInID = username
            print("Welcome to your ",role," account. \n", "You are loggen in as ", username)
        else:
            print("Wrong Password")

    else:
        print("No account with such username")

    return role, loggedInID


role, account = None, None

while role == None or account == None:
    role, account = login(database)