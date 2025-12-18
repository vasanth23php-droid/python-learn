class department:
    def __init__(self):
        super().__init__()
        self.departmentName = input("Department Name: ")
        self.departmentCode = input("Department Code: ")
    def showDepartment(self):
        print(f"Your Department name is {self.departmentName} and code is {self.departmentCode}")
        
class course(department):
    def __init__(self):
        super().__init__()
        self.courseName = input("Course Name: ")
        self.courseMajor = input("Course Major: ")
        self.courseAlied = input("Course Alied: ")
    def showCourse(self):
        print(f"Your course is {self.courseName} , major and alied {self.courseMajor} , {self.courseAlied}")
        
class student(course):
    def __init__(self):
        super().__init__()
        self.studentName = input("Student Name: ")
        self.studentId = input("Student Id: ")
    def showStudent(self):
        super().showCourse()
        super().showDepartment()
        print(f"Student Name is {self.studentName} and his id {self.studentId}")
        
objectStudent = student()
objectStudent.showStudent()
