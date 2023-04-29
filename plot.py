import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import serial_reader
import physics
import opencvt

def plotting(coords):
    serial = serial_reader.Readings()
    if serial:
        if serial[0] == 1:
            cue_ball_center, second_ball_center = coords[0], coords[1]
            cue_angle = serial[1]
            return physics.lines(cue_angle, cue_ball_center, second_ball_center)
    return ((0),(0))
        

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

ax.set_facecolor('#004225')

# Add points at the corners
corners_x = [0, 0, 20, 20, 10, 10]
corners_y = [0, 20, 0, 20, 0, 20]
ax.scatter(corners_x, corners_y, s=1000, color='#654321')

coords = opencvt.get_coords();
ax.scatter(coords[0][0], coords[0][1], s=500, color='white')
ax.scatter(coords[1][0], coords[1][1], s=1500, color='gray')
ax.scatter(coords[1][0], coords[1][1], s=500, color='black')


# Initialize an empty line object
line, = ax.plot([], [], lw=2)

# Define a function to update the line data
def update(num):
    plot = plotting(coords)
    x = plot[0]
    y = plot[1]

    # Update the line data
    line.set_data(x, y)

    colors = ['white', 'black']
    line.set_markerfacecolor(colors)

    # Set the title
    ax.set_title('Pool Table')

    # Return the line object
    return line,

# Create an animation object
ani = FuncAnimation(fig, update, frames=1000, interval=1, blit=True)

# Show the plot
plt.show()
