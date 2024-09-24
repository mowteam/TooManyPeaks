from analyze_data import Data
import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy.signal import argrelextrema, argrelmin, argrelmax
import pandas as pd
import csv
from labellines import labelLines

#plot data
file = sys.argv[1]
data = Data(file)
plt.plot(data.frequency, data.norm_diode)
plt.xticks(np.linspace(min(data.frequency), max(data.frequency), len(data.frequency)//200))
plt.show(block=False)

temp = argrelextrema(np.array(data.norm_diode), np.less_equal, order=50)[0]
peaks = []
for i in temp:
    if data.norm_diode[i] < 0.9985:
        peaks.append(i)

print(len(peaks))
print(peaks)

for idx, peak in enumerate(peaks):
    plt.axvline(data.frequency[peak], label=str(idx))

labelLines(plt.gca().get_lines())

for idx, i in enumerate(peaks):
    print(str(idx) + ": " + str(i))
correct_peaks = [peaks[int(i)] for i in input("Correct Peaks: ").split()]


arr = []
for p, peak_idx in enumerate(correct_peaks):
    print("Num: " + str(p))
    print("freq: " + str(data.frequency[peak_idx]))
    print("norm voltage: " + str(data.norm_diode[peak_idx]))
    print("C: " + str(1 - data.norm_diode[peak_idx]))
    
    #find Gamma
    min_val = data.norm_diode[peak_idx]
    half_max = (max(data.norm_diode) - min_val) / 2 + min_val

    half_idx = peak_idx
    while data.norm_diode[half_idx] < half_max:
        half_idx -= 1
    
    half_idx2 = peak_idx
    while data.norm_diode[half_idx2] < half_max:
        half_idx2 += 1

    gamma1 = abs(data.frequency[peak_idx] - data.frequency[half_idx])
    gamma2 = abs(data.frequency[peak_idx] - data.frequency[half_idx2])
    gamma = min(gamma1, gamma2)
    print("Gamma: " + str(gamma))
    print()
    
    arr.append(data.frequency[peak_idx])
    arr.append(gamma)
    arr.append(1 - data.norm_diode[peak_idx])

#find D, assuming two peaks closest to D
N = len(correct_peaks) - 1
D_idx = list(data.diode[correct_peaks[N//2]:correct_peaks[N//2 + 1]]).index(max(data.diode[correct_peaks[N//2]:correct_peaks[N//2 + 1]])) + correct_peaks[N//2]
print("D: " + str(data.frequency[D_idx]))

arr.append(data.frequency[D_idx])
arr.append(len(correct_peaks))

with open('peak_analysis.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(arr)
    
