import numpy as np
import matplotlib.pyplot as plt

r = 2

omega = np.linspace(0, 10, 500)

v = r * omega

plt.figure(figsize=(6,4))
plt.plot(omega, v, color='green', linewidth=2)
plt.title("The relationship between angular velocity ω and linear velocity v")
plt.xlabel("Angular Velocity ω (rad/s)")
plt.ylabel("Linear Velocity v (m/s)")
plt.grid(True)

plt.savefig("The relationship between angular velocity and linear velocity.png", dpi=300, bbox_inches="tight")
plt.show()
