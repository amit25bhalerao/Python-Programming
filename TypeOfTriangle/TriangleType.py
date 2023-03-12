# Program To Detect The Type Of Triangle

def TriangleType(s1, s2, s3):
    if s1 == s2 and s2 == s3 and s3 == s1:
        return 'The Given Triangle Is Equilateral Triangle'
    elif s1 != s2 and s2 != s3 and s3 != s1:
        return 'The Given Triangle Is Scalene Triangle'
    else:
        return 'The Given Triangle Is Isosceles Triangle'


s1 = float(input("Enter The Length Of Side1 Of Triangle: "))
s2 = float(input("Enter The Length Of Side2 Of Triangle: "))
s3 = float(input("Enter The Length Of Side3 Of Triangle: "))

print(TriangleType(s1,s2,s3))
