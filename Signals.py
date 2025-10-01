# -*- coding: utf-8 -*-

import numpy as np

# defines the unit-step funtion
def u (start, finish, amplitude, sample_rate):
    t=np.linspace (start, finish, sample_rate)
    return t, np.where (t<0, 0, amplitude)

# defines sine wave function
def generate_sine_wave (frequency, duration, sample_rate):
    t= np.linspace (0, duration, sample_rate)
    y= np.sin (frequency*2*np.pi*t)
    return t, y
