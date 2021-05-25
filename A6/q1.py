import numpy as numpy
import pandas as pandas
import matplotlib.pyplot as pyplot

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,18,19,20]
y = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95]

pyplot.figure(figsize=(14,10))
for i in range (1,10):
    degree = i
    mymodel = numpy.polyId(numpy.polyfit(x,y,degree))
    myline = numpy.linspace(1,22,100);
    pyplot.subplot(3,3,i)
    pyplot.scatter(x,y)
    pyplot.plot(myline, mymodel(myline))
    pyplot.title("Polynomial" + str(degree))