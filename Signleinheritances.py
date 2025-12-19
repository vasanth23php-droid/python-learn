class person:
    def __init__(self):
        self.personName = input("Enter Name: ")
        self.personAge = input("Enter Age: ")
    def showDetails(self):
        print(f"The Person Name {self.personName} and his age is {self.personAge}")
class address(person):
    def __init__(self):
        super().__init__()
        self.houseNo = input("Enter House No: ")
        self.streetname = input("Enter Street Name: ")
        self.areaname = input("Enter Area Name: ")
        self.city = input("Enter City: ")
    def show(self):
        super().showDetails()
        print(f" this person address is {self.houseNo} , {self.streetname} , {self.areaname} , {self.city}")
objectAddress = address()
objectAddress.show()

