# -*- coding: utf-8 -*-
import Signals as sig
import matplotlib.pyplot as plt

#generate sine wave function
t, y = sig.generate_sine_wave (4,2,1000)
plt.figure (1)
plt.plot (t,y)
plt.grid (True)
plt.title ("Sine wave")
plt.xlabel ("time (s)")
plt.ylabel("amplitude")
plt.show()

#generate unit step function 
t, y = sig.u (-10, 10, 3, 10000)
plt.figure (2)
plt.plot (t, y)
plt.grid (True)
plt.title ("Unit step")
plt.xlabel ("time (s)")
plt.ylabel("height (m)")
plt.show()

#generate modified sine wave function
t, y = sig.modified_sine_wave(4,2,1000,amplitude=10.0)
plt.figure (3)
plt.plot (t,y)
plt.grid (True)
plt.title ("Modified sine wave")
plt.xlabel ("time (s)")
plt.ylabel("amplitude")
plt.show()

#generate modified unit step function
t, y= sig.modified_u(-10,10,-2,3,10000)
plt.figure (4)
plt.plot (t, y)
plt.grid (True)
plt.title ("Modified unit step")
plt.xlabel ("time (s)")
plt.ylabel("height (m)")
plt.show()
