import math
class Calculator(object):
    def __init__(self):
        acc = 0
        self.acc = "{:.2f}".format(acc)
    def set_accumulator(self, a):
        self.acc = a
    def get_accumulator(self):
        return "{:.2f}".format(self.acc)
    def add(self, x):
        self.acc += x
    def subtract(self, x):
        self.acc -= x
    def multiply(self, x):
        self.acc *= x
    def divide(self, x):
        try:
            self.acc /= x
        except:
            print("Value Error")
    def printresult(self):
        return "Result: " + "{:.2f}".format(self.acc)
    
class Sci_calc(Calculator):
    def __init__(self):
        super().__init__()
    def square(self):
        self.acc = self.acc*self.acc
    def exp(self, x):
        self.acc = math.pow(self.acc, x)
    def factorial(self):
        sum = 1
        while self.acc > 0:
            sum *= self.acc
            self.acc -= 1
        self.acc = sum
    def printresult(self):
        return super().printresult()



calc = Sci_calc()
calc.set_accumulator(10)
print(calc.get_accumulator())
print(calc.printresult())
calc.add(10)
print(calc.printresult())
calc.subtract(5)
print(calc.printresult())
calc.multiply(5)
print(calc.printresult())
calc.divide(25)
print(calc.printresult())
calc.square()
print(calc.printresult())
calc.exp(2)
print(calc.printresult())
calc.factorial()
print(calc.printresult())
calc.divide(0)
print(calc.printresult())