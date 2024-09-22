from analyze_data import Data
import matplotlib.pyplot as plt
 
fig, ax1 = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(8)
ax2 = ax1.twinx()


#AMPS=0 and waveform
data = Data("data/AMPS=0,AVG=25.csv")
ax1.plot(data.time_milli, data.diode, "-b", label="Fluorescence", linewidth = '0.5')
ax2.plot(data.time_milli, data.waveform, "-g", label="Waveform", linewidth = '0.5')

plt.title("Fluorescencse Intensity Vs. Waveform Signal for no B-field")
fig.legend()

ax1.set_xlabel("Time (ms)")
ax1.set_ylabel("Fluorescence Signal (V)")
ax2.set_ylabel("Waveform Generator (V)")
plt.savefig("graphs/WaveformVsSignal.svg")

