from analyze_data import Data
import matplotlib.pyplot as plt
 
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
plt.title("Fluorescencse Intensity Vs. Microwave Frequency for varying B-fields")
fig.legend()

ax1.set_xlabel("Time (ms)")
ax1.set_ylabel("Fluorescence Signal (V)")
ax1.set_ylabel("Waveform Generator (V)")


#AMPS=0
data = Data("data/AMPS=0,AVG=25.csv")
ax1.plot(data.frequency, data.diode, "-b", label="0 A", linewidth = '0.5')

#AMPS=0.6
data = Data("data/AMPS=0.6,AVG=25.csv")
ax2.plot(data.frequency, data.diode, "-b", label="0 A", linewidth = '0.5')

#AMPS=1.2
data = Data("data/AMPS=1.2,AVG=25.csv")
ax3.plot(data.frequency, data.diode, "-b", label="0 A", linewidth = '0.5')

#AMPS=1.8
data = Data("data/AMPS=1.8,AVG=25.csv")
ax4.plot(data.frequency, data.diode, "-b", label="0 A", linewidth = '0.5')

plt.show()
