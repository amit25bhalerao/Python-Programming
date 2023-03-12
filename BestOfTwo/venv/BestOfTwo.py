# Program To Find Best Of Two Marks

def marks(m1, m2, m3):

    s1 = m1 + m2
    s2 = m2 + m3
    s3 = m3 + m1

    if s1 > s2 and s2 > s3:
        print("The Best Of Two Marks Are: {}, {}".format(m1, m2))
    elif s2 > s1 and s2 > s3:
        print("The Best Of Two Marks Are: {}, {}".format(m2, m3))
    else:
        print("The Best Of Two Marks Are: {}, {}".format(m3, m1))


marks1 = int (input("Enter The Marks In First Subject: "))
marks2 = int (input("Enter The Marks In Second Subject: "))
marks3 = int (input("Enter The Marks In Third Subject: "))
marks(marks1, marks2, marks3)