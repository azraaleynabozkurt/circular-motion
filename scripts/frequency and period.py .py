import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0.1, 5, 500) 

f = 1 / T

plt.figure(figsize=(6,4))
plt.plot(T, f, color='red', linewidth=2)
plt.title("The relationship between Frequency and Period")
plt.xlabel("Period T (second)")
plt.ylabel("Frequency f (Hz)")
plt.grid(True)

plt.savefig("frequency_period.png", dpi=300, bbox_inches="tight")
plt.show()