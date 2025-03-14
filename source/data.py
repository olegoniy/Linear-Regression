import numpy as np

class Data():

    def __init__(self, n:int):
        self._values = np.ndarray(shape=(2, n))
        self._length = n            # Quantity of generated points in a set
        self._x_max = 0             # Last x-value in a set
        self._slope = 0             # Slope coefficient 
        self._intersection = 0      # Shfit term

    def len(self):
        return self._length

    def setLen(self, n):
        self._values = np.ndarray(shape=(2, n))
        self._length = n

    def setValues(self, row:int, values:np.ndarray):
        self._values[row] = values
        return 0

    def getValues(self, row:int):
        return self._values[row]
    
    def getPoints(self):
        return self._values
    
    def setXmax(self, value:int):
        self._x_max = value
        return 0
    
    def getXmax(self):
        return self._x_max
    
    def setSlope(self, value:float):
        self._slope = value
        return 0
    
    def getSlope(self):
        return self._slope
    
    def setIntersection(self, value:float):
        self._intersection = value
        return 0

    def getIntersection(self):
        return self._intersection
