import numpy as np
import matplotlib.pyplot as plt

# Ask the user for input
v0 = float(input("Enter the initial velocity (m/s): "))  # Initial velocity
theta = float(input("Enter the angle of projection (degrees): "))  # Angle of projection

# Constants
g = 9.81  # Acceleration due to gravity
theta_rad = np.radians(theta)  # Convert angle to radians

# Calculate time of flight
t_flight = 2 * v0 * np.sin(theta_rad) / g

# Calculate maximum height and horizontal range
max_height = (v0**2 * np.sin(theta_rad)**2) / (2 * g)
horizontal_range = (v0**2 * np.sin(2 * theta_rad)) / g

# Display results
print(f"Maximum Height: {max_height:.2f} m")
print(f"Horizontal Range: {horizontal_range:.2f} m")

# Create time array
t = np.linspace(0, t_flight, num=500)  # Time values for simulation

# Calculate horizontal and vertical positions
x = v0 * np.cos(theta_rad) * t  # Horizontal position
y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2  # Vertical position

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Projectile Motion')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)

# Save the plot as an image
plt.savefig('projectile_motion.png')

# Show the plot
plt.show()