class User:
    
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def sayName(self):
        print(self.firstname)

    def saySurname(self):
        print(self.lastname)

    def sayFirst_lastName(self):
        print(self.firstname , self.lastname )