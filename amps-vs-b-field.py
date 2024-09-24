from analyze_data import Data
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
from sklearn.metrics import r2_score


fig, ax1 = plt.subplots(1)
plt.title("Predicted B-field Intensity Vs. Current")
fig.legend()

ax1.set_xlabel("Current (A)")
ax1.set_ylabel("B-field (mT)")

#data
current = np.append(np.arange(0, 1.6, 0.2), [1.8, 2])
print(current)
b_field = np.array([0, 0.001989504123, 0.007759987994, 0.01176044212, 0.01567854613, 0.01999660804, 0.02342996641, 0.02770562575, 0.03375836687, 0.03298252961])
b_field = b_field * 1000

#line of best fit
b, m = polyfit(current, b_field, 1)
yfit = np.polyval((m, b), current)
r2 = r2_score(b_field, yfit)
print(r2)

#plot
ax1.plot(current, b_field, ".", markersize=12)
ax1.plot(current, b + m * current, '-', label='B = {:.1f}*I + {:.1f}'.format(m, b))
ax1.legend(loc='upper left')
plt.show()
#plt.savefig("graphs/BFieldvsAmps.svg")
