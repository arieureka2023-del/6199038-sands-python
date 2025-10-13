# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:08:17 2025

@author: ASUS
"""
import Signals as sig
import numpy as np


_, y = sig.generate_sine_wave(5, 3, 1)
if np.isclose(max(y), 3, atol=1e-6):
    print("Test passed")
else:
    print("Test failed")

def test_generate_sine_wave():
    t, y = sig.generate_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0

    t, y = sig.generate_sine_wave(1, 2, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = sig.generate_sine_wave(1, 2, 1)
    assert len(t) == 0 and len(y) == 0

    t, y = sig.generate_sine_wave(1, 2, 1)
    assert np.allclose(y,0)

# pytest will only run functions that start with "test_  otherwise it will ignore them"
# use pytest to test your code, you dont need a 100% suc6 rate you just need to show that you know to use it and to incorporate it