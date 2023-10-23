from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self):
        self.start = ""
        self.end = ""

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, dist):
        super().__init__()
        self.dist = dist
        self.station = "-"
    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, dist):
        super().__init__()
        self.dist = dist
        self.station = "-"
    def find_cost(self):
        return self.dist*40
    
class Train(Transportation):
    def __init__(self, station):
        super().__init__()
        self.station = station
    def find_cost(self):
        return self.station*5
    
walk = Walk(0.6)
taxi1 = Taxi(5)
train = Train(6)
taxi2 = Taxi(3)

list = [walk, taxi1, train, taxi2]

for i in list:
    cost = i.find_cost()
    print(str(cost) + " Baht")