class Library:
    def __init__(self, acc_number, title, author, pubisher, late_days, fine):
        self.acc_number = acc_number
        self.title = title
        self.author = author
        self.publisher = pubisher
        self.late_days = late_days
        self.fine = fine

    def read(self):
        self.acc_number = int(input("Enter The Account Number: "))
        self.title = input("Enter The Book Title: ")
        self.author = input("Enter The Author Name: ")
        self.publisher = input("Enter The Publisher Name: ")

    def compute(self):
        self.late_days = int(input("Enter The Number Of Days Crossed After DeadLine: "))
        print("Thank You For Providing The Above Details")
        print("*************************************************************************")
        self.fine = self.late_days * 1.50

    def print(self):
        print("Account Number: ", self.acc_number)
        print("Book Title: ", self.title)
        print("Author: ", self.author)
        print("Publisher: ", self.publisher)
        print("Number Of Days Crossed After DeadLine: ", self.late_days)
        print("Fine To Be Paid @ 1.5 Dollars Per Day Is: ", self.fine, "Dollars")


a = 0
b = " "
c = " "
d = " "
e = 0
f = 0
ob = Library(a, b, c, d, e, f)
ob.read()
ob.compute()
ob.print()


