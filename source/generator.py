'''Genartor 

Usage:
    generator.py [-n=<Number>] [-m=<X_max>] [-a=<Slope>] [-b=<Intersection>] [-f=<Filename>]
    generator.py (-h|--help)

Options:
    -h --help           Show this menu
    -n=<Number>         Number of points to generate
    -m=<X_max>          Biggest x-value
    -a=<Slope>          Slope coefficient
    -b=<Intersection>   Intersection with Oy in f(0)
    -f=<Filename>       File to save generated data in
'''

import numpy as np
import matplotlib.pyplot as plt
from docopt import docopt
from validator import Validator as vld
import pathvalidate as pv


class DataGenerator():
    def __init__(self, n:int, xMax:float, a:float, b:float, filename:str = "file.txt"):
        self._values = np.ndarray(shape=(2, n))
        self._length = n            # Quantity of generated points in a set
        self._x_max = xMax          # Last x-value in a set
        self._slope = a             # Slope coefficient 
        self._intersection = b      # Shfit term
        self._filename = filename   # File for saving

    def generate(self)->np.ndarray:
        self._values[0] = np.linspace(0, self._x_max, self._length)             # Creating equally spaced x-values
        self._values[1] = self._values[0] * self._slope + self._intersection    # Creating corresponding y-values
        self._values[1] += np.random.normal(loc=0, scale=.5, size=self._length) # Adding Gaussian "noise" to y-values
        return self._values

    def safe(self, array:np.ndarray)->bool:
        np.savetxt(self._filename, array, delimiter=',')
        return True
        
    def plot(self):
        plt.plot(self._values[0], self._values[1], 'ro')
        plt.show()



if __name__ == "__main__":
    args = docopt(__doc__, version = "Generator 0.0.69")
    val = vld()
    # Validating of entries
    # Number of points
    if args["-n"]:
        n = args["-n"]
    else:
        n = input("What's a number of points are to generate:\n>")
    while not val.is_pos_int(n):
        n = input("Your entry must be a positive integer. Try again:\n>")
    n = int(n)

    # Maximal x-value
    if args["-m"]:
        m = args["-m"]
    else:
        m = input("The greatest x-value of generated data:\n>")
    while not val.is_pos_float(m):
        m = input("Your entry must be a positive number. Try again:\n>")
    m = float(m)

    # Slope coefficient
    if args["-a"]:
        a = args["-a"]
    else:
        a = input("Slope coefficient for dependency in generated data:\n>")
    while not val.is_float(a):
        a = input("Your entry must be a float. Try again:\n>")
    a = float(a)

    # Shift
    if args["-b"]:
        b = args["-b"]
    else:
        b = input("Shift term for generated data:\n>")
    while not val.is_float(b):
        b = input("Your entry must be a float. Try again:\n>")
    b = float(b)

    # File for saving
    if args["-f"]:
        filename = args["-f"]
    else:
        filename = input("Where would you like to save your data? (Leave field empty to save it to standart file)\n>")
    while not (pv.is_valid_filepath(filename) or filename == ""):
        filename = input("The name you provided is not valid. Try again: \n>")
    if filename=="":
        filename = "file.txt"
    gen = DataGenerator(n, m, a, b, filename)
    res = gen.generate()
    gen.plot()
    if gen.safe(res):
        print(f"Data was successfuly saved in {filename}!\n")
    else:
        print(f"Something went wrong during saving :(")    

