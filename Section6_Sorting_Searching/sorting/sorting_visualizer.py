import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def my_plotter(ax, indexes, values, param_dict):
    '''
    A helper function to make a graph

    Parameters
    ----------
    ax: Axes
        The axes to draw to

    index: list
        The x data

    values: list
        The y data

    param_dict: dict
        Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out: list
        list of artists added
    '''
    out = ax.plot(indexes, values, **param_dict)
    return out


def plot_sin(amplitude):
    x = np.linspace(-np.pi, np.pi, 100)
    y = amplitude * np.sin(x)
    plt.plot(x, y, label="Sine Function")

    plt.xlabel("Angle [rad]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.axis("tight")
    plt.show()


def plot_cos(amplitude):
    x = np.linspace(-np.pi, np.pi, 100)
    y = amplitude * np.cos(x)
    plt.plot(x, y, label="Cosine Function")

    plt.xlabel("Angle [rad]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.axis("tight")
    plt.show()


plot_sin(1)
plot_cos(5)
