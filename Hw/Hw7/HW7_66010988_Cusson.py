#Question 1
class Clock:
    def __init__(self, period = "AM", hour = 0, minute = 0, second = 0):
        self.period = period
        self.hour = hour
        self.minute = minute
        self.second = second
    def settime(self, hour, minute, second):
        self.period = "AM" if hour < 12 else "PM"
        self.hour = hour
        self.minute = minute
        self.second = second
    def gettime(self):
        while self.second > 60:
            self.second -= 60
            self.minute += 1
        while self.minute > 60:
            self.minute -= 60
            self.hour += 1
        if self.hour > 12:
            self.hour -= 12
        print(str("{:02d}".format(self.hour)) + ":" + str("{:02d}".format(self.minute)) + ":" + str("{:02d}".format(self.second)) + " " + self.period)
    def tick(self):
        self.second += 1
    
clock1 = Clock()
clock1.settime(12, 61, 61)
clock1.gettime()
clock1.tick()
clock1.gettime()
clock1.tick()
clock1.gettime()
clock1.tick()
clock1.gettime()

#Question 2
class Poly:
    def __init__(self, tup):
        vec = []
        for i in tup:
            vec.append(int(i))
        self.a = vec[0] if len(vec)> 0  else 0
        self.b = vec[1] if len(vec)> 1  else 0
        self.c = vec[2] if len(vec)> 2  else 0
        self.d = vec[3] if len(vec)> 3  else 0
        self.e = vec[4] if len(vec)> 4  else 0
        self.f = vec[5] if len(vec)> 5  else 0
    def add(self, p):
        vecp = [int(i) for i in p]
        ayyo = len(vecp)
        while ayyo < 6:
            vecp.append(0)
            ayyo += 1
        self.a += vecp[0]
        self.b += vecp[1]
        self.c += vecp[2]
        self.d += vecp[3]
        self.e += vecp[4]
        self.f += vecp[5]
    def scalar_multiply(self, n):
        self.a *= n
        self.b *= n
        self.c *= n
        self.d *= n
        self.e *= n
        self.f *= n
    def power(self, n):
        result = Poly((self.a, self.b, self.c, self.d, self.e, self.f))
        for _ in range(n - 1):
            result = result.multiply(self)
        return result

    def multiply(self, p):
        result = Poly((0, 0, 0, 0, 0, 0))
        result.a = self.a * p.a
        result.b = self.a * p.b + self.b * p.a
        result.c = self.a * p.c + self.b * p.b + self.c * p.a
        result.d = self.a * p.d + self.b * p.c + self.c * p.b + self.d * p.a
        result.e = self.a * p.e + self.b * p.d + self.c * p.c + self.d * p.b + self.e * p.a
        result.f = self.a * p.f + self.b * p.e + self.c * p.d + self.d * p.c + self.e * p.b + self.f * p.a
        return result

    def printpoly(self):
        terms = []

        if self.a != 0:
            terms.append(str(self.a))
        if self.b != 0:
            terms.append(f"{self.b}x")
        if self.c != 0:
            terms.append(f"{self.c}x^2")
        if self.d != 0:
            terms.append(f"{self.d}x^3")
        if self.e != 0:
            terms.append(f"{self.e}x^4")
        if self.f != 0:
            terms.append(f"{self.f}x^5")

        if len(terms) == 0:
            print("0")
        else:
            result = " + ".join(terms)
            print(result)

    def diff(self):
        if self.a != 0:
            self.a = self.b * 1
        else:
            self.a = 0

        if self.b != 0:
            self.b = self.c * 2
        else:
            self.b = 0

        if self.c != 0:
            self.c = self.d * 3
        else:
            self.c = 0

        if self.d != 0:
            self.d = self.e * 4
        else:
            self.d = 0

        if self.e != 0:
            self.e = self.f * 5
        else:
            self.e = 0
        self.f = 0
        return self
    
    def integrate(self):
        result = Poly((0, 0, 0, 0, 0, 0))

        if self.a != 0:
            result.b = self.a / 1

        if self.b != 0:
            result.c = self.b / 2

        if self.c != 0:
            result.d = self.c / 3

        if self.d != 0:
            result.e = self.d / 4

        if self.e != 0:
            result.f = self.e / 5

        return result
    
    def eval(self, n):
        result = 0
        result += self.a * (n**0)
        result += self.b * (n**1)
        result += self.c * (n**2)
        result += self.d * (n**3)
        result += self.e * (n**4)
        result += self.f * (n**5)
        print(str(result))

p = Poly((1, 0, -2))
q = (1, 2, 3, 4, 5, 6)
p.add(q)
p.printpoly()
p.scalar_multiply(2)
p.printpoly()
q = p.power(2)
q.printpoly()
q.diff()
q.printpoly()
q = q.integrate()
q.printpoly()
q = q.eval(1)




            
            
        
    

#Question 3
class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c
    def getd(self):
        return self.__d
    def gete(self):
        return self.__e
    def getf(self):
        return self.__f
    def isSolvable(self):
        if (self.__a)*(self.__d) - (self.__b)*(self.__c) == 0:
            return False
        else:
            return True
    def getX(self):
        try :
            result = ((self.__e*self.__d - self.__b*self.__f)/(self.__a*self.__d - self.__b*self.__c))
            print(str(result))
        except:
            print("The equation is unsolvable")
    def getY(self):
        try:
            result = ((self.__a*self.__f - self.__e*self.__c)/(self.__a*self.__d - self.__b*self.__c))
            print(str(result))
        except:
            print("The equation is unsolvable")

eq1 = LinearEquation(1, 2, 3, 4, 5, 6)
eq1.geta()
eq1.getb()
eq1.getc()
eq1.getd()
eq1.gete()
eq1.getf()
print(eq1.isSolvable())
eq1.getX()
eq1.getY()

eq2 = LinearEquation(2, 2, 2, 2, 5, 6)
eq2.geta()
eq2.getb()
eq2.getc()
eq2.getd()
eq2.gete()
eq2.getf()
print(eq2.isSolvable())
eq2.getX()
eq2.getY()

    
    
