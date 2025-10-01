# -*- coding: utf-8 -*-
import Signals as sig
import matplotlib.pyplot as plt

#generate sine wave function
t, y = sig.generate_sine_wave (4,2,100)
plt.figure (1)
plt.plot (t,y)
plt.grid (True)
plt.title ("Sine wave")
plt.xlable ("time")
plt.ylable("amplitude")
plt.show()


