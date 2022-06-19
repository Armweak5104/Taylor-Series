import matplotlib.pyplot as plt
import numpy as np
import math

X = np.arange(0, math.pi*2, 0.05)
def f1(x):
  return x - (x**3)/6
def f2(x):
  return x - ((x**3)/6) + ((x**5)/120)
def f3(x):
  return x - ((x**3)/6) + ((x**5)/120) - ((x**7)/5040)+(x**9)/362880

Y1 = np.sin(X)
Y2 = []
for i in X:
  Y2.append(f1(i))
Y3 = []
for i in X:
  Y3.append(f2(i))
Y4 = []
for i in X:
  Y4.append(f3(i))






figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Sine Function")

axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("2 taylor terms")

axis[1, 0].plot(X, Y3)
axis[1, 0].set_title("3 taylor terms")

axis[1, 1].plot(X, Y4)
axis[1, 1].set_title("5 taylor terms")


plt.show()
