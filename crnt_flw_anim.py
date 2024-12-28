import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 4)
ax.axis('off')

# Draw the circuit (Battery, wires, and resistor)
# Battery in center of bottom wire (like a resistor)
ax.plot([2.5, 3.5], [1, 1], 'red', lw=6)  # Battery
ax.text(2.4, 0.8, "-", fontsize=12, color='black')  # Negative terminal
ax.text(3.6, 0.8, "+", fontsize=12, color='black')  # Positive terminal
ax.text(2.6, 0.6, "Battery", fontsize=10, color='black')

# Wires
ax.plot([0.5, 2.5], [1, 1], 'black', lw=2)  # Left bottom wire
ax.plot([3.5, 5.5], [1, 1], 'black', lw=2)  # Right bottom wire
ax.plot([5.5, 5.5], [1, 3], 'black', lw=2)  # Right wire
ax.plot([5.5, 0.5], [3, 3], 'black', lw=2)  # Top wire
ax.plot([0.5, 0.5], [3, 1], 'black', lw=2)  # Left wire

# Resistor
ax.plot([2.5, 3.5], [3, 3], 'gold', lw=6)
ax.text(2.9, 3.2, "R", fontsize=10, color='black')

# Electron parameters (moving + to -)
num_electrons = 10
x_positions = np.linspace(5.3, 0.7, num=num_electrons)  # Start near positive terminal
y_positions = np.ones_like(x_positions) * 1  # Starting on bottom wire
electrons, = ax.plot([], [], 'bo', markersize=6, label="Electrons")

# Update function for animation
def update(frame):
    global x_positions, y_positions

    for i in range(len(x_positions)):
        # Move electrons along the bottom wire (+ to -)
        if y_positions[i] == 1 and x_positions[i] > 0.5:
            x_positions[i] -= 0.05  # Slower speed
        # Move electrons up the left wire
        elif x_positions[i] <= 0.5 and y_positions[i] < 3:
            y_positions[i] += 0.05
        # Move electrons along the top wire (left to right)
        elif y_positions[i] >= 3 and x_positions[i] < 5.5:
            x_positions[i] += 0.05
        # Move electrons down the right wire
        elif x_positions[i] >= 5.5 and y_positions[i] > 1:
            y_positions[i] -= 0.05

        # Reset positions to loop electrons
        if x_positions[i] >= 5.3 and y_positions[i] <= 1:
            x_positions[i] = 5.3
            y_positions[i] = 1

    electrons.set_data(x_positions, y_positions)
    return electrons,

# Animate
ani = animation.FuncAnimation(fig, update, frames=400, interval=50, blit=True)
plt.legend()
plt.show()
