import numpy as np
import matplotlib.pyplot as plt

r = 5                
omega = 2             
t = np.linspace(0, 2*np.pi/omega, 500)  

x = r * np.cos(omega * t)
y = r * np.sin(omega * t)

v_x = -r * omega * np.sin(omega * t[::50])
v_y = r * omega * np.cos(omega * t[::50])

a_c_x = -omega**2 * x[::50]
a_c_y = -omega**2 * y[::50]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'b', linewidth=2, label="Orbit")
plt.quiver(x[::50], y[::50], v_x, v_y, color='green', scale=20, label="Linear Velocity v")
plt.quiver(x[::50], y[::50], a_c_x, a_c_y, color='red', scale=20, label="Centripetal Acceleration a_c")

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Uniform Circular Motion")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.savefig("Uniform_circular_motion.png", dpi=300, bbox_inches="tight")
plt.show()
