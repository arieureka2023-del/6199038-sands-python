# -*- coding: utf-8 -*-

import numpy as np

# defines the unit-step funtion
def u (start, finish, amplitude, sample_rate):
    t=np.linspace (start, finish, sample_rate)
    return t, np.where (t<0, 0, amplitude)


