from pyvisa import *
import numpy as np
import keyoscacquire as koa
import matplotlib.pyplot as plt
import sys

visa_addr = "TCPIP::192.168.1.106::inst0::INSTR"
avgs = [sys.argv[1]]
amps = sys.argv[2]

def averaged_trace(scope, measurement_number, averages=2):
    # Set the number of averages and get a trace
    time, voltages, _ = scope.set_options_get_trace(acq_type=f"AVER{averages}")
    scope.save_trace(fname=f"AMPS={amps},AVG={averages}",
                     showplot=False)
    return time, voltages


def different_averaging(visa_address, measurement_number):
    # Connect to the scope
    with koa.Oscilloscope(address=visa_address) as scope:
        scope.timeout = 100*1000
        # Set the channels to view on the scope
        scope.active_channels = [1, 2]
        # Prepare a two panel plot
        fig, ax = plt.subplots(nrows=2, sharex=True)
        # Obtain traces for different numbers of averages
        for averages in avgs:
            time, voltages = averaged_trace(scope, measurement_number, averages=averages)
            # Plot channel 1 to ax[0] and ch 3 to ax[1]
            for a, ch in zip(ax, voltages.T):
                a.plot(time, ch, label=f"{averages}", alpha=0.5)
        # Add legends to and labels to both plots
        for a, ch_num in zip(ax, scope.active_channels):
            a.set_xlabel("Time [s]")
            a.set_ylabel(f"Channel {ch_num} [V]")
            a.legend()
    plt.show()


different_averaging(visa_address=visa_addr, measurement_number=1)
