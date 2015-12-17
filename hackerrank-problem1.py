# HL machine learning: Normal Distribution #1

"""
p(x<b) is calculated using the integral of a gaussian distribution from infinity to b.

Infinity is approximated by a large number INFINITY, and DELTLA for the discrete integral
is approximated by a small number.

"""

import math

def arange(l, h, inc):
    """List of numbers from l to h with incremental value of inc"""
    num = int((h-l)/inc)+1
    x = []
    for i in range(0, num):
        x.append(l+inc*i)
    return x

def normal_dis(x, sigma, mu):
    """Normal distribution calculated for list x, with standard deviation sigma
    and mean mu"""
    y = []
    for i in range(0,len(x)):
        y.append(math.exp(-(x[i]-mu)**2/(2*sigma**2))/(sigma*math.sqrt(2*math.pi)))
    return y

DELTA = 1e-3 # the increamental value for integral
INFINITY = 1000

# p(x<40)
x = arange(-INFINITY, 40, DELTA)
y = normal_dis(x, 4, 30)
print "%.3f" % (DELTA*sum(y)) # The integral is calculated by the sum of the discreted values

# p(x>21)
x = arange(21, INFINITY, DELTA)
y = normal_dis(x, 4, 30)
print "%.3f" % (DELTA*sum(y))

# p(30<x<35)
x = arange(30, 35, DELTA)
y = normal_dis(x, 4, 30)
print "%.3f" % (DELTA*sum(y))