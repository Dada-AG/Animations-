import matplotlib.pyplot as plt
import numpy as np
import time

# Define time range and parameters
time_range = 1
time_step = 0.01
time = np.arange(0, time_range, time_step)

# DC voltage
dc_voltage = 5 * np.ones(len(time))

# AC voltage with random noise
ac_voltage = 5 * np.sin(2 * np.pi * 60 * time) 
# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Plot DC voltage (fixed line)
line1, = ax1.plot(time, dc_voltage, label='DC Voltage')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('DC Voltage vs Time')
ax1.grid(True)
ax1.legend()

# Plot AC voltage (dynamic with noise)
line2, = ax2.plot(time, ac_voltage, label='AC Voltage')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Voltage (V)')
ax2.set_title('AC Voltage vs Time')
ax2.grid(True)
ax2.legend()

plt.ion()  # Turn interactive mode on

# Update the plots in a loop
for i in range(len(time)):
    # Update AC voltage plot
    line2.set_xdata(time[:i+1])
    line2.set_ydata(ac_voltage[:i+1])
    ax2.set_xlim(0, max(time[:i+1]))
    ax2.set_ylim(-6, 6)

    plt.draw()
    plt.pause(time_step)

plt.ioff()  # Turn interactive mode off
plt.show()


