class student:
    def __init__(self):
        super().__init__()
        self.studentName = input("Student Name: ")
        self.studentid = input("Student Id: ")
    def showStudent(self):
        print(f"The Student is {self.studentName} and his id is {self.studentid}")
        
class campsInterview(student):
    def __init__(self):
        super().__init__()
        self.companyName = input("Company Name: ")
        self.placementId = input("Placement Id: ")
    def showPlacement(self):
        print(f"The Student is placed company {self.companyName} and his id is {self.placementId}")

class sportEvent(student):
    def __init__(self):
        super().__init__()
        self.sportName = input("Sports Name: ")
        self.sportTime = input("Sports Time: ")
    def showsportEvent(self):
        super().showStudent()
        super().showPlacement()
        print(f"The Student is participat the sport event {self.sportName} and time is {self.sportTime}")


objectsportEvent = sportEvent()
objectsportEvent.showsportEvent()
