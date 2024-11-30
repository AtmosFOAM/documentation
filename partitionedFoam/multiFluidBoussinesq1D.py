import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

H = 100
gamma = 0.01
W = gamma*pi/H

print('Wmax =', W)

z = np.linspace(0, H, 41)

w = W*np.sin(pi*z/H)
b = W*pi/H*np.sin(pi*z/H)*(W*np.cos(pi*z/H) + gamma*pi/H)

plt.plot(w, z, label='w')
plt.plot(b, z, label = 'b')
plt.legend()
plt.show()
