#Exercise 1
x = input("Enter your name: ")

def hello (name):
    print('Hello, {0}'.format(name))

if __name__ == "__main__":
    hello(x)

#Exercise 2
import matplotlib.pyplot as plot

def f(x):
    return(x + 1)

xs = list(range(-3, 4))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

#Exercise 3
import matplotlib.pyplot as plot

def f(x):
    return(x * x)

xs = list(range(-100, 100))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

#Exercise 4
import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 1:
        return(1)
    else:
        return(-1)

xs = list(range(-5, 5))
ys = []

for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()

#Exercise 5
import matplotlib.pyplot as plot
import math

def f(x):
    return (math.sin(x))

xs = list(range(-5, 5))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

#Exercise 6
from numpy import arange
import matplotlib.pyplot as plot
import math

def f(x):
    return (math.sin(x))

xs = list(arange(-5, 6, .1))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

#Exercise 7
from numpy import arange
import matplotlib.pyplot as plot
import math

def f(c):
    return(c*(9/5)+32)

xs = list(arange(-100, 200, .1))
ys = []

for c in xs:
    ys.append(f(c))

plot.plot(xs, ys)
plot.show()

#Exercise 8
def playAgain():
    a = 'a'
    while a != True and a != False:
        a = input("Play again? (y/n)")
        a = a.lower()
        if a == 'y':
            return(True)
        elif a == 'n':
            return(False)
        else:
            print('Oh come on, that wasn\'t y or n')
