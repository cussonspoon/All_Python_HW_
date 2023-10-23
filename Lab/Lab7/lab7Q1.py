#Question 1
class Time :
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        while self.second >= 60 :
            self.second -= 60
            self.minute += 1
        while self.minute >= 60 :
            self.minute -= 60
            self.hour += 1
    def printit(self):
        print(str("{:02}".format(self.hour)) + ":" + str("{:02}".format(abs(self.minute)) + ":" + str("{:02}".format(abs(self.second)))) + " Hrs.")
time1 = Time(9, 30, 0)
time1.printit()
time2 = Time(9, 61, 61)
time2.printit()

