# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:08:17 2025

@author: ASUS
"""
import Signals as sig
import numpy as np

def test_generate_sine_wave():
    t, y = sig.generate_sine_wave(5, 2, 100)
    assert y[0] == 0

    t, y = sig.generate_sine_wave(5, 0, 100)
    assert len(t) == 0 and len(y) == 0

    t, y = sig.generate_sine_wave(0, 1, 10)
    assert np.allclose(y, 0)
