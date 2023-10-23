#Question 4
import math
class QuadraticEquation :
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
        
    def getDiscriminant(self):
        disc = self.__b**2 - 4*self.__a*self.__c
        return disc
    
    def getRoot1(self):
        disc = self.__b**2 - 4*self.__a*self.__c
        if disc >= 0.0:
            r1 = ((-1)*(self.__b) + math.sqrt(disc))/2*self.__a
            return r1
        else:
            return 0
        
    def getRoot2(self):
        disc = self.__b**2 - 4*self.__a*self.__c
        if disc >= 0.0:
            r2 = ((-1)*(self.__b) - math.sqrt(disc))/2*self.__a
            return r2
        else:
            return 0
        
#Discriminant is negative
formula = QuadraticEquation(2, 3, 4)
print(formula.getA())
print(formula.getB())
print(formula.getC())
print(formula.getDiscriminant())
print(formula.getRoot1())
print(formula.getRoot2())

#Discriminant is positive
formula2 = QuadraticEquation(2, 10, 5)
print(formula2.getA())
print(formula2.getB())
print(formula2.getC())
print(formula2.getDiscriminant())
print(formula2.getRoot1())
print(formula2.getRoot2())




