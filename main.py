import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 5, figsize=(20, 20))
R = 8.314
b = 3.19 * (10 ** (-5))
a = 0.1382
T = 273.15 - 140
V = np.linspace(b + 10 ** (-5), 10 ** (-3), 2000)

for i in range(5):
    T = T + 10
    print(T)
    P = (R * T) / (V - b) - a / (V ** 2)
    ax[i].plot(V, P, label=f"{T - 273.15} deg")
    ax[i].grid(True)
    ax[i].set_xlabel("Объем, м ** 3")
    ax[i].set_ylabel("Давление, Па")
plt.show()

