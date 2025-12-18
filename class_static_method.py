class company:
    companyName = 'k2bsolution'
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def changeCompany(cls, changeName):
        cls.companyName = changeName
        return cls.companyName
    
print(company.changeCompany("Interlace"))

