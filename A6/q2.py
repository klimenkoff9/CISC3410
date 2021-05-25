import numpy as numpy
import matplotlib.pyplot as pyplot

x = numpy.array([0.0, 1.0, 4.0, 5.0])
y = numpy.array([0.0, 0.8, -0.8, 1.0])
degree = 3
weights = numpy.polyfit(x,y,degree)

model = numpy.polyId(weights)
print(x.shape)
print(y.shape)

pyplot.scatter(x,y)