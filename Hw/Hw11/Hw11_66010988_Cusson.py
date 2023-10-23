#Question 1
import time
class Clock(object):
    def __init__(self):
        self.hh = 0
        self.mm = 0
        self.ss = 0
    def run(self):
        while True:
            self.tick()
            print(f"{self.hh:02}:{self.mm:02}:{self.ss:02}")
            time.sleep(1)
    def setTime(self, h, m, s):
        if 0 <= h <= 23:
            self.hh = h
        else:
            print("Invalid input value")
            return
        if 0<= m <= 59:
            self.mm = m
        else:
            print("Invalid input value")
            return
        if 0 <= s <= 59:
            self.ss = s
        else:
            print("Invalid input value")
            return
    def tick(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
                if self.hh == 24:
                    self.hh = 0

class AlarmClock(Clock):
    def __init__(self):
        super().__init__()
        self.alarm_hh = 0
        self.alarm__mm = 0
        self.alarm_ss = 0
        self.alarm_on_off = False
    def setAlarmTime(self, h, m, s):
        if 0 <= h <= 23:
            self.alarm_hh = h
        else:
            print("Invalid input value")
            return
        if 0<= m <= 59:
            self.alarm__mm = m
        else:
            print("Invalid input value")
            return
        if 0 <= s <= 59:
            self.alarm_ss = s
        else:
            print("Invalid input value")
            return
    def alarm_on(self):
        self.alarm_on_off = True
    def alarm_off(self):
        self.alarm_on_off = False
    def run(self):
        while True:
            self.tick()
            print(f"{self.hh:02}:{self.mm:02}:{self.ss:02}")
            time.sleep(1)
            if self.alarm_on_off and self.hh == self.alarm_hh and self.mm == self.alarm__mm and self.ss == self.alarm_ss:
                print("WAKEUPPP!!")
                break
    
# clock1 = AlarmClock()
# clock1.setTime(24, 60, 60)
# clock1.setAlarmTime(24, 60, 60)
# clock1.setTime(17, 59, 55)
# clock1.setAlarmTime(18, 00, 00)
# clock1.alarm_on()
# clock1.run()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 2
import turtle
turtle.speed(0)
turtle.ht()

def RobotBattle():
    #robotList stores the list of robots in the battle
    robotList = []

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()
        
        #Display the status of each robot
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("================")
            
        #Ask user which robot to command or to create a new robot
        choice = input("Enter which type of robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create")
            robotType = input("'r' for Robot, 'm' for Medicbot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)

        #Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1


class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10

    def draw(self):
        turtle.penup()
        turtle.setpos(self.x, self.y)
        turtle.rt(90)
        turtle.fd(20)
        turtle.lt(90)
        turtle.pendown()
        turtle.circle(20)

    def displayStatus(self):
        print(f"x = {self.x} y = {self.y}")
        print(f"Health = {self.health} Energy = {self.energy}")

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)


class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        if self.energy >= 20 and self.x - r.x <= 10 and self.y - r.y <= 10:
            r.health += 10
            self.energy -= 20
        elif self.energy < 20:
            print("Not enough energy to perform")
        elif self.x - r.x <= 10 and self.y - r.y <= 10:
            print("Robot is not in range")

    def command(self, robotList):
        print("Possible actions: move, heal")
        cmd = str(input("Possible actions : Move(m) , Heal(h): "))
        if cmd == "m":
            newx = int(input("Enter new X coordinate: "))
            newy = int(input("Enter new Y coordinate: "))
            self.move(newx, newy)

        elif cmd == "h":
            robot = int(input("Which one to heal: "))
            self.heal(robotList[robot])

    def draw(self):
        super().draw()
        turtle.pencolor("red")
        turtle.pensize(4)
        turtle.lt(90)
        turtle.fd(30)
        turtle.bk(15)
        turtle.rt(90)
        turtle.bk(15)
        turtle.fd(30)
        turtle.pencolor("black")
        turtle.pensize(1)


class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and self.x - r.x <= 10 and self.y - r.y <= 10:
            r.health -= 50
            self.missile -= 1
            self.energy -= 20
        elif self.missile <= 0:
            print("No misslie left sadly")
        elif self.energy < 20:
            print("Not enough energy to perform")
        elif self.x - r.x <= 10 and self.y - r.y <= 10:
            print("Robot is not in range")

    def displayStatus(self):
        print("x = %d y = %d" % (self.x, self.y))
        print("Health = %d Energy = %d" % (self.health, self.energy))
        print("Missile = %d" %self.missile)

    def command(self, robotList):
        print("Possible actions: move, attack")
        cmd = input("Choose the command: Move(m) or Strike(s): ")
        if cmd == 'm':
            newx = int(input("Enter new X coordinate: "))
            newy = int(input("Enter new Y coordinate: "))
            self.move(newx, newy)
        elif cmd == 's':
            robot = int(input("Which one to strike: "))
            self.strike(robotList[robot])

    def draw(self):
        super().draw()
        turtle.pu()
        turtle.pencolor("blue")
        turtle.lt(90)
        turtle.fd(7)
        turtle.pd()
        turtle.rt(90)
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(8, 360, 4)
        turtle.end_fill()
        turtle.pencolor("black")


# RobotBattle()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 3

class Point(object):
    def __init__(self):
        self.xy = []
    def getpoints(self):
        lst = input("Enter the points:  ")
        lst = [float(i) for i in lst.split()]
        index = len(lst)
        count = 0
        while index != 0:
            result = []
            result.append(float(lst[count]))
            result.append(float(lst[count+1]))
            self.xy.append(result)
            count += 2
            index -= 2

class Rectangle2D(Point):
    def __init__(self):
        super().__init__()
        self.tlx = 0
        self.tly = 0
        self.brx = 0
        self.bry = 0
    def getRectangle(self):
        x_values, y_values = zip(*self.xy) 
        self.tlx = min(x_values)
        self.tly = min(y_values)
        self.brx = max(x_values)
        self.bry = max(y_values)
        for x, y in self.xy:
            self.tlx = min(self.tlx, x)
            self.tly = min(self.tly, y)
            self.brx = max(self.brx, x)
            self.bry = max(self.bry, y)
        center_x = (self.tlx + self.brx) / 2
        center_y = (self.tly + self.bry) / 2
        width = self.brx - self.tlx
        height = self.bry - self.tly
        print(f"The bounding rectangle is centered at  ({center_x}, {center_y}) with width {width} and height {height}")

# rec1 = Rectangle2D()
# rec1.getpoints()
# rec1.getRectangle()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 4
import abc

class Char(abc.ABC):
    def __init__(self):
        pass
    @abc.abstractmethod
    def getWidth(self):
        pass

    @abc.abstractmethod
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        pass
    def drawnum(self, x):
        char0 = Char0()
        char1 = Char1()
        char2 = Char2()
        char3 = Char3()
        char4 = Char4()
        char5 = Char5()
        char6 = Char6()
        char7 = Char7()
        char8 = Char8()
        char9 = Char9()
        char_dict = {
                0: char0,
                1: char1,
                2: char2,
                3: char3,
                4: char4,
                5: char5,
                6: char6,
                7: char7,
                8: char8,
                9: char9
            }
        char = char_dict.get(x)
        char.draw(0, 0)

class Char0(Char):
    def __init__(self):
        super().__init__()
    def draw(self, x ,y):
           super().draw(x, y)
           turtle.circle(10)
    def getWidth(self):
        return "20"

class Char1(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(40)

    def getWidth(self):
        return "1"

class Char2(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.lt(90)
        turtle.forward(20)
        turtle.lt(90)
        turtle.forward(20)
        
    def getWidth(self):
        return "20"

class Char3(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.lt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)

    def getWidth(self):
        return "20"

class Char4(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(25)
        turtle.backward(25)
        turtle.lt(45)
        turtle.forward(20)
        turtle.setheading(270)
        turtle.forward(40)

    def getWidth(self):
        return "20"


class Char5(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(20)
        turtle.backward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.lt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)

    def getWidth(self):
        return "20"


class Char6(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(20)
        turtle.backward(20)
        turtle.rt(90)
        turtle.forward(40)
        turtle.lt(90)
        turtle.forward(20)
        turtle.lt(90)
        turtle.forward(20)
        turtle.lt(90)
        turtle.forward(20)

    def getWidth(self):
        return "20"


class Char7(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(20)
        turtle.rt(115)
        turtle.forward(40)

    def getWidth(self):
        return "20"


class Char8(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.circle(10)
        turtle.penup()
        turtle.rt(90)
        turtle.forward(20)
        turtle.pendown()
        turtle.lt(90)
        turtle.circle(10)

    def getWidth(self):
        return "20"

class Char9(Char):
    def __init__(self):
        super().__init__()

    def draw(self, x, y):
        super().draw(x, y)
        turtle.setheading(0)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)
        turtle.forward(20)
        turtle.rt(90)
        turtle.forward(20)

    def getWidth(self):
        return "20"



# char0 = Char0()
# char1 = Char1()
# char2 = Char2()
# char3 = Char3()
# char4 = Char4()
# char5 = Char5()
# char6 = Char6()
# char7 = Char7()
# char8 = Char8()
# char9 = Char9()
# turtle.speed(0)

# for i in [char0, char1, char2, char3, char4, char5, char6, char7, char8, char9]:
#     i.draw(100,100)

# turtle.penup()
# turtle.home()
# turtle.pendown()
# char = Char0()
# char.drawnum(0)

# turtle.done()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 5
class AbstractItem(abc.ABC):
    def __init__(self, x = 0):
        self.x = x

    @abc.abstractmethod
    def calculate_cost(self):
        pass

class StationaryGood(AbstractItem):
    def __init__(self, x):
        super().__init__(x)

    def calculate_cost(self):
        return self.x

class Magazine(AbstractItem):
    def __init__(self, x):
        super().__init__(x)

    def calculate_cost(self):
        return self.x
    
class Book(AbstractItem):
    def __init__(self, x):
        super().__init__(x)
    def calculate_cost(self):
        return 0.9*self.x
    
class Ribbon(AbstractItem):
    def __init__(self, x):
        super().__init__(x)
    def calculate_cost(self):
        return 5*self.x


#I can do the version where you can pass the quantity inside it as a second argument too but this is more realistic having literlly 3 ComputerWorlds inside a basket.

ComputerWorld_1 = Magazine(70)
ComputerWorld_2 = Magazine(70)
ComputerWorld_3 = Magazine(70)
Window7ForBeginners_1 = Book(200)
Window7ForBeginners_2 = Book(200)
BlueRibbon_10m = Ribbon(10)

basket = [ComputerWorld_1,ComputerWorld_2, ComputerWorld_3, Window7ForBeginners_1, Window7ForBeginners_2, BlueRibbon_10m]

def getTotalcost(lst):
    result = []
    for i in lst:
        x = i.calculate_cost()
        result.append(x)
    return f"{sum(result)} Bahts total"

print(getTotalcost(basket))



