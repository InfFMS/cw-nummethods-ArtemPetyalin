import matplotlib.pyplot as plt
import numpy as np
R = 8.314
b = 3.19 * (10 ** (-5))
a = 0.1382
T = 273.15 - 130
V = np.linspace(b + 10 ** (-5), 10 ** (-3), 2000)
P0 = 3664186.998
def P(V):
    return (R * T) / (V - b) - a / (V ** 2) - P0

fig, ax = plt.subplots(figsize=(10, 10))
plt.plot(V, P(V))
plt.grid(True)
eps = 10 ** (-7)
a = 6 * (10 ** (-5))
b1 = 6.25 * (10 ** (-5)) 
while b1 - a > eps:
    c = (a + b1) / 2

    if P(a) + P(c) <= 0:
        b1 = c

    else:
        a = c

print(c - b)
answer = plt.scatter(c, P(c))
plt.show()