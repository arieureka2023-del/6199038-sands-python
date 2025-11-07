# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:08:17 2025

@author: ASUS
"""
import Signals as sig
import numpy as np

#testing generate_sine_wave function
def test_generate_sine_wave():
    t, y = sig.generate_sine_wave(5, 2, 100)
    assert y[0] == 0

    t, y = sig.generate_sine_wave(5, 0, 100)
    assert len(t) == 100 and len(y) == 100

    t, y = sig.generate_sine_wave(0, 1, 10)
    assert np.allclose(y, 0)

#testing modified_sine_wave function
def test_modified_sine_wave():
    t, y = sig.modified_sine_wave(5, 2, 10000, amplitude=10.0)
    
    assert y[0] == 0 
    
    assert len(t) == 10000
    
    assert np.allclose(max(y), 10, atol=1e-6)
    
#testing generate_u function
def test_generate_u():
    t, y= sig.generate_u(-10,10,3,10000)
   
    assert y[0] == 0
    assert y[9000] == 3 
    
    assert len(t) == 10000
   
    assert np.allclose(max(y),3, atol=1e-6)
    
#testing modified_u function
def test_modified_u():
    t, y= sig.modified_u(-10,10,-2,3,10000)
    
    assert y[0] == 0
    assert y[9000] == 3
    
    assert len(t) == 10000
    
    assert np.allclose(max(y), 3, atol=1e-6)

 