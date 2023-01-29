class Authenticated:

    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.loggedIn = False
        