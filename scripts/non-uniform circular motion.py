import numpy as np
import matplotlib.pyplot as plt

r = 5
theta = np.linspace(0, 2*np.pi, 200)  # 1 tur
v0 = 1
alpha = 0.3  

x = r * np.cos(theta)
y = r * np.sin(theta)

v = v0 + alpha * theta                 
a_t = np.full_like(theta, alpha * r)   
a_c = v**2 / r                

plt.figure(figsize=(6,6))
plt.plot(x, y, 'b', linewidth=2, label="Orbit")

indices = np.arange(0, len(theta), 15)

v_x = -v[indices] * np.sin(theta[indices])
v_y = v[indices] * np.cos(theta[indices])
plt.quiver(x[indices], y[indices], v_x, v_y, color='green', scale=20, label="Linear Velocity v")

a_c_x = -a_c[indices] * np.cos(theta[indices])
a_c_y = -a_c[indices] * np.sin(theta[indices])
plt.quiver(x[indices], y[indices], a_c_x, a_c_y, color='red', scale=20, label="Centripetal Acceleration a_c")

a_t_x = -a_t[indices] * np.sin(theta[indices])
a_t_y = a_t[indices] * np.cos(theta[indices])
plt.quiver(x[indices], y[indices], a_t_x, a_t_y, color='orange', scale=20, label="Tangential Acceleration a_t")

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Non-Uniform Circular Motion")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.savefig("Non_uniform_circular_motion.png", dpi=300, bbox_inches="tight")
plt.show()
