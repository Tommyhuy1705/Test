class People:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def on_honor_roll(self): #check any student in class that honors
        if self.gpa >= 3.5:
            return True
        else:
            return False
    
