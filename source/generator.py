import numpy as np
import matplotlib.pyplot as plt

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
    print(np.array([[],[]])[1].shape)

    print(np.linspace(0, 10, 20).shape)
    n = int(input("\nHow many points would you like to generate?\n>"))
    x_max = float(input("\nWhat is the greatest x-value?\n>"))
    a = float(input("\nThe slope of linear dependence:\n>"))
    b = float(input("\nValue of shift-term:\n>"))
    filename = input("\nWhere you'd want to save generated data?\n>")

    gen = DataGenerator(n, x_max, a, b, filename)
    res = gen.generate()
    gen.plot()
    if gen.safe(res):
        print(f"Data was successfuly saved in {filename}!\n")
    else:
        print(f"Something went wrong during saving :(")    


