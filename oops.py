class course:
    def __init__(self):
        self.courseName = input("Enter the Course Name: ")
        self.courseFees = input("Enter the Course Fees: ")
        self.courseDuration = input("Enter the Course Duration: ")
        self.courseMaximum = input("Enter the Course Maximum People: ")
    def show(self):
        print(f"Right Now the following Course is Active {self.courseName} , the fees {self.courseFees} , this duraiton of the {self.courseDuration} and the maximum people for this course {self.courseMaximum} ")
objectCourse = course();
objectCourse.show()
objectCourse1 = course();
objectCourse1.show()
