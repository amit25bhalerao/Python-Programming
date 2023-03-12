class Student:
    """Attributes: Name, USN, Semester"""

    def __init__(self, name, usn, semester):
        self.name = name
        self.usn = usn
        self.semester = semester


class Exam(Student):
    def __init__(self, name, usn, semester):
        super().__init__(name, usn, semester)
        self.marks = []

    def accept_marks(self):
        print("Enter The Marks Obtained By {} In 6 Subjects".format(self.name))
        for i in range(6):
            marks = int(input("Enter The Marks Of %s In Subject %d: " % (self.name, i + 1)))
            if marks <= 0 or marks > 100:
                print("Marks Entered Are Invalid. The Program Will Terminate.")
                exit(0)

            self.marks.append(marks)


class Result(Exam):
    def __init__(self, name, usn, semester):
        super().__init__(name, usn, semester)
        self.total_marks = 0
        self.percentage = 0

    def calculate(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / 600) * 100

        print("Marks Obtained Out Of 600: ", total_marks)
        print("Percentage Obtained: ", percentage)
        if percentage >= 70:
            print("Result: First Class With Distinction")
        elif percentage >= 60:
            print("Result: First Class")
        elif percentage >= 50:
            print("Result: Second Class")
        elif percentage >= 45:
            print("Result: Third Class")
        else:
            print("Result: Fail")


student_name = input("Enter The Name Of The Student: ")
student_usn = input("Enter The USN Of The Student: ")
student_semester = input("Enter The Semester In Which Student Is Studying: ")
s = Result(student_name, student_usn, student_semester)
s.accept_marks()
s.calculate()