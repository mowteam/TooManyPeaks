from analyze_data import Data
import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy.signal import argrelextrema, argrelmin, argrelmax


#data
file = sys.argv[1]
data = Data(file)

#lorentzian
I = lambda G, C, v_m, v_p, v : 1 - C*( pow(G/2, 2) / (pow(v - v_p, 2) + pow(G/2, 2))  +  pow(G/2, 2) / (pow(v - v_m, 2) + pow(G/2, 2)) )
v_p = lambda D, E, g, B: D + pow(E**2 + (g * B)**2, 1/2)
v_m = lambda D, E, g, B: D - pow(E**2 + (g * B)**2, 1/2)
O_1 = -0.9822
O_2 = 0.1688
O_3 = 0.3363
O_4 = 0.4764

#O_1 = -0.983
#O_2 = 0.205
#O_3 = 0.284
#O_4 = 0.493

#constants
g = 28
D = 2.8555
E = 0.005
C = 0.0181
G = 0.0054
m1 = v_m(D, E, g, 0.012 * O_1)
p1 = v_p(D, E, g, 0.012 * O_1)
m2 = v_m(D, E, g, 0.012 * O_2)
p2 = v_p(D, E, g, 0.012 * O_2)
m3 = v_m(D, E, g, 0.012 * O_3)
p3 = v_p(D, E, g, 0.012 * O_3)
m4 = v_m(D, E, g, 0.012 * O_4)
p4 = v_p(D, E, g, 0.012 * O_4)

plt.plot(data.frequency, 0.25 * I(G, C, m1, p1, data.frequency) + 0.25 * I(G, C, m2, p2, data.frequency) + 0.25 * I(G, C, m3, p3, data.frequency) + 0.25 * I(G, C, m4, p4, data.frequency))
plt.plot(data.frequency, data.norm_diode)
plt.show()

