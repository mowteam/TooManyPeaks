from analyze_data import Data
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit

fig, ax1 = plt.subplots(1)
plt.title("Measured Resonance Frequencies Vs. B-field")
fig.legend()

ax1.set_xlabel("B-field (mT)")
ax1.set_ylabel("Frequency (GHz)")

#data
v_m4 = [0, 0, 0, 2.796120375, 2.777845232, 2.757819177, 2.740419489, 2.72291037, 2.686961959, 2.673173528]
v_p4 = [0, 0, 0, 2.915401251, 2.935700886, 2.956055237, 0, 0, 2.947519541, 2.957258989]
v_m3 = [0, 0, 2.816365294, 2.816474726, 2.801920271, 2.788843147, 2.776149036, 2.765315268, 2.741021365, 2.734838458]
v_p3 = [0, 0, 2.894663887, 2.896360083, 2.913814487, 2.93017457, 2.946261073, 2.964645649, 2.922569046, 2.93154247]
v_m2 = [0, 0, 2.83474987, 2.830263158, 2.824846274, 2.820085982, 2.814067223, 2.810893695, 2.804437207, 2.803014591]
v_p2 = [0, 0, 2.878303804, 2.88492444, 2.893241271, 2.902707139, 2.914033351, 2.92470297, 2.901175091, 2.906154247]
v_m1 = [2.850617509, 2.844325169, 2.849194893, 2.847225117, 2.847608129, 2.848866597, 2.848045857, 2.850726941, 2.831904638, 2.832670662]
v_p1 = [2.860794685, 2.867251172, 2.863913497, 2.868728504, 2.871573736, 2.876607608, 2.881313184, 2.888535696, 2.853353309, 2.856198541]

b_field = np.arange(0, 36, 18*0.2) #np.array([0, 0.001989504123, 0.007759987994, 0.01176044212, 0.01567854613, 0.01999660804, 0.02342996641, 0.02770562575, 0.03375836687, 0.03298252961])
b_field = b_field

#plot
ax1.plot(b_field[3:], v_m4[3:], ".", markersize=7, label="NV4, ms = -1")
t1 = list(b_field[3:6])
t1.extend(b_field[8:])
t2 = list(v_p4[3:6])
t2.extend(v_p4[8:])
ax1.plot(t1, t2, ".", markersize=7, label="NV4, ms = +1")

ax1.plot(b_field[2:], v_m3[2:], ".", markersize=7, label="NV3, ms = -1")
ax1.plot(b_field[2:], v_p3[2:], ".", markersize=7, label="NV3, ms = +1")
ax1.plot(b_field[2:], v_m2[2:], ".", markersize=7, label="NV2, ms = -1")
ax1.plot(b_field[2:], v_p2[2:], ".", markersize=7, label="NV2, ms = +1")
ax1.plot(b_field, v_m1, ".", markersize=7, label="NV1, ms = -1")
ax1.plot(b_field, v_p1, ".", markersize=7, label="NV1, ms = +1")
ax1.legend(loc="lower left")

#predicted
v_p = lambda D, E, g, B: D + pow(E**2 + (g * B)**2, 1/2)
v_m = lambda D, E, g, B: D - pow(E**2 + (g * B)**2, 1/2)
O_1 = -0.9822
O_2 = 0.1688
O_3 = 0.3363
O_4 = 0.4764 + 5

#constants
g = 28
D = 2.8555
E = 0.005

m = v_m(D, E, g, (b_field / O_4) * O_1)
p = v_p(D, E, g, (b_field / O_4) * O_1)
#ax1.plot(b_field, m, '-')
#ax1.plot(b_field, p, '-')

m = v_m(D, E, g, (b_field / O_4) * O_2)
p = v_p(D, E, g, (b_field / O_4) * O_2)
#ax1.plot(b_field, m, '-')
#ax1.plot(b_field, p, '-')

m = v_m(D, E, g, (b_field / O_4) * O_3)
p = v_p(D, E, g, (b_field / O_4) * O_3)
#ax1.plot(b_field, m, '-')
#ax1.plot(b_field, p, '-')

m = v_m(D, E, g, (b_field / O_4))
p = v_p(D, E, g, (b_field / O_4))
#ax1.plot(b_field, m, '-')
#ax1.plot(b_field, p, '-')
fig.set_figwidth(10)
fig.set_figheight(6)
plt.savefig("graphs/ResonanceVsBField.svg")
#plt.show()
