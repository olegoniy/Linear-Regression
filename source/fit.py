'''Fitting program

Usage:
    fit.py [-f=<Filename>]
    fit.py (-h|--help)
    
Options:
    -h --help       Show this information
    -f=<Filename>   File to read data from (must be csv)
'''

from data import Data
from numpy import genfromtxt as gft
import matplotlib.pyplot as plt
from docopt import docopt
import pathvalidate as pv
import numpy as np


class Fitter():              # Well I am not sure it is proper name for it, but who cares

    def __init__(self):
        self.data = Data(1)
        
    def import_data(self, filename:str)->bool:
        
        tmp = gft(filename, delimiter=',')
        self.data.setLen(tmp.shape[1])
        self.data.setValues(0,tmp[0])
        self.data.setValues(1,tmp[1])   
        self.data.setXmax(tmp[0,-1])

    def _calculate_slope(self):
        ans = 0
        ans += self.data.len()*(self.data.getValues(0)*self.data.getValues(1)).sum()
        ans -= self.data.getValues(0).sum()*self.data.getValues(1).sum()
        ans /= (self.data.getValues(0)**2).sum() - (self.data.getValues(0)).sum()**2
        self.data.setSlope(ans)

    def _calculate_intersection(self):
        ans = self.data.getValues(1).sum() - self.data.getSlope()*self.data.getValues(0).sum()
        ans /= self.data.len()
        self.data.setIntersection(ans)

    def analyse(self):
        self._calculate_slope()
        self._calculate_intersection()


    def plot(self):
        plt.plot(self.data.getValues(0), self.data.getValues(1), "bo")
        tmpX = np.array([0, self.data.getXmax()])
        tmpY = tmpX*self.data.getSlope() + self.data.getIntersection()
        plt.plot(tmpX, tmpY)
        plt.show()

if __name__ == "__main__":
    args = docopt(__doc__,version="Fitting program 0.0.69")
    if args["-f"]:
        filename = args["-f"]
    else:
        filename = input("The file to import data (must be .csv):\n>")
    while not pv.is_valid_filename(filename):
        filename = input("The name, you provided is not to be used! Try again:\n>")
    fitter = Fitter()
    fitter.import_data(filename)
    fitter.analyse()
    fitter.plot()
    print(f"a = {fitter.data.getSlope}")
    print(f"b = {fitter.data.getIntersection}")


    input("Press enter to end the program...")
