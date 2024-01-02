import numpy as np
import cmocean
from matplotlib import pyplot as plt

def run_simulation(size=(100,100)):
    """Produce mock 'simulation' data (Gaussian noise)

    Some longer explanation about purpose and science.

    Parameters
    ----------
        size : tuple of int
               Size of simulation data to produce
    
    Returns
    -------
        np.ndarray
               Simulation 'data' with shape `size`
    """
    X = np.random.normal(size=size)
    return X

def plot_simulation(X, cmap=cmocean.cm.balance,
    vmin=-2, vmax=2):
    """Plot mock simulation data.

    Pseudocolor plot of the mock simulation data using
    cmocean colormaps.

    Parameters
    ----------
        X : np.ndarray
            Simulation data
        cmap :
               Valid matplotlib colormap for pcolormesh `cmap` argument
        vmin, vmax : int
                     Min and max colorbar limits
    """
    plt.pcolormesh(X, cmap=cmap, vmin=vmin, vmax=vmax)

