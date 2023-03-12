import copy


class Time:
    """
    attributes: hours, minutes, seconds
    """

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_time(self, t1, t2):

        t = Time(0, 0, 0)
        t.seconds = t1.seconds + t2.seconds
        t.minutes = t1.minutes + t2.minutes
        t.hours = t1.hours + t2.hours

        if t.seconds >= 60:
            t.seconds -= 60
            t.minutes += 1
            if t.minutes >= 60:
                t.minutes -= 60
                t.hours += 1

        return t

    def increment(self, t, sec):
        t.seconds += sec
        while t.seconds >= 60:
            t.seconds -= 60
            t.minutes += 1
            if t.minutes >= 60:
                t.minutes -= 60
                t.hours += 1

        return t

    def pure_increment(self, time, seconds):
        new_time = copy.copy(time)
        a = new_time.seconds + seconds
        b = new_time.minutes + a // 60
        new_time.hours += b // 60
        new_time.minutes = b % 60
        new_time.seconds = a % 60
        return new_time

    def mul_time(self, t, n):
        new_time = copy.copy(t)
        new_time.seconds *= n
        new_time.minutes *= n
        new_time.hours *= n

        while new_time.seconds >= 60:
            new_time.seconds -= 60
            new_time.minutes += 1

        while new_time.minutes >= 60:
            new_time.minutes -= 60
            new_time.hours += 1

        return new_time

    def print_time(self):
        return "Hours: {} Minutes: {} Seconds: {}".format(self.hours, self.minutes, self.seconds)


while True:
    print("Enter 1: Add Two Times To Find The Resultant Time")
    print("Enter 2: Increment Time By Adding Seconds To It")
    print("Enter 3: Pure Version Of Increment")
    print("Enter 4: Multiply Time")
    print("Enter 5: Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        A_hours = int(input("Enter The Value Of Hours For T1: "))
        if A_hours < 0 or A_hours > 23:
            print("Invalid Hour Value Entered!")
            continue

        A_minutes = int(input("Enter The Value Of Minutes For T1: "))
        if A_minutes < 0 or A_minutes > 59:
            print("Invalid Minute Value Entered!")
            continue

        A_seconds = int(input("Enter The Value Of Seconds For T1: "))
        if A_seconds < 0 or A_seconds > 59:
            print("Invalid Seconds Value Entered!")
            continue

        t1 = Time(A_hours, A_minutes, A_seconds)

        B_hours = int(input("Enter The Value Of Hours For T2: "))
        if B_hours < 0 or B_hours > 23:
            print("Invalid Hour Value Entered!")
            continue

        B_minutes = int(input("Enter The Value Of Minutes For T2: "))
        if B_minutes < 0 or B_minutes > 60:
            print("Invalid Minute Value Entered!")
            continue

        B_seconds = int(input("Enter The Value Of Seconds For T2: "))
        if B_seconds < 0 or B_seconds > 60:
            print("Invalid Seconds Value Entered!")
            continue

        t2 = Time(B_hours, B_minutes, B_seconds)

        t3 = Time(0, 0, 0)
        t3 = t3.add_time(t1, t2)
        print("Time T1: {}\nTime T2: {}\nTime T3(Time T1 + Time T2): {}".format(t1.print_time(), t2.print_time(),
                                                                                t3.print_time()))

        print("*******************************************************************************************************")

    elif choice == 2:

        sec = int(input("Enter The Value Of Seconds To Be Added To Given Time: "))

        hours = int(input("Enter The Value Of Hours For Your Desired Time: "))
        if hours < 0 or hours > 23:
            print("Invalid Hour Value Entered!")
            continue

        minutes = int(input("Enter The Value Of Minutes For Your Desired Time: "))
        if minutes < 0 or minutes > 59:
            print("Invalid Minute Value Entered!")
            continue

        seconds = int(input("Enter The Value Of Seconds For Your Desired Time: "))
        if seconds < 0 or seconds > 59:
            print("Invalid Seconds Value Entered!")
            continue

        t = Time(hours, minutes, seconds)
        print("Entered Time: ", t.print_time())

        t = t.increment(t, sec)
        print("Incremented Time: ", t.print_time())

        print("*******************************************************************************************************")

    elif choice == 3:

        sec = int(input("Enter The Value Of Seconds To Be Added To Given Time: "))
        hours = int(input("Enter The Value Of Hours For For Your Desired Time: "))
        if hours < 0 or hours > 23:
            print("Invalid Hour Value Entered!")
            continue

        minutes = int(input("Enter The Value Of Minutes For Your Desired Time: "))
        if minutes < 0 or minutes > 59:
            print("Invalid Minute Value Entered!")
            continue

        seconds = int(input("Enter The Value Of Seconds For Your Desired Time: "))
        if seconds < 0 or seconds > 59:
            print("Invalid Seconds Value Entered!")
            continue

        t = Time(hours, minutes, seconds)
        print("Entered Time: ", t.print_time())

        t = t.pure_increment(t, sec)
        print("Incremented Time: ", t.print_time())

        print("*******************************************************************************************************")

    elif choice == 4:
        n = int(input("Enter The Value By Which You Wish To Multiply The Given Time: "))

        hours = int(input("Enter The Value Of Hours For Your Desired Time: "))
        if hours < 0 or hours > 23:
            print("Invalid Hour Value Entered!")
            continue

        minutes = int(input("Enter The Value Of Minutes For Your Desired Time: "))
        if minutes < 0 or minutes > 59:
            print("Invalid Minute Value Entered!")
            continue

        seconds = int(input("Enter The Value Of Seconds For Your Desired Time: "))
        if seconds < 0 or seconds > 59:
            print("Invalid Seconds Value Entered!")
            continue

        t = Time(hours, minutes, seconds)
        print("Entered Time: ", t.print_time())

        t = t.mul_time(t, n)
        print("Multiplied Time: ", t.print_time())

        print("*******************************************************************************************************")

    elif choice == 5:
        print("Thank You!!")
        exit(0)

    else:
        print("Invalid Input Entered. Please Try Again")
