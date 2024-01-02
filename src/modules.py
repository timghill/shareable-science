"""
    Simple module file. Put your functions here.
"""

import numpy as np

def run_simulation():
    """Produce mock 'simulation' data (Gaussian noise)

    Some longer explanation about purpose and science.

    Parameters
    ----------
        None
    
    Returns
    -------
        None"""
    X = np.random.normal(size=(100,100))
    return X

