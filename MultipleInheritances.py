class person:
    def __init__(self):
        super().__init__()
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")

    def showPerson(self):
        print(f"The person name is {self.name} and his age is {self.age}")


class permanent:
    def __init__(self):
        super().__init__()
        self.houseno = input("Permanent Addresss House No: ")
        self.streetname = input("Permanent Addresss Street Name: ")
        self.areaName = input("Permanent Addresss Area name: ")
        self.city = input("Permanent Addresss City: ")

    def showPermanentAddresss(self):
        print(f"The person permanent Address is {self.houseno} , {self.streetname} , {self.areaName} , {self.city}")


class temporaryAddress(person, permanent):
    def __init__(self):
        super().__init__()   # Calls person → permanent
        self.Temporaryhouseno = input("Temporary Addresss House No: ")
        self.Temporarystreetname = input("Temporary Addresss Street Name: ")
        self.TemporaryareaName = input("Temporary Addresss Area name: ")
        self.Temporarycity = input("Temporary Addresss City: ")

    def showtemporaryAddresss(self):
        super().showPerson()
        super().showPermanentAddresss()
        print(f"The person temporary Address is {self.Temporaryhouseno} , {self.Temporarystreetname} , {self.TemporaryareaName} , {self.Temporarycity}")


objecttemporaryAddress = temporaryAddress()
objecttemporaryAddress.showtemporaryAddresss()
