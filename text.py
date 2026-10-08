import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
t= np.linspace(0, 1, 1000)
signal = np.sin(2* np.pi * 10* t)

plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
