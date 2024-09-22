import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import argrelmin

class Data:
    
    BASELINE_NOISE = 0.124 #volts
    MIN_FREQ = 2.565 #GHZ
    MAX_FREQ = 2.985 #GHZ

    def __init__(self, filename):
        #read file
        file = pd.read_csv(filename)
        keys = file.keys()
        self.time = np.array(file[keys[0]])
        self.time = self.time - min(self.time)
        self.time_milli = self.time * 1000
        self.waveform = np.array(file[keys[1]]) / 20 #oscilloscope x20 - idk why??
        #self.waveform = (self.waveform - min(self.waveform)) / 10
        self.diode = np.array(file[keys[2]])
        self.frequency = np.linspace(self.MIN_FREQ, self.MAX_FREQ, len(self.time))

        #normalize data
        self.norm_diode = []
        mx = max(self.diode) - self.BASELINE_NOISE
        for idx, item in enumerate(self.diode):
            self.norm_diode.append((item - self.BASELINE_NOISE) / mx)
        
        #get trimmed data
        min_idx = np.argmin(self.waveform)
        max_idx = np.argmax(self.waveform)
        self.trim_data(min_idx, max_idx)

    def trim_data(self, min_idx, max_idx):
        self.diode = self.diode[min_idx:max_idx]
        self.waveform = self.waveform[min_idx:max_idx]
        self.time = self.time[min_idx:max_idx]
        self.time_milli = self.time_milli[min_idx:max_idx]
        self.frequency = self.frequency[min_idx:max_idx]

    #analyzing things
    def graph_diode(self):
        plt.plot(self.time, self.diode)
        #plt.plot(self.trim_time, self.trim_diode)
    
    def graph_waveform(self):
        plt.plot(self.time, self.waveform)

    def find_local_mins(self):
        mins = argrelmin(self.trim_diode, order=30)[0]
        temp = []
        for i in mins:
            if self.trim_diode[i] < 0.9:
                temp.append(self.trim_diode[i])

        return temp

