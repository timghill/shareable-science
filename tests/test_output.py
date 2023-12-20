"""
Unit testing for src package.

Tests the function src.run_simulation based on the shape and quantitative
statistics of the returned 'simulation' data x
"""

import numpy as np

import src

class TestClass:
    """Class to consolidate tests"""

    def test_std(self):
        x = src.run_simulation()
        assert np.std(x)>0
    
    def test_mean(self):
        x = src.run_simulation()
        assert np.abs(np.mean(x))<1

    def test_min(self):
        x = src.run_simulation()
        assert np.min(x)<0

    def test_shape(self):
        x = src.run_simulation()
        assert x.shape==(100,100)
